import streamlit as st
import json
import os
from database_jadwal import hal_higdon_db
from fpdf import FPDF # Library PDF yang aman untuk Windows & Cloud

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
jarak_ke_km = {"5K": 5.0, "10K": 10.0, "Half Marathon": 21.1, "Marathon": 42.2}

# --- FUNGSI ZONA PACE ---
def format_waktu(total_detik):
    if total_detik <= 0: return "Sprint"
    m = int(total_detik // 60)
    s = int(total_detik % 60)
    return f"{m}:{s:02d}/km"

def hitung_zona_dari_rp(rp_sec):
    return {
        "RP": format_waktu(rp_sec),
        "Easy": f"{format_waktu(rp_sec + 60)} - {format_waktu(rp_sec + 90)}",
        "Tempo": f"{format_waktu(rp_sec + 10)} - {format_waktu(rp_sec + 20)}",
        "Interval": f"{format_waktu(rp_sec - 15)} - {format_waktu(rp_sec - 5)}",
        "Long": f"{format_waktu(rp_sec + 60)} - {format_waktu(rp_sec + 120)}"
    }

# --- FUNGSI GENERATE PDF (DENGAN GLOSARIUM & CARA BACA) ---
def buat_pdf(data, jadwal_tabel, zona, ada_interval):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    
    # Header Judul
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, f"Rencana Latihan: {data['level']} {data['jarak']}", new_x="LMARGIN", new_y="NEXT", align="C")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 8, f"Disiapkan khusus untuk: {data['nama']}", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)
    
    # Kotak Zona Kecepatan
    pdf.set_font("helvetica", "B", 10)
    pdf.set_fill_color(239, 246, 255)
    pdf.set_text_color(30, 41, 59)
    txt_target = f"Target Finis: {data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}  |  Race Pace Target: {zona['RP']}"
    pdf.cell(0, 8, txt_target, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
    
    pdf.set_font("helvetica", "", 10)
    txt_zona = f"Easy: {zona['Easy']}  |  Tempo: {zona['Tempo']}  |  Interval: {zona['Interval']}  |  Long Run: {zona['Long']}"
    pdf.cell(0, 8, txt_zona, border=1, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)
    
    # Header Tabel
    pdf.set_font("helvetica", "B", 9)
    pdf.set_fill_color(59, 130, 246)
    pdf.set_text_color(255, 255, 255)
    col_w = [22, 35, 35, 35, 35, 35, 35, 35] 
    headers = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    for i in range(8):
        pdf.cell(col_w[i], 8, headers[i], border=1, align="C", fill=True)
    pdf.ln()
    
    # Isi Tabel
    pdf.set_font("helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    for row in jadwal_tabel:
        pdf.cell(col_w[0], 7, str(row.get('Minggu Ke-', '-')), border=1, align="C")
        pdf.cell(col_w[1], 7, str(row.get('Senin', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[2], 7, str(row.get('Selasa', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[3], 7, str(row.get('Rabu', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[4], 7, str(row.get('Kamis', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[5], 7, str(row.get('Jumat', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[6], 7, str(row.get('Sabtu', '-'))[:25], border=1, align="C")
        pdf.cell(col_w[7], 7, str(row.get('Minggu', '-'))[:25], border=1, align="C")
        pdf.ln()

    # --- TAMBAHAN: PANDUAN & GLOSARIUM DI PDF ---
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, "PANDUAN & ISTILAH LATIHAN", new_x="LMARGIN", new_y="NEXT", align="L")
    
    pdf.set_font("helvetica", "", 9)
    if ada_interval:
        pdf.set_font("helvetica", "B", 9)
        pdf.cell(0, 5, "Cara Membaca Interval (Contoh: 4x400m):", new_x="LMARGIN", new_y="NEXT", align="L")
        pdf.set_font("helvetica", "", 8)
        instruksi = ("1. Pemanasan 1-2 km. 2. Lari cepat sesuai jarak instruksi (Pace Interval). "
                     "3. Pemulihan jalan/joging pelan 2-3 menit. 4. Ulangi sesuai jumlah set. 5. Pendinginan 1 km.")
        pdf.multi_cell(0, 5, instruksi)
        pdf.ln(2)

    # Glosarium Terms
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(0, 5, "Glosarium Istilah:", new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.set_font("helvetica", "", 8)
    glosarium_text = (
        "- ISTIRAHAT: Vital untuk pemulihan otot. Tubuh bertambah kuat saat istirahat.\n"
        "- LARI SANTAI (RUN): Fokus pada jarak. Wajib bisa berlari sambil mengobrol (Conversational Pace).\n"
        "- LARI TARGET (PACE): Berlari persis dengan kecepatan Target Race Pace (RP) Anda.\n"
        "- LARI TEMPO: Lari berkelanjutan yang makin cepat untuk melatih ambang batas anaerobik.\n"
        "- LARI JARAK JAUH (LONG RUN): Latihan daya tahan mingguan dengan intensitas santai.\n"
        "- CROSS TRAINING: Olahraga non-lari (sepeda/renang) untuk melatih jantung tanpa beban sendi."
    )
    if not ada_interval:
        glosarium_text += "\n- LARI/JALAN: Kombinasi lari dan jalan untuk pemulihan napas bagi pemula."
    
    pdf.multi_cell(0, 4, glosarium_text)
    
    # Footer
    pdf.set_y(-15)
    pdf.set_font("helvetica", "I", 8)
    pdf.set_text_color(148, 163, 184)
    pdf.cell(0, 10, "Dihasilkan oleh Asisten Lari Cerdas - Metodologi Hal Higdon", align="C")
    
    return bytes(pdf.output())

if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# --- PAGE 1: ONBOARDING ---
if st.session_state.page == 'onboarding':
    st.title("🏃 Selamat Datang di Asisten Lari Cerdas")
    
    st.subheader("📝 Profil & Target")
    col1, col2 = st.columns(2)
    nama = col1.text_input("Nama Lengkap:")
    jarak_target = col2.selectbox("Target jarak lomba?", [k for k in hal_higdon_db.keys() if k != "Base_Training"])
    
    st.markdown("---")
    st.subheader("⏱️ Metode Penentuan Target & Pace")
    metode_target = st.radio(
        "Bagaimana Anda ingin sistem menentukan jadwal Anda?", 
        [
            "1. Mode Pemula (Hanya ingin finis dengan aman & nyaman)", 
            "2. Mode Realistis (Hitung dari Pace Lari Santai/Easy Run saya saat ini)",
            "3. Mode Ambisius (Saya punya target waktu finis impian)"
        ]
    )
    
    jam_finis, menit_finis, detik_finis = 0, 0, 0
    ez_m, ez_s = 0, 0
    
    if "Realistis" in metode_target:
        st.info("💡 Masukkan rata-rata waktu yang Anda butuhkan untuk berlari 1 Km dengan santai (masih bisa sambil ngobrol).")
        c1, c2 = st.columns(2)
        ez_m = c1.number_input("Pace Santai (Menit):", min_value=3, max_value=15, value=7)
        ez_s = c2.number_input("Pace Santai (Detik):", min_value=0, max_value=59, value=30)
    elif "Ambisius" in metode_target:
        st.warning("⚡ Masukkan target waktu finis lomba Anda (Hati-hati risiko overtraining jika tidak realistis).")
        col_j, col_m, col_s = st.columns(3)
        jam_finis = col_j.number_input("Jam:", min_value=0, max_value=10, value=0)
        menit_finis = col_m.number_input("Menit:", min_value=0, max_value=59, value=25)
        detik_finis = col_s.number_input("Detik:", min_value=0, max_value=59, value=0)

    st.markdown("---")
    st.subheader("👟 Tes Kebugaran & Riwayat")
    cedera = st.selectbox("Riwayat cedera 6 bulan terakhir?", ["Tidak ada, sehat 100%", "Ada nyeri ringan", "Ya, pernah cedera berat"])
    frekuensi = st.radio("Berapa kali Anda lari dalam seminggu terakhir?", ["< 1x", "1-2x", "3-4x", "> 4x"])
    speedwork = st.radio("Familiar dengan latihan Interval/Kecepatan?", ["Tidak tahu", "Pernah sesekali", "Ya, Rutin"])
    sisa_waktu = st.slider("Berapa minggu sisa waktu menuju lomba?", 1, 30, 8)
    
    if st.button("Analisis Kemampuan & Hasilkan Jadwal"):
        pesan_peringatan = ""
        level_tersedia = list(hal_higdon_db[jarak_target].keys())
        rp_sec = 999 
        jarak_km = jarak_ke_km[jarak_target]

        if "Realistis" in metode_target:
            ez_sec = (ez_m * 60) + ez_s
            rp_sec = ez_sec - 70 
            total_detik = rp_sec * jarak_km
            jam_finis, menit_finis, detik_finis = int(total_detik // 3600), int((total_detik % 3600) // 60), int(total_detik % 60)
            
        elif "Ambisius" in metode_target:
            total_detik = (jam_finis * 3600) + (menit_finis * 60) + detik_finis
            if total_detik > 0: rp_sec = total_detik / jarak_km

        base_level = level_tersedia[0]
        if rp_sec <= 270: 
            opsi = [k for k in level_tersedia if "Advance" in k or "Advanced" in k]
            base_level = next((k for k in opsi if "2" in k), opsi[-1] if opsi else level_tersedia[-1])
        elif rp_sec <= 360: 
            opsi = [k for k in level_tersedia if "Intermediate" in k]
            base_level = next((k for k in opsi if "1" in k), opsi[0] if opsi else level_tersedia[len(level_tersedia)//2])
        else: 
            opsi = [k for k in level_tersedia if "Novice" in k]
            base_level = next((k for k in opsi if "2" in k), opsi[-1] if opsi else level_tersedia[0])

        level_final = base_level
        pace_asli_str = format_waktu(rp_sec) 
        
        if "cedera" in cedera and "Ya" in cedera:
            pesan_peringatan = "🚨 **INTERVENSI MEDIS:** Sistem mendeteksi riwayat cedera berat. Kami mengabaikan target Anda dan menurunkan intensitas ke program pemulihan."
            opsi = [k for k in level_tersedia if "Novice" in k or "Walker" in k]
            level_final = opsi[0] if opsi else level_tersedia[0]
            if rp_sec < 480: 
                rp_sec = 480
                pesan_peringatan += " Target pace otomatis diturunkan ke zona aman (8:00/km) demi sendi Anda."
                
        elif rp_sec <= 330 and (frekuensi == "< 1x" or frekuensi == "1-2x"):
            pesan_peringatan = f"⚠️ **RISIKO OVERTRAINING:** Target pace Anda ({pace_asli_str}) tergolong sangat cepat, namun frekuensi lari mingguan Anda kurang. Kami menurunkan jadwal ke level yang lebih realistis."
            opsi = [k for k in level_tersedia if "Novice" in k]
            level_final = opsi[-1] if opsi else level_tersedia[0]
            if rp_sec < 420: 
                rp_sec = 420
                pesan_peringatan += " Target pace otomatis disesuaikan ke zona pemula (7:00/km)."
                
        elif rp_sec <= 270 and speedwork in ["Tidak", "Tidak tahu"]:
            pesan_peringatan = f"⚠️ **PENYESUAIAN PROGRAM:** Pace target Anda ({pace_asli_str}) masuk kategori Elite. Karena Anda belum familiar dengan latihan interval, kami menyesuaikan program agar bertahap."
            opsi = [k for k in level_tersedia if "Intermediate" in k]
            level_final = opsi[-1] if opsi else level_tersedia[len(level_tersedia)//2]
            if rp_sec < 330: 
                rp_sec = 330
                pesan_peringatan += " Target pace otomatis disesuaikan ke tingkat menengah (5:30/km)."

        if "Pemula" in metode_target and not pesan_peringatan:
            opsi = [k for k in level_tersedia if "Novice" in k]
            level_final = opsi[0] if opsi else level_tersedia[0]

        total_detik_baru = rp_sec * jarak_km
        jam_finis = int(total_detik_baru // 3600)
        menit_finis = int((total_detik_baru % 3600) // 60)
        detik_finis = int(total_detik_baru % 60)

        user_data = {
            "nama": nama, "jarak": jarak_target, "level": level_final, 
            "sisa_waktu": sisa_waktu, "metode_target": metode_target, 
            "rp_sec": rp_sec, "pesan_peringatan": pesan_peringatan,
            "jam_finis": jam_finis, "menit_finis": menit_finis, "detik_finis": detik_finis
        }
        simpan_data(user_data)
        st.session_state.user_data = user_data
        st.session_state.page = 'jadwal'
        st.rerun()

# --- PAGE 2: HASIL JADWAL ---
elif st.session_state.page == 'jadwal':
    data = st.session_state.user_data
    st.title(f"📊 Program {data['level']} {data['jarak']}")
    
    if data.get('pesan_peringatan'):
        st.error(data['pesan_peringatan'])

    if st.button("⬅️ Kembali & Ganti Target"):
        st.session_state.page = 'onboarding'
        st.rerun()
    
    st.markdown("---")
    st.subheader("🎯 Target & Intensitas Zona Latihan")
    
    zona = hitung_zona_dari_rp(data['rp_sec'])
    
    if "Pemula" in data['metode_target']:
        st.info("💡 **Mode Finish Happy:** Fokus pada perasaan (RPE). Lari Santai (3-4/10) harus bisa sambil ngobrol santai. Jangan hiraukan kecepatan pace!")
    else:
        if "Realistis" in data['metode_target']:
            st.success(f"Berdasarkan Easy Pace Anda, prediksi waktu finis Anda adalah **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** dengan Target Race Pace **{zona['RP']}**.")
        else:
            st.success(f"Target Waktu: **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** | Target Race Pace: **{zona['RP']}**.")
            
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Lari Santai (Easy)", zona['Easy'])
        c2.metric("Lari Jauh (Long)", zona['Long'])
        c3.metric("Lari Tempo", zona['Tempo'])
        c4.metric("Interval/Speed", zona['Interval'])

    st.markdown("---")

    jarak, level, sisa_waktu = data['jarak'], data['level'], data['sisa_waktu']
    durasi_ideal = hal_higdon_db[jarak][level]["durasi_minggu"]
    jadwal_mentah = hal_higdon_db[jarak][level]["jadwal"]
    jadwal_terpilih = {}
    
    base_level = "Novice"
    if "Intermediate" in level: base_level = "Intermediate"
    elif "Advance" in level or "Advanced" in level: base_level = "Advanced"

    if sisa_waktu < durasi_ideal:
        st.warning(f"⚠️ Mode Tapering: Waktu sisa {sisa_waktu} minggu (Idealnya {durasi_ideal} minggu).")
        minggu_mulai = durasi_ideal - sisa_waktu + 1
        for i in range(minggu_mulai, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]
            
    elif sisa_waktu > durasi_ideal:
        selisih = sisa_waktu - durasi_ideal
        st.success(f"🌟 Mode Periodisasi: Sistem menyisipkan {selisih} minggu Base Training di awal.")
        try: jadwal_base = hal_higdon_db["Base_Training"][base_level]["jadwal"]
        except KeyError: jadwal_base = {"1": {"Senin": "Istirahat", "Selasa": "Lari Ringan", "Rabu": "Cross", "Kamis": "Lari Ringan", "Jumat": "Istirahat", "Sabtu": "Lari Ringan", "Minggu": "Long Run"}}
            
        for i in range(1, selisih + 1):
            key_base = str(((i - 1) % 12) + 1)
            if key_base not in jadwal_base: key_base = "1"
            jadwal_terpilih[i] = jadwal_base[key_base]
            
        for i in range(1, durasi_ideal + 1):
            key_inti = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[selisih + i] = jadwal_mentah[key_inti]
            
    else:
        for i in range(1, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]

    ada_lomba_tuneup, ada_interval = False, False
    list_minggu = sorted(list(jadwal_terpilih.keys()))
    minggu_terakhir = list_minggu[-1] if list_minggu else 0
    tabel_rapi = []
    
    for m, h in jadwal_terpilih.items():
        if m != minggu_terakhir and any("Lomba" in str(v) for v in h.values() if isinstance(v, str)): ada_lomba_tuneup = True
        if any(" x " in str(v) or "400" in str(v) or "Interval" in str(v) for v in h.values() if isinstance(v, str)): ada_interval = True

        label = f"Minggu {m}" if sisa_waktu >= durasi_ideal else f"H-{minggu_terakhir-m+1}"
        baris = {"Minggu Ke-": label}; baris.update(h); tabel_rapi.append(baris)
    
    st.table(tabel_rapi)

    # --- TOMBOL DOWNLOAD PDF (DENGAN GLOSARIUM TERSEMAT) ---
    pdf_bytes = buat_pdf(data, tabel_rapi, zona, ada_interval)
    st.download_button(
        label="📥 Download Jadwal & Panduan (PDF)",
        data=pdf_bytes,
        file_name=f"Jadwal_Lari_{data['nama']}.pdf",
        mime="application/pdf"
    )

    if ada_lomba_tuneup:
        st.info("💡 **Info Tune-up Race:** Gunakan 'Lomba' di tengah jadwal untuk simulasi, atau ganti dengan Time Trial mandiri.")

    # GLOSARIUM DINAMIS DI WEB
    st.markdown("---")
    if ada_interval:
        col_a, col_b = st.columns(2)
        with col_a:
            with st.expander("❓ CARA MEMBACA LATIHAN INTERVAL (Contoh: 4x400m)", expanded=True):
                st.markdown("""
                Jika Anda melihat instruksi seperti **"4 x 400 m"** atau **"Interval 6x400"**:
                1. **Pemanasan:** Joging sangat santai 1-2 km untuk memanaskan otot.
                2. **Inti:** Lari cepat sejauh instruksi (Gunakan target 'Interval/Speed' di atas).
                3. **Pemulihan:** Jalan santai atau joging sangat pelan selama 2-3 menit sampai napas kembali tenang.
                4. **Ulangi:** Lakukan fase Lari & Pemulihan sebanyak instruksi angka di depan (misal: 4 kali).
                5. **Pendinginan:** Joging santai 1 km untuk melemaskan otot dan membuang asam laktat.
                """)
        with col_b:
            with st.expander("📖 PANDUAN ISTILAH & FILOSOFI LATIHAN", expanded=True):
                st.markdown("""
                * **Istirahat (Rest):** Sangat vital untuk pemulihan. Otot bertambah kuat saat istirahat, bukan saat berlari.
                * **Lari Santai (Run):** Fokus pada jarak, bukan kecepatan. Anda wajib bisa berlari sambil mengobrol santai.
                * **Lari Cepat (Fast):** Lari dengan intensitas agak berat. Gunakan patokan **Pace Tempo** Anda.
                * **Lari Target (Pace):** Jika jadwal menulis "Pace", larilah persis dengan kecepatan **Target Race Pace (RP)** Anda.
                * **Lari Tempo (Tempo Runs):** Mulai dengan santai, lalu makin cepat di tengah sesi untuk melatih ambang batas anaerobik.
                * **Lari Jarak Jauh (Long Runs):** Latihan daya tahan mingguan. Lakukan dengan intensitas paling santai.
                * **Cross Training:** Olahraga non-lari (sepeda/renang) untuk melatih jantung.
                """)
    else:
        with st.expander("📖 PANDUAN ISTILAH & FILOSOFI LATIHAN", expanded=True):
            st.markdown("""
            * **Istirahat (Rest):** Sangat vital untuk pemulihan. Otot bertambah kuat saat istirahat, bukan saat berlari.
            * **Lari Santai (Run):** Fokus pada menyelesaikan jarak, bukan kecepatan. Anda wajib bisa berlari sambil mengobrol santai.
            * **Lari Jarak Jauh (Long Runs):** Latihan daya tahan mingguan. Lakukan dengan intensitas paling santai.
            * **Lari/Jalan (Run/Walk):** Anda tidak harus berlari terus-menerus. Larilah sampai lelah, lalu berjalan untuk memulihkan napas.
            * **Cross Training:** Olahraga non-lari (sepeda/renang) untuk melatih jantung.
            """)