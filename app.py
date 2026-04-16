import streamlit as st
import json
import os
from database_jadwal import hal_higdon_db

# --- CONFIGURATION ---
st.set_page_config(page_title="Asisten Lari Cerdas", layout="wide")
DB_FILE = "database_user.json"

def simpan_data(data):
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db_lama = json.load(f)
    else:
        db_lama = []
    db_lama.append(data)
    with open(DB_FILE, "w") as f:
        json.dump(db_lama, f, indent=4)

# --- KNOWLEDGE BASE JARAK ---
jarak_ke_km = {
    "5K": 5.0,
    "10K": 10.0,
    "Half Marathon": 21.1,
    "Marathon": 42.2
}

def hitung_zona_pace(jam, menit, detik, jarak_label):
    jarak_km = jarak_ke_km[jarak_label]
    total_waktu_detik = (jam * 3600) + (menit * 60) + detik
    if total_waktu_detik == 0: return None
    pace_detik_per_km = int(total_waktu_detik / jarak_km)
    
    def format_waktu(total_detik):
        if total_detik <= 0: return "Sprint"
        m = total_detik // 60
        s = total_detik % 60
        return f"{m}:{s:02d}/km"

    return {
        "Finis": f"{jam:02d}:{menit:02d}:{detik:02d}",
        "RP": format_waktu(pace_detik_per_km),
        "Easy": f"{format_waktu(pace_detik_per_km + 60)} - {format_waktu(pace_detik_per_km + 90)}",
        "Tempo": f"{format_waktu(pace_detik_per_km + 10)} - {format_waktu(pace_detik_per_km + 20)}",
        "Interval": f"{format_waktu(pace_detik_per_km - 15)} - {format_waktu(pace_detik_per_km - 5)}",
        "Long": f"{format_waktu(pace_detik_per_km + 60)} - {format_waktu(pace_detik_per_km + 120)}"
    }

if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# --- PAGE 1: ONBOARDING ---
if st.session_state.page == 'onboarding':
    st.title("🏃 Selamat Datang di Asisten Lari Cerdas")
    
    # Menghapus st.form agar UI menjadi responsif/real-time
    st.subheader("📝 Profil & Target")
    col1, col2 = st.columns(2)
    nama = col1.text_input("Nama Lengkap:")
    jarak_target = col2.selectbox("Target jarak lomba?", list(hal_higdon_db.keys()))
    
    st.markdown("---")
    st.subheader("⏱️ Target Waktu Finis")
    punya_target = st.radio("Target waktu?", ["Saya hanya ingin finis dengan aman (Pemula)", "Saya punya target waktu finis"])
    
    # LOGIKA DISABLE: Jika user pilih 'Pemula', maka waktu_disabled bernilai True
    waktu_disabled = "Pemula" in punya_target
    
    col_j, col_m, col_s = st.columns(3)
    # Parameter 'disabled' dipasang di sini
    jam_finis = col_j.number_input("Jam:", min_value=0, max_value=10, value=0, disabled=waktu_disabled)
    menit_finis = col_m.number_input("Menit:", min_value=0, max_value=59, value=25, disabled=waktu_disabled)
    detik_finis = col_s.number_input("Detik:", min_value=0, max_value=59, value=0, disabled=waktu_disabled)

    st.markdown("---")
    st.subheader("👟 Tes Kebugaran")
    cedera = st.selectbox("Riwayat cedera?", ["Tidak ada", "Ada nyeri ringan", "Ya, cedera berat"])
    frekuensi = st.radio("Frekuensi lari?", ["< 1x", "1-2x", "3-4x", "> 4x seminggu"])
    speedwork = st.radio("Familiar Speedwork?", ["Tidak", "Pernah", "Ya, Rutin"])
    sisa_waktu = st.slider("Sisa minggu?", 1, 30, 8)
    
    # Mengganti form_submit_button menjadi button biasa
    submit_profil = st.button("Analisis & Hasilkan Jadwal")

    if submit_profil:
        level_rekomendasi = ""
        if "cedera" in cedera and "Ya" in cedera: level_rekomendasi = "Walkers"
        else:
            if frekuensi == "< 1x": level_rekomendasi = "Novice" if "Novice" in hal_higdon_db[jarak_target] else "Novice 1"
            elif frekuensi == "1-2x": level_rekomendasi = "Novice" if "Novice" in hal_higdon_db[jarak_target] else "Novice 2"
            else: level_rekomendasi = "Intermediate" if "Intermediate" in hal_higdon_db[jarak_target] else "Intermediate 1"

        user_data = {"nama": nama, "jarak": jarak_target, "level": level_rekomendasi, "sisa_waktu": sisa_waktu, "punya_target": punya_target, "jam_finis": jam_finis, "menit_finis": menit_finis, "detik_finis": detik_finis}
        simpan_data(user_data)
        st.session_state.user_data = user_data
        st.session_state.page = 'jadwal'
        st.rerun()

