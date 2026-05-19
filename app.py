import streamlit as st
import json
import os
import datetime
from database_jadwal import hal_higdon_db
from fpdf import FPDF # Library PDF yang aman untuk Windows & Cloud

# --- CONFIGURATION ---
# --- CONFIGURATION ---
st.set_page_config(page_title="Asisten Lari Cerdas", layout="wide", page_icon="🏃")

# --- CUSTOM CSS UI (TAMBAHKAN BLOK INI) ---
# --- CUSTOM CSS UI ---
st.markdown("""
<style>
    /* Mengimpor font Poppins yang modern */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Menerapkan font ke seluruh aplikasi */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    /* Latar Belakang Aplikasi: Gradasi halus biru keabu-abuan layaknya aplikasi fitness premium */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4ecf7 100%);
    }

    /* Mempercantik Kotak Metrik (Zona Pace) agar terlihat seperti widget */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 15px 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 6px solid #3b82f6; /* Garis aksen biru sport */
        transition: transform 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: scale(1.02);
    }

    /* --- MEMPERKECIL UKURAN ANGKA PACE AGAR TIDAK TERPOTONG --- */
    div[data-testid="stMetricValue"] {
        font-size: 1.4rem !important; 
        color: #1e293b !important;
    }
    /* Mempertegas label judul metriknya */
    div[data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
    }

    /* Mempercantik Tombol Utama (Bentuk Pill, Efek Hover 3D) */
    .stButton>button {
        background: linear-gradient(to right, #2563eb, #3b82f6);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.4);
        background: linear-gradient(to right, #1d4ed8, #2563eb);
    }

    /* Mempercantik Tampilan Tabel */
    div[data-testid="stTable"] {
        background-color: white;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    
    /* Expander (Menu Glosarium) yang lebih elegan */
    .streamlit-expanderHeader {
        font-weight: 600;
        background-color: white;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
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

# --- CLASS KUSTOM UNTUK PDF (MENCEGAH HALAMAN KOSONG) ---
class PDFLatihan(FPDF):
    def footer(self):
        # Posisi mengunci 15 mm dari bawah kertas
        self.set_y(-15)
        self.set_font("helvetica", "I", 7)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, "Dihasilkan oleh Asisten Lari Cerdas - Metodologi Hal Higdon", align="C")

# --- FUNGSI GENERATE PDF (A4 PORTRAIT) ---
def buat_pdf(data, jadwal_tabel, zona, ada_interval):
    # Menggunakan class PDFLatihan yang memiliki auto-footer
    pdf = PDFLatihan(orientation="P", unit="mm", format="A4")
    # Mengaktifkan batas bawah otomatis agar konten tidak menabrak footer
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(10, 15, 10)
    pdf.add_page()
    
    # Header Judul
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 8, f"Rencana Latihan: {data['level']} {data['jarak']}", new_x="LMARGIN", new_y="NEXT", align="C")
    
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 6, f"Disiapkan khusus untuk: {data['nama']}", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)
    
    # Kotak Zona Kecepatan
    pdf.set_font("helvetica", "B", 9)
    pdf.set_fill_color(239, 246, 255)
    pdf.set_text_color(30, 41, 59)
    txt_target = f"Target Finis: {data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}  |  Race Pace: {zona['RP']}"
    pdf.cell(0, 7, txt_target, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
    
    pdf.set_font("helvetica", "", 8)
    txt_zona = f"Easy: {zona['Easy']} | Tempo: {zona['Tempo']} | Interval: {zona['Interval']} | Long: {zona['Long']}"
    pdf.cell(0, 7, txt_zona, border=1, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(6)
    
    # Header Tabel
    pdf.set_font("helvetica", "B", 8)
    pdf.set_fill_color(59, 130, 246)
    pdf.set_text_color(255, 255, 255)
    
    col_w = [14, 25, 25, 25, 25, 25, 25, 25] 
    headers = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    for i in range(8):
        pdf.cell(col_w[i], 7, headers[i], border=1, align="C", fill=True)
    pdf.ln()
    
    # Isi Tabel
    pdf.set_font("helvetica", "", 7.5) 
    pdf.set_text_color(30, 41, 59)
    for row in jadwal_tabel:
        minggu_label = str(row.get('Minggu Ke-', '-')).replace("Minggu ", "M-")
        pdf.cell(col_w[0], 6, minggu_label, border=1, align="C")
        
        pdf.cell(col_w[1], 6, str(row.get('Senin', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[2], 6, str(row.get('Selasa', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[3], 6, str(row.get('Rabu', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[4], 6, str(row.get('Kamis', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[5], 6, str(row.get('Jumat', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[6], 6, str(row.get('Sabtu', '-'))[:20], border=1, align="C")
        pdf.cell(col_w[7], 6, str(row.get('Minggu', '-'))[:20], border=1, align="C")
        pdf.ln()

    # --- PANDUAN & GLOSARIUM DI PDF ---
    pdf.ln(4)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 6, "PANDUAN & ISTILAH LATIHAN", new_x="LMARGIN", new_y="NEXT", align="L")
    
    pdf.set_font("helvetica", "", 8)
    if ada_interval:
        pdf.set_font("helvetica", "B", 8)
        pdf.cell(0, 4, "Cara Membaca Interval (Contoh: 4x400m):", new_x="LMARGIN", new_y="NEXT", align="L")
        pdf.set_font("helvetica", "", 7.5)
        instruksi = ("1. Pemanasan 1-2 km. 2. Lari cepat sejauh instruksi (Gunakan Pace Interval). "
                     "3. Pemulihan jalan/joging pelan 2-3 menit. 4. Ulangi sesuai jumlah set. 5. Pendinginan 1 km.")
        pdf.multi_cell(0, 4, instruksi)
        pdf.ln(1)

    pdf.set_font("helvetica", "B", 8)
    pdf.cell(0, 4, "Glosarium Istilah:", new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.set_font("helvetica", "", 7.5)
    glosarium_text = (
        "- ISTIRAHAT: Vital untuk pemulihan otot. Tubuh bertambah kuat saat istirahat.\n"
        "- LARI SANTAI: Fokus pada jarak. Wajib bisa berlari sambil mengobrol (Conversational Pace).\n"
        "- LARI TARGET: Berlari persis dengan kecepatan Target Race Pace (RP) Anda.\n"
        "- LARI TEMPO: Lari berkelanjutan yang makin cepat untuk melatih ambang batas anaerobik.\n"
        "- LARI JARAK JAUH: Latihan daya tahan mingguan dengan intensitas santai.\n"
        "- CROSS TRAINING: Olahraga non-lari (sepeda/renang) untuk melatih jantung tanpa beban sendi."
    )
    if not ada_interval:
        glosarium_text += "\n- LARI/JALAN: Kombinasi lari dan jalan untuk pemulihan napas."
    
    pdf.multi_cell(0, 4, glosarium_text)
    
    # Perhatikan: Bagian Footer manual "pdf.set_y(-15)..." sudah dihapus dari sini!
    
    return bytes(pdf.output())

if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# --- PAGE 1: ONBOARDING ---
if st.session_state.page == 'onboarding':
    st.title("🏃 Selamat Datang di Asisten Lari Cerdas")
    
    st.subheader("📝 Profil & Target")
    col1, col2 = st.columns(2)
    nama = col1.text_input("Nama Lengkap:")
    # Pastikan jarak_target tidak memasukkan 'Base_Training' sebagai opsi jarak
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
        st.info("💡 Masukkan rata-rata waktu yang Anda butuhkan untuk berlari 1 Km dengan santai.")
        c1, c2 = st.columns(2)
        ez_m = c1.number_input("Pace Santai (Menit):", min_value=3, max_value=15, value=7)
        ez_s = c2.number_input("Pace Santai (Detik):", min_value=0, max_value=59, value=30)
        
        # --- Prediksi Real-Time Langsung di Layar ---
        jarak_km = jarak_ke_km[jarak_target]
        ez_sec_sementara = (ez_m * 60) + ez_s
        rp_sec_sementara = ez_sec_sementara - 70 # Rumus: Race Pace = Easy Pace - 70 detik
        
        if rp_sec_sementara > 0:
            total_detik_sementara = rp_sec_sementara * jarak_km
            jam_pred = int(total_detik_sementara // 3600)
            menit_pred = int((total_detik_sementara % 3600) // 60)
            detik_pred = int(total_detik_sementara % 60)
            pace_pred_m = int(rp_sec_sementara // 60)
            pace_pred_s = int(rp_sec_sementara % 60)
            
            st.success(f"⏱️ **Prediksi Cerdas:** Jika Pace Santai Anda **{ez_m}:{ez_s:02d}/km**, maka target Race Pace lomba Anda adalah **{pace_pred_m}:{pace_pred_s:02d}/km**. \n\n🏁 Estimasi finis {jarak_target}: **{jam_pred} Jam {menit_pred} Menit {detik_pred} Detik**.")

    elif "Ambisius" in metode_target:
        st.warning("⚡ Masukkan target waktu finis lomba Anda.")
        col_j, col_m, col_s = st.columns(3)
        jam_finis = col_j.number_input("Jam:", min_value=0, max_value=10, value=0)
        menit_finis = col_m.number_input("Menit:", min_value=0, max_value=59, value=25)
        detik_finis = col_s.number_input("Detik:", min_value=0, max_value=59, value=0)

    st.markdown("---")
    st.subheader("🗓️ Riwayat Medis & Kalender Lomba")
    cedera = st.selectbox("Riwayat cedera 6 bulan terakhir?", ["Tidak ada, sehat 100%", "Ada nyeri ringan", "Ya, pernah cedera berat"])
    frekuensi = st.radio("Berapa kali Anda lari dalam seminggu terakhir?", ["< 1x", "1-2x", "3-4x", "> 4x"])
    speedwork = st.radio("Familiar dengan latihan Interval/Kecepatan?", ["Tidak tahu", "Pernah sesekali", "Ya, Rutin"])
    
    # --- LOGIKA KALENDER REAL-TIME & PERENCANAAN ---
    hari_ini = datetime.date.today()
    
    st.write("📅 **Pengaturan Waktu Program**")
    col_lomba, col_mulai = st.columns(2)
    
    # 1. Pilih Hari Lomba (DI KIRI)
    default_lomba = hari_ini + datetime.timedelta(days=56) 
    tanggal_lomba = col_lomba.date_input(
        "Pilih Tanggal Hari H Lomba Anda:", 
        value=default_lomba, 
        min_value=hari_ini + datetime.timedelta(days=7)
    )
    
    # 2. Pilih Mulai Latihan (DI KANAN)
    tanggal_mulai = col_mulai.date_input(
        "Kapan Anda mulai berlatih?", 
        value=hari_ini, 
        min_value=hari_ini,
        max_value=tanggal_lomba - datetime.timedelta(days=1)
    )
    
    # Perhitungan blok minggu (berbasis kalender penuh)
    sisa_hari = (tanggal_lomba - tanggal_mulai).days
    sisa_waktu = max(1, (sisa_hari // 7) + 1)
    
    st.info(f"⏱️ Sistem mendeteksi durasi persiapan efektif Anda adalah **{sisa_waktu} minggu** terhitung dari tanggal mulai latihan.")

    # --- TOMBOL PROSES & ALGORITMA PENILAIAN ---
    if st.button("Analisis Kemampuan & Hasilkan Jadwal"):
        pesan_peringatan = ""
        level_tersedia = list(hal_higdon_db[jarak_target].keys())
        rp_sec = 999 
        jarak_km = jarak_ke_km[jarak_target]

        # 1. Konversi Target ke Detik
        if "Realistis" in metode_target:
            ez_sec = (ez_m * 60) + ez_s
            rp_sec = ez_sec - 70 
            total_detik = rp_sec * jarak_km
            jam_finis, menit_finis, detik_finis = int(total_detik // 3600), int((total_detik % 3600) // 60), int(total_detik % 60)
        elif "Ambisius" in metode_target:
            total_detik = (jam_finis * 3600) + (menit_finis * 60) + detik_finis
            if total_detik > 0: rp_sec = total_detik / jarak_km

        # 2. Hipotesis Awal Level Jadwal
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

        pace_asli_str = format_waktu(rp_sec) 
        level_final = base_level 
        
        # 3. Validasi Batas Bawah Sisa Minggu
        batas_bawah_db = {"5K": 3, "10K": 4, "Half Marathon": 8, "Marathon": 12}
        batas_bawah = batas_bawah_db[jarak_target]
        
        if sisa_waktu < batas_bawah:
            pesan_peringatan += f"🚨 **WAKTU KRITIS:** Persiapan aman minimal untuk {jarak_target} adalah {batas_bawah} minggu. Memaksakan lomba dalam {sisa_waktu} minggu sangat berisiko cedera. Jadwal di bawah ini murni fase *Survival/Tapering*.\n\n"

        # 4. Deteksi Risiko & Rekomendasi Medis (Dual-Track)
        resiko_ditemukan = False
        rp_sec_aman = rp_sec
        level_aman = base_level

        if "cedera" in cedera and "Ya" in cedera:
            pesan_peringatan += "⚠️ **RESIKO MEDIS:** Sistem mendeteksi riwayat cedera berat. Tubuh Anda butuh pemulihan, bukan mengejar Personal Record. "
            resiko_ditemukan = True
            opsi_aman = [k for k in level_tersedia if "Novice" in k or "Walker" in k]
            level_aman = opsi_aman[0] if opsi_aman else level_tersedia[0]
            if rp_sec_aman < 480: rp_sec_aman = 480
                
        elif rp_sec <= 330 and (frekuensi == "< 1x" or frekuensi == "1-2x"):
            pesan_peringatan += f"⚠️ **RESIKO OVERTRAINING:** Target pace Anda ({pace_asli_str}) sangat ambisius, namun frekuensi latihan Anda minim. Berpotensi merobek otot. "
            resiko_ditemukan = True
            opsi_aman = [k for k in level_tersedia if "Novice" in k]
            level_aman = opsi_aman[-1] if opsi_aman else level_tersedia[0]
            if rp_sec_aman < 420: rp_sec_aman = 420
                
        elif rp_sec <= 270 and speedwork in ["Tidak", "Tidak tahu"]:
            pesan_peringatan += f"⚠️ **RESIKO TEKNIS:** Pace Elite ({pace_asli_str}) butuh adaptasi otot untuk lari interval yang belum Anda miliki. "
            resiko_ditemukan = True
            opsi_aman = [k for k in level_tersedia if "Intermediate" in k]
            level_aman = opsi_aman[-1] if opsi_aman else level_tersedia[len(level_tersedia)//2]
            if rp_sec_aman < 330: rp_sec_aman = 330

        if resiko_ditemukan:
            total_detik_aman = rp_sec_aman * jarak_km
            jam_aman = int(total_detik_aman // 3600)
            menit_aman = int((total_detik_aman % 3600) // 60)
            
            pesan_peringatan += f"\n\n🛡️ **REKOMENDASI AMAN SISTEM:** Demi keselamatan sendi, kami sangat merekomendasikan Anda turun ke **Program {level_aman}** dengan Target Pace **{format_waktu(rp_sec_aman)}** (Prediksi Finis {jam_aman}j {menit_aman}m)."
            pesan_peringatan += f"\n\n💡 **DISCLAIMER:** Menghargai komitmen Anda, sistem tetap merender jadwal level tinggi di bawah ini sesuai ambisi awal Anda (Program {level_final}). Lakukan dengan kewaspadaan penuh!"

        if "Pemula" in metode_target and not pesan_peringatan:
            opsi = [k for k in level_tersedia if "Novice" in k]
            level_final = opsi[0] if opsi else level_tersedia[0]

        total_detik_baru = rp_sec * jarak_km
        jam_finis = int(total_detik_baru // 3600)
        menit_finis = int((total_detik_baru % 3600) // 60)
        detik_finis = int(total_detik_baru % 60)

        # 5. Penyimpanan ke Session State untuk Halaman 2
        user_data = {
            "nama": nama, "jarak": jarak_target, "level": level_final, 
            "sisa_waktu": sisa_waktu, "metode_target": metode_target, 
            "rp_sec": rp_sec, "pesan_peringatan": pesan_peringatan,
            "jam_finis": jam_finis, "menit_finis": menit_finis, "detik_finis": detik_finis,
            "tanggal_lomba": tanggal_lomba.strftime("%Y-%m-%d"),
            "tanggal_mulai": tanggal_mulai.strftime("%Y-%m-%d"),
            "resiko_ditemukan": resiko_ditemukan,
            "level_aman": level_aman,
            "rp_sec_aman": rp_sec_aman
        }
        
        try:
            simpan_data(user_data) # Berjalan jika kamu masih pakai JSON logger
        except NameError:
            pass # Mengamankan jika fungsi simpan_data tidak ada
            
        st.session_state.user_data = user_data
        st.session_state.page = 'jadwal'
        st.rerun()

# --- PAGE 2: HASIL JADWAL ---
elif st.session_state.page == 'jadwal':
    data = st.session_state.user_data
    st.title(f"📊 Analisis Program Latihan: {data['nama']}")
    
    # Menampilkan Peringatan Kritis dari Halaman 1 (Jika Ada)
    if data.get('pesan_peringatan'):
        st.warning(data['pesan_peringatan'])

    if st.button("⬅️ Kembali & Ganti Target"):
        st.session_state.page = 'onboarding'
        st.rerun()
    
    st.markdown("---")

    # --- FUNGSI BANTUAN 1: RENDER METRIK ZONA ---
    def render_metrik_zona(rp_sec_target):
        zona = hitung_zona_dari_rp(rp_sec_target)
        lr_cepat_sec = rp_sec_target + 20
        lr_lambat_sec = rp_sec_target + 60
        zona['Long_Aman'] = f"{format_waktu(lr_cepat_sec)} - {format_waktu(lr_lambat_sec)}"
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Lari Santai (Easy)", zona['Easy'])
        c2.metric("Lari Jauh (Long)", zona['Long_Aman'])
        c3.metric("Lari Tempo", zona['Tempo'])
        c4.metric("Interval/Speed", zona['Interval'])
        return zona

    # --- FUNGSI BANTUAN 2: GENERATOR TABEL ---
    def generate_full_table(target_level, target_rp_sec):
        jarak = data['jarak']
        sisa_waktu = data['sisa_waktu']
        durasi_ideal = hal_higdon_db[jarak][target_level]["durasi_minggu"]
        jadwal_mentah = hal_higdon_db[jarak][target_level]["jadwal"]
        jadwal_terpilih = {}
        
        base_level = "Novice"
        if "Intermediate" in target_level: base_level = "Intermediate"
        elif "Advance" in target_level or "Advanced" in target_level: base_level = "Advanced"

        # --- MENGEMBALIKAN PERINGATAN WAKTU IDEAL VS AKTUAL ---
        if sisa_waktu < durasi_ideal:
            st.warning(f"⚠️ **Penyesuaian Jadwal:** Sisa waktu Anda {sisa_waktu} minggu (Idealnya {durasi_ideal} minggu untuk program ini). Sistem memotong fase awal secara cerdas dan langsung fokus pada menu inti.")
            minggu_mulai = durasi_ideal - sisa_waktu + 1
            for i in range(minggu_mulai, durasi_ideal + 1):
                key = str(i) if str(i) in jadwal_mentah else i
                jadwal_terpilih[i] = jadwal_mentah[key]
        elif sisa_waktu > durasi_ideal:
            selisih = sisa_waktu - durasi_ideal
            st.success(f"🌟 **Fase Periodisasi:** Sisa waktu Anda sangat panjang ({sisa_waktu} minggu). Sistem menyisipkan {selisih} minggu *Base Training* di awal untuk membangun stamina Anda perlahan-lahan.")
            try: jadwal_base = hal_higdon_db["Base_Training"][base_level]["jadwal"]
            except KeyError: jadwal_base = {"1": {"Senin": "Istirahat", "Selasa": "Lari", "Rabu": "Cross", "Kamis": "Lari", "Jumat": "Istirahat", "Sabtu": "Lari", "Minggu": "Long Run"}}
            for i in range(1, selisih + 1):
                key_base = str(((i - 1) % 12) + 1)
                jadwal_terpilih[i] = jadwal_base.get(key_base, jadwal_base["1"])
            for i in range(1, durasi_ideal + 1):
                key_inti = str(i) if str(i) in jadwal_mentah else i
                jadwal_terpilih[selisih + i] = jadwal_mentah[key_inti]
        else:
            for i in range(1, durasi_ideal + 1):
                key = str(i) if str(i) in jadwal_mentah else i
                jadwal_terpilih[i] = jadwal_mentah[key]

        list_minggu = sorted(list(jadwal_terpilih.keys()))
        minggu_terakhir = list_minggu[-1] if list_minggu else 0
        tabel_ui, tabel_pdf = [], []
        
        tanggal_lomba = datetime.datetime.strptime(data['tanggal_lomba'], "%Y-%m-%d").date()
        tanggal_mulai = datetime.datetime.strptime(data['tanggal_mulai'], "%Y-%m-%d").date()
        target_weekday = tanggal_lomba.weekday() 
        nama_hari_standar = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        kolom_hari_dinamis = [nama_hari_standar[(target_weekday + 1 + i) % 7] for i in range(7)]
            
        for m, h in jadwal_terpilih.items():
            tgl_akhir = tanggal_lomba - datetime.timedelta(days=(minggu_terakhir - m) * 7)
            tgl_awal = tgl_akhir - datetime.timedelta(days=6)
            is_taper = m == minggu_terakhir or (jarak == "Marathon" and m >= minggu_terakhir - 2)
            
            label_ui = f"M-{m}\n{tgl_awal.strftime('%d %b')} - {tgl_akhir.strftime('%d %b')}" + ("\n📉 Tapering" if is_taper else "")
            label_pdf = f"M-{m} | {tgl_awal.strftime('%d %b')} - {tgl_akhir.strftime('%d %b')}" + (" (Tapering)" if is_taper else "")
            
            baris_ui, baris_pdf = {"Minggu Ke-": label_ui}, {"Minggu Ke-": label_pdf}
            for idx, hari_kolom in enumerate(kolom_hari_dinamis):
                tgl_skrg = tgl_awal + datetime.timedelta(days=idx)
                if tgl_skrg < tanggal_mulai: teks_ui, teks_pdf = "➖ Blm Mulai", "- Belum Mulai"
                elif tgl_skrg > tanggal_lomba: teks_ui, teks_pdf = "🏁 Selesai", "- Selesai"
                elif tgl_skrg == tanggal_lomba: teks_ui, teks_pdf = f"🎯 RACE DAY!\nLomba {jarak}", f"RACE DAY! Lomba {jarak}"
                else:
                    menu = str(h.get(nama_hari_standar[idx], '-'))
                    teks_ui = f"🛌 {menu}" if "Istirahat" in menu else f"🏃 {menu}" if any(x in menu.lower() for x in ["km", "mil", "pace"]) or idx == 6 else menu
                    teks_pdf = menu
                baris_ui[hari_kolom], baris_pdf[hari_kolom] = teks_ui, teks_pdf
            tabel_ui.append(baris_ui); tabel_pdf.append(baris_pdf)
            
        return tabel_ui, tabel_pdf

    # --- EKSEKUSI RENDER TABEL & METRIK (DUAL-TRACK) ---
    if data.get("resiko_ditemukan"):
        st.info("⚠️ **Mode Penyesuaian:** Sistem memproses dua opsi jadwal untuk Anda evaluasi.")
        st.markdown("### 🛡️ Opsi 1: Jadwal Rekomendasi Aman (Disarankan)")
        st.success(f"🏁 Prediksi Finis Aman: {data['level_aman']} | 🎯 Race Pace: {format_waktu(data['rp_sec_aman'])}/km")
        zona_aman = render_metrik_zona(data['rp_sec_aman'])
        tb_ui_aman, tb_pdf_aman = generate_full_table(data['level_aman'], data['rp_sec_aman'])
        st.table(tb_ui_aman)
        
        st.markdown("---")
        st.markdown("### 🎯 Opsi 2: Jadwal Sesuai Target Anda (Risiko Tinggi)")
        st.error(f"🏁 Target Ambisius: {data['level']} | 🎯 Race Pace: {format_waktu(data['rp_sec'])}/km")
        zona_ambisi = render_metrik_zona(data['rp_sec'])
        tb_ui_ambisi, tb_pdf_ambisi = generate_full_table(data['level'], data['rp_sec'])
        st.table(tb_ui_ambisi)
        tabel_rapi_pdf, zona_pdf = tb_pdf_ambisi, zona_ambisi
    else:
        st.markdown("### 🎯 Target & Intensitas Zona Latihan")
        if "Pemula" in data['metode_target']:
            st.info("💡 **Mode Finish Happy:** Fokus pada perasaan (RPE). Lari Santai (3-4/10) harus bisa sambil ngobrol santai. Jangan hiraukan kecepatan pace!")
        elif "Realistis" in data['metode_target']:
            st.success(f"🏁 Prediksi Waktu Finis: **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** | 🎯 Target Race Pace: **{format_waktu(data['rp_sec'])}/km**")
        else:
            st.success(f"🏁 Target Waktu Finis: **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** | 🎯 Target Race Pace: **{format_waktu(data['rp_sec'])}/km**")
            
        zona_normal = render_metrik_zona(data['rp_sec'])
        tb_ui_normal, tb_pdf_normal = generate_full_table(data['level'], data['rp_sec'])
        st.table(tb_ui_normal)
        tabel_rapi_pdf, zona_pdf = tb_pdf_normal, zona_normal

    # --- TOMBOL DOWNLOAD & PUSAT EDUKASI ---
    pdf_bytes = buat_pdf(data, tabel_rapi_pdf, zona_pdf, True)
    st.download_button(label="📥 Download Jadwal Latihan (PDF)", data=pdf_bytes, file_name=f"Jadwal_{data['nama']}.pdf", mime="application/pdf")

    st.markdown("---")
    st.subheader("🎓 Pusat Edukasi: Memahami Jadwal Anda") 
    with st.expander("Buka Kamus Lari & Aturan Emas", expanded=False):
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📉 Tapering", "🏃 Long Run", "🔄 Stepback", "🚴 Cross-Training", "⏱️ Lari Tempo", "⚡ Interval"
        ])
        
        with tab1:
            st.markdown("""
            ### Apa itu Tapering?
            **Tapering** adalah fase pengurangan beban latihan (jarak lari) yang dilakukan secara sengaja menjelang hari H lomba.
            * **Tujuannya apa?** Mengisi kembali tangki energi otot yang terkuras selama latihan berbulan-bulan. 
            * **Kenapa jaraknya malah turun?** Kalau Anda tetap memaksakan latihan berat sampai H-1, otot akan kelelahan (fatigue) saat lomba. Tapering ibarat menabung energi agar Anda bisa "meledak" saat Race Day.
            * **Durasi:** Maraton butuh 3 minggu tapering, sedangkan Half Marathon/10K butuh 1-2 minggu.
            """)
            
        with tab2:
            st.markdown("""
            ### Lari Jauh (Long Run) & Batas Kecepatan
            **Long Run** adalah menu paling penting dalam seminggu (biasanya di akhir pekan) untuk membangun stamina paru-paru dan kaki.
            * **Aturan Emas:** Anda **WAJIB** berlari lebih lambat dari target kecepatan (Pace) lomba Anda.
            * **Kenapa harus lambat?** Tujuannya adalah durasi, bukan kecepatan. Lari terlalu cepat saat Long Run akan merobek otot terlalu parah, sehingga Anda gagal latihan di minggu berikutnya karena cedera/pegal.
            """)
            
        with tab3:
            st.markdown("""
            ### Minggu Istirahat (Stepback / Recovery Week)
            Apakah Anda sadar jarak lari Anda tidak selalu naik setiap minggu? Terkadang di minggu ke-3, jaraknya malah turun. Ini disebut **Stepback**.
            * **Fungsinya:** Tubuh manusia tidak bisa disiksa terus-menerus. Minggu Stepback memberikan jeda bagi sendi dan tulang untuk beradaptasi dan menyerap hasil latihan yang sudah dilakukan. 
            """)
            
        with tab4:
            st.markdown("""
            ### Olahraga Pengganti (Cross-Training)
            Jadwal menyuruh Anda melakukan **Cross-Training** (Cross) selama 30-60 menit. Ini berarti Anda harus melakukan olahraga aerobik SELAIN berlari.
            * **Boleh:** Bersepeda, Berenang, atau Jalan Cepat. (Ini melatih kardio tanpa membenturkan kaki ke aspal).
            * **DILARANG KERAS:** Futsal, Basket, Bulutangkis, atau Tenis.
            * **Kenapa dilarang?** Olahraga dengan gerakan menyamping mendadak dan melompat memiliki risiko sangat tinggi membuat lutut/engkel Anda keseleo.
            """)
            
        with tab5:
            st.markdown("""
            ### Apa itu Lari Tempo?
            Lari Tempo **BUKAN** lari cepat dari awal sampai akhir. Lari Tempo melatih tubuh Anda bertahan di batas kelelahan.
            * **Cara Melakukannya (3 Fase):**
                1. Mulai dengan 15 menit joging super pelan (Pemanasan).
                2. Akselerasi perlahan sampai ke *Race Pace* Anda, dan tahan selama 5-15 menit di tengah-tengah (Inti).
                3. Tutup dengan 10 menit joging pelan (Pendinginan).
            """)
            
        with tab6:
            st.markdown("""
            ### Latihan Kecepatan (Interval)
            Jika Anda melihat instruksi **"4 x 400 m"**, ini adalah latihan interval untuk mencetak kecepatan maksimal di lintasan lari.
            * **Cara Melakukannya:**
                1. Pemanasan joging 1-2 km.
                2. Lari secepat mungkin sejauh 400 meter (1 keliling lapangan).
                3. Berhenti dan jalan santai selama 2 menit (Pemulihan).
                4. Ulangi lari cepat & jalan santai tersebut sebanyak 4 set.
                5. Tutup dengan joging pelan 1 km.
            """)