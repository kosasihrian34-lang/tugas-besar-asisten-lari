import streamlit as st
import json
import os
from database_jadwal import hal_higdon_db

# --- CONFIGURATION ---
st.set_page_config(page_title="Asisten Lari Cerdas", layout="wide")

# File untuk menyimpan data user secara permanen
DB_FILE = "database_user.json"

# Fungsi untuk menyimpan data ke JSON (Penyimpanan Data)
def simpan_data(data):
    # Membaca data lama jika ada
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db_lama = json.load(f)
    else:
        db_lama = []
    
    db_lama.append(data)
    with open(DB_FILE, "w") as f:
        json.dump(db_lama, f, indent=4)

# --- KNOWLEDGE BASE: DESKRIPSI JARAK ---
deskripsi_jarak = {
    "5K": "Jarak kompetitif pertama. Lomba ini menyenangkan dan pemulihannya cepat[cite: 2, 5].",
    "10K": "Langkah lanjutan untuk meningkatkan catatan waktu (PR) dengan speedwork[cite: 48, 56].",
    "Half Marathon": "Persiapan ideal sebelum marathon penuh. Fokus pada daya tahan[cite: 50].",
    "Marathon": "Puncak lari jarak jauh. Menekankan performa maksimal dan pemulihan[cite: 105, 112]."
}

if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# --- PAGE 1: ONBOARDING ---
if st.session_state.page == 'onboarding':
    st.title("🏃 Selamat Datang di Asisten Lari Cerdas")
    
    with st.form("form_profil"):
        st.subheader("📝 Profil & Riwayat Kesehatan")
        col_n, col_u = st.columns(2)
        nama = col_n.text_input("Nama Lengkap:")
        usia = col_u.number_input("Usia (Tahun):", min_value=10, max_value=80, value=20)
        
        cedera = st.selectbox(
            "Riwayat cedera 6 bulan terakhir?",
            ["Tidak ada, sehat 100%", "Ada nyeri ringan", "Pernah cedera berat/masih pengobatan"]
        )
        
        st.markdown("---")
        st.subheader("👟 Tes Kebugaran")
        jarak_target = st.selectbox("Target jarak?", list(hal_higdon_db.keys()))
        frekuensi = st.radio("Frekuensi lari (3 bulan terakhir)?", ["< 1x seminggu", "1-2x seminggu", "3-4x seminggu", "> 4x seminggu"])
        speedwork = st.radio("Familiar Speedwork?", ["Tidak", "Pernah", "Ya, Rutin"])
        sisa_waktu = st.slider("Minggu sisa?", 1, 30, 8)
        
        submit_profil = st.form_submit_button("Simpan & Hasilkan Jadwal")

    if submit_profil:
        # LOGIKA SISTEM PAKAR
        level_rekomendasi = ""
        if "cedera berat" in cedera:
            level_rekomendasi = "Walkers"
        else:
            if frekuensi == "< 1x seminggu": level_rekomendasi = "Novice" if "Novice" in hal_higdon_db[jarak_target] else "Novice 1"
            elif frekuensi == "1-2x seminggu": level_rekomendasi = "Novice" if "Novice" in hal_higdon_db[jarak_target] else "Novice 2"
            elif frekuensi == "3-4x seminggu": level_rekomendasi = "Intermediate" if "Intermediate" in hal_higdon_db[jarak_target] else "Intermediate 1"
            else: level_rekomendasi = "Advance" if speedwork == "Ya, Rutin" else "Intermediate"

        user_data = {"nama": nama, "usia": usia, "jarak": jarak_target, "level": level_rekomendasi, "sisa_waktu": sisa_waktu}
        
        # PROSES PENYIMPANAN DATA (PERMANEN KE FILE JSON)
        simpan_data(user_data)
        
        st.session_state.user_data = user_data
        st.session_state.page = 'jadwal'
        st.rerun()

# --- PAGE 2: HASIL JADWAL ---
elif st.session_state.page == 'jadwal':
    data = st.session_state.user_data
    st.title(f"📊 Analisis Jadwal: {data['nama']}")
    
    if st.button("⬅️ Kembali"):
        st.session_state.page = 'onboarding'
        st.rerun()
    
    st.info(f"**Program:** {data['level']} {data['jarak']}\n\n{deskripsi_jarak[data['jarak']]}")

    # LOGIKA PENGAMBILAN JADWAL
    jarak, level, sisa_waktu = data['jarak'], data['level'], data['sisa_waktu']
    durasi_ideal = hal_higdon_db[jarak][level]["durasi_minggu"]
    jadwal_mentah = hal_higdon_db[jarak][level]["jadwal"]
    jadwal_terpilih = {}
    
    # Ambil jadwal
    if sisa_waktu < durasi_ideal:
        minggu_mulai = durasi_ideal - sisa_waktu + 1
        for i in range(minggu_mulai, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]
    else:
        for i in range(1, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]

    # FIX LOGIKA LOMBA TUNE-UP:
    # Hanya muncul jika ada kata 'Lomba' di luar minggu terakhir jadwal yang ditampilkan
    ada_lomba_tuneup = False
    list_minggu = sorted(list(jadwal_terpilih.keys()))
    minggu_terakhir = list_minggu[-1]

    for m, hari in jadwal_terpilih.items():
        if m != minggu_terakhir: # Jangan cek minggu terakhir (Race Day)
            if any("Lomba" in str(v) for v in hari.values()):
                ada_lomba_tuneup = True

    # Render Tabel
    tabel_rapi = []
    for m, h in jadwal_terpilih.items():
        label = f"Minggu {m}" if sisa_waktu >= durasi_ideal else f"H-{minggu_terakhir-m+1} Lomba"
        baris = {"Minggu": label}; baris.update(h); tabel_rapi.append(baris)
    st.table(tabel_rapi)

    if ada_lomba_tuneup:
        st.success("💡 **Info Tune-up Race:** Gunakan lomba di tengah jadwal untuk simulasi mental & fisik.")

    with st.expander("📖 PANDUAN ISTILAH"):
        st.markdown("* **Istirahat:** Vital untuk pemulihan [cite: 35].\n* **Tempo:** Lari buildup untuk ambang batas anaerobik[cite: 77, 80].")