# --- PAGE 2: HASIL JADWAL ---
elif st.session_state.page == 'jadwal':
    data = st.session_state.user_data
    st.title(f"📊 Program {data['level']} {data['jarak']}")
    if st.button("⬅️ Kembali"):
        st.session_state.page = 'onboarding'
        st.rerun()
    
    st.subheader("🎯 Target & Intensitas")
    if "punya target" in data['punya_target']:
        zona = hitung_zona_pace(data['jam_finis'], data['menit_finis'], data['detik_finis'], data['jarak'])
        if zona:
            st.success(f"Target Pace Lomba: **{zona['RP']}**")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Easy Run", zona['Easy'])
            c2.metric("Long Run", zona['Long'])
            c3.metric("Tempo", zona['Tempo'])
            c4.metric("Interval", zona['Interval'])
    else:
        st.info("💡 Gunakan Skala Usaha (RPE): Santai (3-4/10), Tempo (6-7/10), Interval (8/10).")

    # LOGIKA PENGAMBILAN JADWAL
    jarak, level, sisa_waktu = data['jarak'], data['level'], data['sisa_waktu']
    durasi_ideal = hal_higdon_db[jarak][level]["durasi_minggu"]
    jadwal_mentah = hal_higdon_db[jarak][level]["jadwal"]
    jadwal_terpilih = {}
    
    range_minggu = range(durasi_ideal - sisa_waktu + 1, durasi_ideal + 1) if sisa_waktu < durasi_ideal else range(1, durasi_ideal + 1)
    for i in range_minggu:
        key = str(i) if str(i) in jadwal_mentah else i
        jadwal_terpilih[i] = jadwal_mentah[key]

    ada_lomba_tuneup = False
    ada_interval = False
    list_minggu = sorted(list(jadwal_terpilih.keys()))
    minggu_terakhir = list_minggu[-1] if list_minggu else 0
    
    tabel_rapi = []
    for m, h in jadwal_terpilih.items():
        if m != minggu_terakhir:
            if any("Lomba" in str(v) for v in h.values()):
                ada_lomba_tuneup = True
        
        if any(" x " in str(v) or "400" in str(v) for v in h.values()):
            ada_interval = True

        label = f"Minggu {m}" if sisa_waktu >= durasi_ideal else f"H-{minggu_terakhir-m+1}"
        baris = {"Minggu Ke-": label}; baris.update(h); tabel_rapi.append(baris)
    
    st.table(tabel_rapi)

    if ada_lomba_tuneup:
        st.info("💡 **Info Tune-up Race:** Gunakan 'Lomba' di tengah jadwal untuk simulasi. Jika tidak ada event resmi, lakukan Time Trial (Lari mandiri secepat mungkin) sesuai jarak tersebut.")

    # PENJELASAN & GLOSARIUM DINAMIS
    st.markdown("---")
    
    if ada_interval:
        col_a, col_b = st.columns(2)
        with col_a:
            with st.expander("❓ CARA MEMBACA LATIHAN INTERVAL (Contoh: 4 x 400m)", expanded=True):
                st.markdown("""
                Jika Anda melihat instruksi **"4 x 400 m"**, lakukan langkah berikut:
                1. **Pemanasan:** Joging santai 1-2 km.
                2. **Inti:** Lari cepat 400 meter.
                3. **Pemulihan:** Jalan santai atau joging pelan selama 400 meter (atau 2-3 menit) sampai napas kembali tenang.
                4. **Ulangi:** Lakukan fase Lari & Pemulihan sebanyak 4 kali.
                5. **Pendinginan:** Joging santai 1 km untuk melemaskan otot.
                """)
        with col_b:
            with st.expander("📖 PANDUAN ISTILAH LATIHAN", expanded=True):
                st.markdown("""
                * **Istirahat:** Vital untuk pemulihan dan membangun kekuatan otot.
                * **Lari Santai:** Fokus pada jarak, Anda wajib bisa lari sambil mengobrol.
                * **Lari Tempo:** Lari yang makin cepat di tengah sesi untuk melatih ambang batas anaerobik.
                * **Lari Jarak Jauh:** Latihan daya tahan mingguan dengan intensitas paling santai.
                * **Cross Training:** Olahraga lain (sepeda/renang) untuk melatih jantung tanpa beban sendi.
                """)
    else:
        with st.expander("📖 PANDUAN ISTILAH & FILOSOFI LATIHAN", expanded=True):
            st.markdown("""
            * **Istirahat (Rest):** Sangat vital untuk pemulihan dan membangun kembali kekuatan otot.
            * **Lari Santai (Run):** Fokus pada menyelesaikan jarak, bukan kecepatan. Anda wajib bisa berlari sambil mengobrol dengan nyaman.
            * **Lari Jarak Jauh (Long Runs):** Latihan daya tahan mingguan. Lakukan dengan santai, jangan paksakan kecepatan.
            * **Lari/Jalan (Run/Walk):** Anda tidak harus berlari tanpa henti. Larilah sampai lelah, lalu berjalanlah untuk memulihkan napas.
            * **Cross Training:** Berolahraga lain (seperti bersepeda atau berenang) untuk melatih jantung tanpa memberikan beban tambahan pada sendi kaki.
            """)