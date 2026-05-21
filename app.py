import streamlit as st
import json
import os
import datetime
from database_jadwal import hal_higdon_db
from fpdf import FPDF

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="RunSmart – Asisten Lari Cerdas",
    layout="wide",
    page_icon="🏃",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────
# PREMIUM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --bg-dark:     #0a0e1a;
    --bg-card:     #111827;
    --bg-card2:    #1a2236;
    --accent:      #f97316;
    --accent2:     #fb923c;
    --accent-glow: rgba(249,115,22,0.25);
    --blue:        #3b82f6;
    --blue-glow:   rgba(59,130,246,0.2);
    --green:       #10b981;
    --red:         #ef4444;
    --text-1:      #f1f5f9;
    --text-2:      #94a3b8;
    --text-3:      #475569;
    --border:      rgba(255,255,255,0.07);
    --radius:      16px;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text-1);
}

.stApp {
    background: var(--bg-dark);
    background-image:
        radial-gradient(ellipse 80% 50% at 20% 20%, rgba(249,115,22,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 60% at 80% 80%, rgba(59,130,246,0.10) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 50% 50%, rgba(16,185,129,0.05) 0%, transparent 70%);
    min-height: 100vh;
}

h1 {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 3.5rem !important;
    letter-spacing: 3px !important;
    background: linear-gradient(135deg, #f97316, #fb923c, #fbbf24) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin-bottom: 0 !important;
    line-height: 1.1 !important;
}

h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: var(--text-1) !important; }
h2 { font-size: 1.6rem !important; font-weight: 600 !important; }
h3 { font-size: 1.2rem !important; font-weight: 500 !important; }

.stApp [data-testid="stMarkdownContainer"] h3 {
    border-left: 3px solid var(--accent);
    padding-left: 12px;
    margin-top: 2rem !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="select"] div,
div[data-baseweb="textarea"] textarea {
    background: var(--bg-card2) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: var(--text-1) !important;
    font-family: 'DM Sans', sans-serif !important;
}

label, .stRadio label, .stCheckbox label {
    color: var(--text-2) !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}

.stRadio div[role="radiogroup"] label {
    background: var(--bg-card2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    margin: 4px 0 !important;
    transition: all 0.2s !important;
    color: var(--text-2) !important;
}
.stRadio div[role="radiogroup"] label:hover {
    border-color: var(--accent) !important;
    color: var(--text-1) !important;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, var(--bg-card), var(--bg-card2)) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 18px 20px !important;
    position: relative;
    overflow: hidden;
}
div[data-testid="stMetric"]::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--blue));
}
div[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    color: var(--accent) !important;
}
div[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    color: var(--text-2) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

.stButton > button {
    background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
    color: #0a0e1a !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px 32px !important;
    box-shadow: 0 4px 20px var(--accent-glow) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 30px rgba(249,115,22,0.45) !important;
}

.stDownloadButton > button {
    background: linear-gradient(135deg, var(--green), #059669) !important;
    color: white !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 12px 28px !important;
    box-shadow: 0 4px 15px rgba(16,185,129,0.3) !important;
    transition: all 0.3s !important;
}
.stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(16,185,129,0.5) !important;
}

div[data-testid="stAlert"] { border-radius: 12px !important; border: none !important; }

div[data-testid="stTable"] {
    background: var(--bg-card) !important;
    border-radius: 14px !important;
    border: 1px solid var(--border) !important;
    overflow: hidden;
}
div[data-testid="stTable"] table { color: var(--text-1) !important; }
div[data-testid="stTable"] thead th {
    background: linear-gradient(135deg, var(--accent), #ea580c) !important;
    color: white !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    padding: 12px 10px !important;
}
div[data-testid="stTable"] tbody tr:nth-child(even) td {
    background: rgba(255,255,255,0.03) !important;
}
div[data-testid="stTable"] tbody tr:hover td {
    background: rgba(249,115,22,0.06) !important;
}
div[data-testid="stTable"] tbody td {
    color: var(--text-2) !important;
    font-size: 0.8rem !important;
    padding: 9px 10px !important;
    border-color: var(--border) !important;
}

.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-1) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
}
.streamlit-expanderContent {
    background: var(--bg-card2) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-2) !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 8px 14px !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
    color: #0a0e1a !important;
    font-weight: 700 !important;
}

hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 28px 0 !important; }
p, li { color: var(--text-2) !important; line-height: 1.7 !important; }

.stat-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(249,115,22,0.12);
    border: 1px solid rgba(249,115,22,0.3);
    border-radius: 50px;
    padding: 6px 16px;
    font-size: 0.85rem;
    font-weight: 600;
    color: #fdba74;
    margin-right: 8px;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    color: var(--text-2);
    margin-top: 4px;
    margin-bottom: 24px;
    font-style: italic;
}

.duration-display {
    background: linear-gradient(135deg, rgba(249,115,22,0.15), rgba(251,146,60,0.08));
    border: 1px solid rgba(249,115,22,0.3);
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: var(--text-3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

#MainMenu, footer, header { visibility: hidden; }

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.stApp > div { animation: fadeUp 0.5s ease both; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# CONSTANTS & HELPERS
# ─────────────────────────────────────────
DB_FILE = "database_user.json"
jarak_ke_km = {"5K": 5.0, "10K": 10.0, "Half Marathon": 21.1, "Marathon": 42.2}
NAMA_HARI_STANDAR = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

def simpan_data(data):
    db = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                db = json.load(f)
            except Exception:
                db = []
    db.append(data)
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def format_waktu(total_detik):
    if total_detik <= 0:
        return "Sprint"
    m = int(total_detik // 60)
    s = int(total_detik % 60)
    return f"{m}:{s:02d}/km"

def hitung_zona_dari_rp(rp_sec):
    return {
        "RP":       format_waktu(rp_sec),
        "Easy":     f"{format_waktu(rp_sec + 60)} - {format_waktu(rp_sec + 90)}",
        "Tempo":    f"{format_waktu(rp_sec + 10)} - {format_waktu(rp_sec + 20)}",
        "Interval": f"{format_waktu(rp_sec - 15)} - {format_waktu(rp_sec - 5)}",
        "Long":     f"{format_waktu(rp_sec + 60)} - {format_waktu(rp_sec + 120)}",
    }

def format_durasi(sisa_hari):
    minggu = sisa_hari // 7
    sisa   = sisa_hari % 7
    if sisa == 0:
        return f"{minggu} minggu"
    return f"{minggu} minggu {sisa} hari ({sisa_hari} hari total)"


# ─────────────────────────────────────────
# CORE SCHEDULE LOGIC
# Menggunakan jadwal Hal Higdon ASLI tanpa modifikasi hari
# Race day selalu di kolom paling kanan
# ─────────────────────────────────────────
def generate_full_table(data, target_level, target_rp_sec):
    """
    Menghasilkan tabel jadwal dengan 7 kolom hari sesuai Hal Higdon.
    Kolom dirotasi sehingga hari race_day selalu di PALING KANAN.
    Jadwal DB Hal Higdon tetap utuh — hanya urutan kolom yang digeser.
    """
    jarak         = data["jarak"]
    sisa_waktu    = data["sisa_waktu"]
    tanggal_lomba = datetime.datetime.strptime(data["tanggal_lomba"], "%Y-%m-%d").date()
    tanggal_mulai = datetime.datetime.strptime(data["tanggal_mulai"], "%Y-%m-%d").date()

    # Hari race
    race_weekday_idx = tanggal_lomba.weekday()  # 0=Senin ... 6=Minggu
    nama_hari_race   = NAMA_HARI_STANDAR[race_weekday_idx]

    # Bangun header_ui: 7 kolom, pos 6 (kanan) = race_day
    # Formula: header_ui[pos] = NAMA_HARI_STANDAR[(race_weekday_idx - 6 + pos) % 7]
    # Contoh race=Selasa(1): [Rabu,Kamis,Jumat,Sabtu,Minggu,Senin,Selasa]
    # Contoh race=Jumat(4):  [Sabtu,Minggu,Senin,Selasa,Rabu,Kamis,Jumat]
    header_ui = [NAMA_HARI_STANDAR[(race_weekday_idx - 6 + pos) % 7] for pos in range(7)]
    # Verifikasi: header_ui[6] == nama_hari_race selalu benar

    # Mapping DB hari -> UI kolom posisi:
    # DB Senin(idx=0)->UI pos 0, ..., DB Minggu(idx=6)->UI pos 6
    # Posisi SAMA persis — yang berubah hanya NAMA label di header.
    # Sesi DB Minggu (long run) otomatis tampil di UI pos 6 = kolom race_day.
    db_hari_to_ui_pos = {NAMA_HARI_STANDAR[i]: i for i in range(7)}

    durasi_ideal  = hal_higdon_db[jarak][target_level]["durasi_minggu"]
    jadwal_mentah = hal_higdon_db[jarak][target_level]["jadwal"]
    jadwal_terpilih = {}

    base_level_str = "Novice"
    if "Intermediate" in target_level:
        base_level_str = "Intermediate"
    elif "Advance" in target_level or "Advanced" in target_level:
        base_level_str = "Advanced"

    if sisa_waktu < durasi_ideal:
        st.warning(
            f"Sisa waktu **{sisa_waktu} minggu** (ideal {durasi_ideal} minggu). "
            f"Jadwal dipotong cerdas dari fase inti."
        )
        minggu_mulai = durasi_ideal - sisa_waktu + 1
        for i in range(minggu_mulai, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]
    elif sisa_waktu > durasi_ideal:
        selisih = sisa_waktu - durasi_ideal
        st.success(
            f"Waktu persiapan panjang! Sistem menyisipkan **{selisih} minggu Base Training** "
            f"sebelum program inti."
        )
        try:
            jadwal_base = hal_higdon_db["Base_Training"][base_level_str]["jadwal"]
        except KeyError:
            jadwal_base = {"1": {
                "Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Cross training",
                "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km",
                "Minggu": "Lari 9.7 km"
            }}
        for i in range(1, selisih + 1):
            key_base = str(((i - 1) % 12) + 1)
            jadwal_terpilih[i] = jadwal_base.get(key_base, list(jadwal_base.values())[0])
        for i in range(1, durasi_ideal + 1):
            key_inti = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[selisih + i] = jadwal_mentah[key_inti]
    else:
        for i in range(1, durasi_ideal + 1):
            key = str(i) if str(i) in jadwal_mentah else i
            jadwal_terpilih[i] = jadwal_mentah[key]

    list_minggu     = sorted(jadwal_terpilih.keys())
    minggu_terakhir = list_minggu[-1] if list_minggu else 0
    tabel_ui, tabel_pdf = [], []

    for m, menu_db in jadwal_terpilih.items():
        is_race_week = (m == minggu_terakhir)
        is_taper     = (m == minggu_terakhir) or (
            jarak == "Marathon" and m >= minggu_terakhir - 2
        )

        # Hitung tanggal: minggu race = minggu_terakhir
        # Tanggal race di minggu ini:
        tgl_race_minggu = tanggal_lomba - datetime.timedelta(days=(minggu_terakhir - m) * 7)

        # Awal minggu UI = tgl_race_minggu - 6 hari (karena race di kolom paling kanan = hari ke-7)
        tgl_awal_ui = tgl_race_minggu - datetime.timedelta(days=6)

        label_ui  = f"M-{m}\n{tgl_awal_ui.strftime('%d %b')} –\n{tgl_race_minggu.strftime('%d %b')}"
        label_pdf = f"M-{m} | {tgl_awal_ui.strftime('%d %b')} - {tgl_race_minggu.strftime('%d %b')}"
        if is_taper:
            label_ui  += "\n(Taper)"
            label_pdf += " (Taper)"

        baris_ui  = {"Minggu Ke-": label_ui}
        baris_pdf = {"Minggu Ke-": label_pdf}

        # Isi 7 kolom UI — iterasi per kolom UI (0=kiri ... 6=kanan/race)
        # Untuk setiap kolom UI, cari DB hari yang berkorespondensi menggunakan
        # db_hari_to_ui_pos: db_nama -> ui_pos
        # Kita perlu kebalikannya: ui_pos -> db_nama
        ui_pos_to_db_nama = {v: k for k, v in db_hari_to_ui_pos.items()}

        for ui_col_idx in range(7):
            ui_hari_nama = header_ui[ui_col_idx]
            is_race_col  = (ui_col_idx == 6)
            db_hari_nama = ui_pos_to_db_nama.get(ui_col_idx)

            # Tanggal kolom ini (untuk cek Blm Mulai)
            tgl_kolom = tgl_awal_ui + datetime.timedelta(days=ui_col_idx)

            # Prioritas:
            # 1. Race Day = kolom paling kanan di minggu terakhir
            if is_race_week and is_race_col:
                teks_ui  = f"🎯 RACE DAY!\n{jarak}"
                teks_pdf = f"RACE DAY! {jarak}"

            # 2. Belum mulai
            elif tgl_kolom < tanggal_mulai:
                teks_ui  = "➖ Blm Mulai"
                teks_pdf = "Blm Mulai"

            # 3. Isi dari DB Hal Higdon (urutan asli terjaga)
            else:
                sesi = menu_db.get(db_hari_nama, "Istirahat") if db_hari_nama else "Istirahat"
                if "istirahat" in sesi.lower() and not any(
                    x in sesi.lower() for x in ["lari", "km", "cross", "tempo", "jalan"]
                ):
                    teks_ui  = f"🛌 {sesi}"
                    teks_pdf = sesi
                elif any(x in sesi.lower() for x in ["km", "tempo", "interval", "hill", "pace", "lari", "jalan"]):
                    teks_ui  = f"🏃 {sesi}"
                    teks_pdf = sesi
                else:
                    teks_ui  = sesi
                    teks_pdf = sesi

            baris_ui[ui_hari_nama]  = teks_ui
            baris_pdf[ui_hari_nama] = teks_pdf

        tabel_ui.append(baris_ui)
        tabel_pdf.append(baris_pdf)

    return tabel_ui, tabel_pdf, header_ui, nama_hari_race


# ─────────────────────────────────────────
# PDF CLASS – A4 PORTRAIT, 2 HALAMAN
# ─────────────────────────────────────────
class PDFLatihan(FPDF):
    def header(self):
        pass  # header custom per halaman

    def footer(self):
        self.set_y(-12)
        self.set_font("helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 6, f"RunSmart - Asisten Lari Cerdas | Hal Higdon Methodology | Hal. {self.page_no()}", align="C")


def clean_pdf_text(s):
    result = []
    for ch in str(s):
        try:
            ch.encode("latin-1")
            result.append(ch)
        except (UnicodeEncodeError, UnicodeDecodeError):
            replacements = {
                "\u2013": "-", "\u2014": "-", "\u2019": "'", "\u2018": "'",
                "\u201c": '"', "\u201d": '"', "\u2192": "->", "\u00d7": "x",
            }
            result.append(replacements.get(ch, ""))
    return "".join(result)


def potong_teks(teks: str, maks_karakter: int) -> str:
    t = teks.strip()
    if len(t) > maks_karakter:
        return t[:maks_karakter - 2] + ".."
    return t


def _render_halaman_jadwal(pdf, data, jadwal_tabel, zona, header_ui, nama_hari_race,
                           judul_opsi="", warna_banner=(249, 115, 22)):
    """
    Render SATU halaman jadwal A4 Portrait ke dalam objek pdf.
    Dipanggil 1x (normal) atau 2x (dual-track: opsi aman + ambisius).
    """
    MARGIN_L = 8
    MARGIN_R = 8
    PAGE_W   = 210   # A4 Portrait
    USABLE_W = PAGE_W - MARGIN_L - MARGIN_R  # ~194 mm

    # ── Banner Header ──
    br, bg, bb = warna_banner
    pdf.set_fill_color(br, bg, bb)
    pdf.rect(0, 0, PAGE_W, 22, "F")
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(MARGIN_L, 2)

    judul_level = judul_opsi if judul_opsi else data['level']
    pdf.cell(USABLE_W, 7,
             clean_pdf_text(f"RUNSMART  |  {judul_level} - {data['jarak']}  |  {data['nama']}"),
             align="L")
    pdf.set_font("helvetica", "", 7.5)
    pdf.set_xy(MARGIN_L, 10)
    pdf.cell(USABLE_W, 5,
             clean_pdf_text(
                 f"Mulai: {data['tanggal_mulai']}   |   Lomba: {data['tanggal_lomba']}"
                 f"   |   Race Day: {nama_hari_race} (kolom kanan)"
             ), align="L")
    pdf.set_xy(MARGIN_L, 16)
    pdf.cell(USABLE_W, 5,
             clean_pdf_text(
                 f"Target Finis: {data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}"
                 f"   |   RP: {zona['RP']}"
                 f"   |   Easy: {zona['Easy']}"
                 f"   |   Tempo: {zona['Tempo']}"
                 f"   |   Interval: {zona['Interval']}"
             ), align="L")
    pdf.ln(23)

    # ── Setup kolom tabel ──
    if jadwal_tabel:
        kolom_hari = [k for k in jadwal_tabel[0].keys() if k != "Minggu Ke-"]
    else:
        kolom_hari = [h for h in header_ui if h]

    N_HARI       = len(kolom_hari)
    LEBAR_MG     = 20          # kolom "Minggu Ke-"
    LEBAR_HARI   = (USABLE_W - LEBAR_MG) / N_HARI
    TINGGI_BARIS = 7           # tinggi baris lebih kecil agar muat di portrait

    # Karakter maks per sel (estimasi: ~1.55 mm per karakter pada font 5.5pt)
    MAKS_CHAR_HARI = max(5, int(LEBAR_HARI / 1.55))
    MAKS_CHAR_MG   = max(5, int(LEBAR_MG  / 1.55))

    # ── Header tabel ──
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 6)
    pdf.cell(LEBAR_MG, TINGGI_BARIS, "MINGGU", border=1, align="C", fill=True)
    for h in kolom_hari:
        lbl = h.upper()[:8]
        if h == nama_hari_race:
            lbl = f"*{lbl}*"
        pdf.cell(LEBAR_HARI, TINGGI_BARIS, clean_pdf_text(lbl), border=1, align="C", fill=True)
    pdf.ln()

    # ── Isi baris ──
    for idx, row in enumerate(jadwal_tabel):
        # page-break check — sisakan ruang untuk footer & keterangan
        if pdf.get_y() > 270:
            pdf.add_page(orientation="P")
            # ulang header tabel setelah page break
            pdf.set_fill_color(30, 41, 59)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("helvetica", "B", 6)
            pdf.cell(LEBAR_MG, TINGGI_BARIS, "MINGGU (lanjutan)", border=1, align="C", fill=True)
            for h in kolom_hari:
                lbl = h.upper()[:8]
                if h == nama_hari_race:
                    lbl = f"*{lbl}*"
                pdf.cell(LEBAR_HARI, TINGGI_BARIS, clean_pdf_text(lbl), border=1, align="C", fill=True)
            pdf.ln()

        if idx % 2 == 0:
            pdf.set_fill_color(248, 249, 252)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.set_text_color(30, 41, 59)

        mg_raw   = str(row.get("Minggu Ke-", "-")).replace("\n", " ").replace("(Taper)", "(T)")
        mg_clean = potong_teks(clean_pdf_text(mg_raw), MAKS_CHAR_MG)
        pdf.set_font("helvetica", "", 5.5)
        pdf.cell(LEBAR_MG, TINGGI_BARIS, mg_clean, border=1, align="C", fill=True)

        for hari in kolom_hari:
            teks_raw   = str(row.get(hari, "-"))
            teks_clean = clean_pdf_text(
                teks_raw
                .replace("🛌 ", "").replace("🏃 ", "").replace("➖ ", "")
                .replace("🎯 ", "").replace("🏁", "").replace("✅", "")
                .replace("\n", " ").strip()
            )
            teks_ptg = potong_teks(teks_clean, MAKS_CHAR_HARI)

            is_race = "RACE DAY" in teks_raw.upper()
            is_long = (hari == nama_hari_race) and not is_race

            if is_race:
                pdf.set_font("helvetica", "B", 6)
                pdf.set_text_color(200, 50, 0)
            elif is_long:
                pdf.set_font("helvetica", "I", 5.5)
                pdf.set_text_color(20, 90, 180)
            else:
                pdf.set_font("helvetica", "", 5.5)
                pdf.set_text_color(30, 41, 59)

            pdf.cell(LEBAR_HARI, TINGGI_BARIS, teks_ptg, border=1, align="C", fill=True)
            pdf.set_text_color(30, 41, 59)

        pdf.ln()

    # ── Keterangan bawah ──
    pdf.ln(1)
    pdf.set_font("helvetica", "", 5.5)
    pdf.set_text_color(110, 110, 110)
    pdf.cell(USABLE_W, 4,
             clean_pdf_text(
                 f"*{nama_hari_race} = Race Day & Long Run (kolom kanan).  "
                 "Biru miring = Long Run.  Merah tebal = Race Day."
             ), align="L")


def _render_halaman_edukasi(pdf, data, zona):
    """Render halaman Pusat Edukasi Lari (A4 Portrait)."""
    MARGIN_L  = 8
    MARGIN_R  = 8
    PAGE_W_P  = 210
    USABLE_WP = PAGE_W_P - MARGIN_L - MARGIN_R  # ~194 mm

    # ── Banner ──
    pdf.set_fill_color(30, 41, 59)
    pdf.rect(0, 0, PAGE_W_P, 22, "F")
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(249, 115, 22)
    pdf.set_xy(MARGIN_L, 3)
    pdf.cell(USABLE_WP, 9, "PUSAT EDUKASI LARI", align="C")
    pdf.set_font("helvetica", "", 7.5)
    pdf.set_text_color(200, 200, 200)
    pdf.set_xy(MARGIN_L, 13)
    pdf.cell(USABLE_WP, 6,
             clean_pdf_text(f"RunSmart - Program {data['level']} {data['jarak']} | {data['nama']}"),
             align="C")
    pdf.ln(22)

    # ── Zona Pace Box ──
    box_y = pdf.get_y()
    pdf.set_fill_color(255, 248, 240)
    pdf.set_draw_color(249, 115, 22)
    pdf.set_line_width(0.4)
    pdf.rect(MARGIN_L, box_y, USABLE_WP, 26, "FD")
    pdf.set_xy(MARGIN_L + 3, box_y + 2)
    pdf.set_font("helvetica", "B", 8)
    pdf.set_text_color(180, 60, 0)
    pdf.cell(USABLE_WP - 6, 5, "ZONA PACE TARGET LATIHAN ANDA", align="C")
    pdf.ln(6)

    zona_items = [
        ("Race Pace (RP)", zona["RP"]),
        ("Easy / Long Run", zona["Easy"]),
        ("Tempo",           zona["Tempo"]),
        ("Interval",        zona["Interval"]),
        ("Long Run Safe",   zona["Long"]),
    ]
    col_w_z = (USABLE_WP - 6) / 2
    for i in range(0, len(zona_items), 2):
        pdf.set_x(MARGIN_L + 3)
        for j in range(2):
            if i + j < len(zona_items):
                lbl, val = zona_items[i + j]
                pdf.set_font("helvetica", "B", 7)
                pdf.set_text_color(80, 80, 80)
                pdf.cell(col_w_z * 0.45, 4.5, clean_pdf_text(lbl + ": "))
                pdf.set_font("helvetica", "B", 7)
                pdf.set_text_color(200, 60, 0)
                pdf.cell(col_w_z * 0.55, 4.5, clean_pdf_text(val))
        pdf.ln(4.5)
    pdf.ln(4)

    # ── Helper untuk render satu section ──
    def section(col_x, col_w, title, lines, fill_rgb):
        pdf.set_x(col_x)
        pdf.set_fill_color(*fill_rgb)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("helvetica", "B", 7.5)
        pdf.cell(col_w, 6, clean_pdf_text(f"  {title}"), fill=True)
        pdf.set_xy(col_x, pdf.get_y() + 6)
        pdf.ln(0.5)
        pdf.set_text_color(40, 40, 40)
        pdf.set_font("helvetica", "", 6.5)
        for line in lines:
            pdf.set_x(col_x + 2)
            pdf.cell(col_w - 2, 4, clean_pdf_text(f"- {line}"), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2.5)

    # ── Dua kolom ──
    TOP_Y  = pdf.get_y()
    COL_W  = (USABLE_WP - 4) / 2
    COL1_X = MARGIN_L
    COL2_X = MARGIN_L + COL_W + 4

    # KOLOM KIRI
    pdf.set_xy(COL1_X, TOP_Y)
    section(COL1_X, COL_W, "TAPERING", [
        "Pengurangan beban latihan menjelang hari H.",
        "Tujuan: mengisi ulang energi otot yang terkuras.",
        "Marathon = 3 mgg | Half Marathon/10K = 1-2 mgg | 5K = 1 mgg.",
        "JANGAN tambah latihan baru saat tapering!",
        "Rasa berat / gelisah saat tapering adalah NORMAL.",
    ], (30, 41, 59))
    section(COL1_X, COL_W, "LONG RUN", [
        "Sesi terpenting per minggu — fondasi daya tahan.",
        "Selalu berlari LEBIH LAMBAT dari race pace.",
        "Target: bisa berlari sambil mengobrol (RPE 5/10).",
        "Di RunSmart, Long Run = kolom Race Day setiap minggu.",
        "Naikkan jarak maks 10% per minggu (10% Rule).",
        "Jangan skip Long Run — tidak bisa diganti sesi lain.",
    ], (20, 80, 160))
    section(COL1_X, COL_W, "LATIHAN INTERVAL", [
        "Contoh: 4 x 400m (4 repetisi sejauh 400 meter).",
        "1. Pemanasan jogging 1-2 km pelan.",
        "2. Lari SECEPAT mungkin sejauh jarak yg ditentukan.",
        "3. Recovery: jalan / jogging pelan 2-3 menit.",
        "4. Ulangi sesuai jumlah set (mis. 4 kali).",
        "5. Pendinginan jogging 1 km pelan.",
        "Manfaat: tingkatkan VO2max & kecepatan puncak.",
    ], (180, 30, 30))
    section(COL1_X, COL_W, "PRINSIP HARD-EASY", [
        "Pilar utama metodologi Hal Higdon.",
        "Setelah sesi BERAT, WAJIB ada sesi ringan/istirahat.",
        "Tidak boleh 2 hari berat berurutan.",
        "Otot perlu 24-48 jam untuk pulih dan bertumbuh.",
        "Contoh: Sel. Interval -> Rab. Easy -> Kam. Tempo.",
        "Melanggar prinsip ini = risiko overtraining & cedera.",
    ], (100, 60, 160))

    y_after_col1 = pdf.get_y()

    # KOLOM KANAN
    pdf.set_xy(COL2_X, TOP_Y)
    section(COL2_X, COL_W, "LARI TEMPO", [
        "Bukan sprint — berlari di ambang anaerobik.",
        "RPE sekitar 7/10 (agak susah ngobrol).",
        "1. Pemanasan 15 menit jogging pelan.",
        "2. Akselerasi ke race pace, tahan 10-20 menit.",
        "3. Pendinginan 10 menit jogging pelan.",
        "Manfaat: tingkatkan lactic threshold.",
        "Lakukan 1x per minggu — jangan berlebihan.",
    ], (180, 100, 0))
    section(COL2_X, COL_W, "CROSS TRAINING", [
        "Olahraga aerobik selain lari, 30-60 menit.",
        "BOLEH: Bersepeda, renang, jalan cepat, elliptical.",
        "DILARANG: Futsal, basket, badminton (risiko keseleo).",
        "Tujuan: jaga kebugaran tanpa beban ke kaki.",
        "Bisa diganti istirahat aktif jika kaki sangat lelah.",
    ], (0, 130, 100))
    section(COL2_X, COL_W, "STEPBACK / RECOVERY WEEK", [
        "Jarak tidak selalu naik — ada minggu yang turun.",
        "Pola umum: naik 3 minggu, turun 1 minggu.",
        "Ini BUKAN kemunduran — bagian penting program!",
        "Tubuh makin kuat saat ada istirahat & recovery.",
        "Jangan tambah volume sendiri saat stepback week.",
    ], (60, 100, 60))
    section(COL2_X, COL_W, "TIPS RACE DAY", [
        "Jangan coba hal baru di hari H (sepatu, gel, dll).",
        "Sarapan 2-3 jam sebelum start, sudah teruji.",
        "Start PELAN — jangan terbawa euforia crowd.",
        "Minum cukup, jangan tunggu haus baru minum.",
        "Km terakhir: keluarkan semua yang tersisa!",
        "Nikmati pencapaian Anda — Anda sudah luar biasa!",
    ], (200, 60, 0))

    y_after_col2 = pdf.get_y()
    pdf.set_y(max(y_after_col1, y_after_col2) + 3)

    # ── Kamus Istilah ──
    pdf.set_fill_color(249, 115, 22)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(USABLE_WP, 6, "  KAMUS ISTILAH LARI",
             border=0, new_x="LMARGIN", new_y="NEXT", fill=True)
    pdf.ln(1)

    glosarium = [
        ("Conversational Pace", "Kecepatan lari sambil bisa berbicara — kecepatan Easy Run ideal."),
        ("RPE",                 "Rate of Perceived Exertion: skala 1-10 rasa berat latihan."),
        ("VO2max",              "Volume oksigen maksimal tubuh — indikator utama kebugaran aerobik."),
        ("Lactic Threshold",    "Titik akumulasi asam laktat — target utama latihan Tempo."),
        ("Fartlek",             "Variasi kecepatan bebas selama lari — campuran santai dan cepat."),
        ("Negative Split",      "Paruh kedua lomba lebih cepat dari paruh pertama — strategi ideal."),
        ("BQ",                  "Boston Qualify: waktu minimal lolos kualifikasi Boston Marathon."),
        ("DNS / DNF",           "Did Not Start / Did Not Finish — hindari dengan persiapan matang."),
    ]
    col_w_g = USABLE_WP / 2 - 2
    for i in range(0, len(glosarium), 2):
        pdf.set_x(MARGIN_L)
        for j in range(2):
            if i + j < len(glosarium):
                ist, art = glosarium[i + j]
                pdf.set_font("helvetica", "B", 6)
                pdf.set_text_color(180, 60, 0)
                pdf.cell(col_w_g * 0.32, 4, clean_pdf_text(f"{ist}: "))
                pdf.set_font("helvetica", "", 6)
                pdf.set_text_color(50, 50, 50)
                pdf.cell(col_w_g * 0.68, 4,
                         clean_pdf_text(potong_teks(art, int(col_w_g * 0.68 / 1.45))))
                if j == 0:
                    pdf.set_x(MARGIN_L + col_w_g + 4)
        pdf.ln(4)

    # ── Motivasi ──
    pdf.ln(2)
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(249, 115, 22)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(USABLE_WP, 8,
             clean_pdf_text(
                 '"Train smart, run happy. Setiap langkah membawa Anda lebih dekat ke garis finish."'
             ),
             border=0, new_x="LMARGIN", new_y="NEXT", fill=True, align="C")


# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI UTAMA PDF
# Mendukung:
#   - Mode normal  : 1 jadwal → Hal.1 Jadwal | Hal.2 Edukasi
#   - Mode dual    : 2 jadwal → Hal.1 Aman | Hal.2 Ambisius | Hal.3 Edukasi
# ─────────────────────────────────────────────────────────────────────────────
def buat_pdf(data, jadwal_tabel, zona, header_ui, nama_hari_race,
             jadwal_tabel_2=None, zona_2=None, header_ui_2=None,
             level_aman_label="", level_ambisi_label=""):
    """
    jadwal_tabel   : tabel PDF opsi utama (atau opsi aman jika dual-track)
    jadwal_tabel_2 : tabel PDF opsi ambisius (None = mode normal)
    """
    MARGIN_L = 8
    MARGIN_R = 8
    MARGIN_T = 14

    pdf = PDFLatihan(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.set_margins(MARGIN_L, MARGIN_T, MARGIN_R)

    # ── Halaman 1: Jadwal Utama / Jadwal Aman ──
    pdf.add_page(orientation="P")
    judul1 = level_aman_label if level_aman_label else data["level"]
    banner1 = (16, 185, 129) if jadwal_tabel_2 else (249, 115, 22)   # hijau jika dual, oranye jika normal
    _render_halaman_jadwal(pdf, data, jadwal_tabel, zona, header_ui, nama_hari_race,
                           judul_opsi=judul1, warna_banner=banner1)

    # ── Halaman 2 (hanya jika dual-track): Jadwal Ambisius ──
    if jadwal_tabel_2 is not None:
        pdf.add_page(orientation="P")
        judul2 = level_ambisi_label if level_ambisi_label else data["level"]
        _render_halaman_jadwal(pdf, data, jadwal_tabel_2, zona_2, header_ui_2, nama_hari_race,
                               judul_opsi=judul2, warna_banner=(239, 68, 68))  # merah = ambisius

    # ── Halaman terakhir: Pusat Edukasi ──
    pdf.add_page(orientation="P")
    # Gunakan zona opsi aman (atau satu-satunya) untuk edukasi
    _render_halaman_edukasi(pdf, data, zona)

    return bytes(pdf.output())

    # 5. Lari Tempo
    pdf.set_x(COL2_X)
    pdf.set_fill_color(180, 100, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(COL_W, 6, "  LARI TEMPO", fill=True)
    pdf.set_xy(COL2_X, pdf.get_y() + 6)
    pdf.ln(1)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("helvetica", "", 7)
    tempo_lines = [
        "Bukan sprint — berlari di ambang anaerobik.",
        "RPE sekitar 7/10 (agak susah ngobrol).",
        "1. Pemanasan 15 menit jogging pelan.",
        "2. Akselerasi ke race pace, tahan 10-20 menit.",
        "3. Pendinginan 10 menit jogging pelan.",
        "Manfaat: tingkatkan lactic threshold.",
        "Lakukan 1x per minggu saja — jangan berlebihan.",
    ]
    for line in tempo_lines:
        pdf.set_x(COL2_X + 2)
        pdf.cell(COL_W - 2, 4.5, clean_pdf_text(f"- {line}"), new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(COL2_X)
    pdf.ln(3)

    # 6. Cross Training
    pdf.set_x(COL2_X)
    pdf.set_fill_color(0, 130, 100)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(COL_W, 6, "  CROSS TRAINING")
    pdf.set_xy(COL2_X, pdf.get_y() + 6)
    pdf.ln(1)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("helvetica", "", 7)
    cross_lines = [
        "Olahraga aerobik selain lari, 30-60 menit.",
        "BOLEH: Bersepeda, renang, jalan cepat, elliptical.",
        "DILARANG: Futsal, basket, badminton (risiko keseleo).",
        "Tujuan: jaga kebugaran tanpa beban ke kaki.",
        "Bisa diganti istirahat aktif jika kaki sangat lelah.",
    ]
    for line in cross_lines:
        pdf.set_x(COL2_X + 2)
        pdf.cell(COL_W - 2, 4.5, clean_pdf_text(f"- {line}"), new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(COL2_X)
    pdf.ln(3)

    # 7. Stepback / Recovery Week
    pdf.set_x(COL2_X)
    pdf.set_fill_color(60, 100, 60)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(COL_W, 6, "  STEPBACK / RECOVERY WEEK")
    pdf.set_xy(COL2_X, pdf.get_y() + 6)
    pdf.ln(1)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("helvetica", "", 7)
    step_lines = [
        "Jarak tidak selalu naik — ada minggu yang turun.",
        "Pola umum: naik 3 minggu, turun 1 minggu.",
        "Ini BUKAN kemunduran — ini bagian dari program!",
        "Tubuh menjadi lebih kuat saat istirahat & recovery.",
        "Jangan tambah volume sendiri saat stepback week.",
    ]
    for line in step_lines:
        pdf.set_x(COL2_X + 2)
        pdf.cell(COL_W - 2, 4.5, clean_pdf_text(f"- {line}"), new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(COL2_X)
    pdf.ln(3)

    # 8. Tips Race Day
    pdf.set_x(COL2_X)
    pdf.set_fill_color(200, 60, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(COL_W, 6, "  TIPS RACE DAY")
    pdf.set_xy(COL2_X, pdf.get_y() + 6)
    pdf.ln(1)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("helvetica", "", 7)
    race_lines = [
        "Jangan mencoba hal baru di hari H (sepatu, gel, dll).",
        "Sarapan 2-3 jam sebelum start, sudah teruji.",
        "Start PELAN — jangan terbawa euforia crowd.",
        "Minum cukup, jangan tunggu haus baru minum.",
        "Km terakhir: keluarkan semua yang tersisa!",
        "Nikmati pencapaian Anda — Anda sudah luar biasa!",
    ]
    for line in race_lines:
        pdf.set_x(COL2_X + 2)
        pdf.cell(COL_W - 2, 4.5, clean_pdf_text(f"- {line}"), new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(COL2_X)

    y_after_col2 = pdf.get_y()

    # ── Pindah ke bawah kolom terpanjang ──
    pdf.set_y(max(y_after_col1, y_after_col2) + 4)

    # ── Glosarium Istilah ──
    pdf.set_fill_color(249, 115, 22)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(USABLE_WP, 7, "  KAMUS ISTILAH LARI",
             border=0, new_x="LMARGIN", new_y="NEXT", fill=True)
    pdf.ln(1)

    glosarium = [
        ("Conversational Pace",  "Kecepatan lari sambil bisa berbicara nyaman — kecepatan Easy Run ideal."),
        ("RPE",                  "Rate of Perceived Exertion: skala 1-10 seberapa berat terasa latihan."),
        ("VO2max",               "Volume oksigen maksimal yang bisa dipakai tubuh — indikator kebugaran."),
        ("Lactic Threshold",     "Titik di mana asam laktat terakumulasi — target latihan Tempo."),
        ("BQ / Boston Qualify",  "Waktu minimal untuk lolos kualifikasi Boston Marathon."),
        ("Fartlek",              "Variasi kecepatan bebas selama lari — campuran santai dan cepat."),
        ("Negative Split",       "Paruh kedua lomba lebih cepat dari paruh pertama — strategi ideal."),
        ("DNS / DNF",            "Did Not Start / Did Not Finish — hindari dengan persiapan matang."),
    ]

    col_w_g = USABLE_WP / 2 - 2
    for i in range(0, len(glosarium), 2):
        pdf.set_x(MARGIN_L)
        for j in range(2):
            if i + j < len(glosarium):
                istilah, arti = glosarium[i + j]
                pdf.set_font("helvetica", "B", 6.5)
                pdf.set_text_color(180, 60, 0)
                pdf.cell(col_w_g * 0.38, 4.5, clean_pdf_text(f"{istilah}: "))
                pdf.set_font("helvetica", "", 6.5)
                pdf.set_text_color(50, 50, 50)
                arti_ptg = potong_teks(arti, int(col_w_g * 0.62 / 1.55))
                pdf.cell(col_w_g * 0.62, 4.5, clean_pdf_text(arti_ptg))
                if j == 0:
                    pdf.set_x(MARGIN_L + col_w_g + 4)
        pdf.ln(4.5)

    # ── Footer motivasi ──
    pdf.ln(3)
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(249, 115, 22)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(USABLE_WP, 8,
             clean_pdf_text('"Train smart, run happy. Setiap langkah membawa Anda lebih dekat ke garis finish."'),
             border=0, new_x="LMARGIN", new_y="NEXT", fill=True, align="C")

    return bytes(pdf.output())


# ─────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "onboarding"


# ══════════════════════════════════════════
# PAGE 1 – ONBOARDING
# ══════════════════════════════════════════
if st.session_state.page == "onboarding":

    st.markdown("""
    <div style="margin-bottom:8px;">
        <h1 style="margin-bottom:4px;">RUNSMART</h1>
        <p class="hero-subtitle">Asisten Jadwal Latihan Berbasis Metodologi Hal Higdon</p>
    </div>
    <div style="margin-bottom:32px;">
        <span class="stat-badge">🏃 5K – Marathon</span>
        <span class="stat-badge">📊 Hal Higdon Database</span>
        <span class="stat-badge">📄 Export PDF 2 Halaman</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👤 Profil & Target Lomba")
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda...")
    with col2:
        jarak_target = st.selectbox(
            "Target Jarak Lomba",
            [k for k in hal_higdon_db.keys() if k != "Base_Training"]
        )

    st.markdown("---")

    st.markdown("### ⏱️ Mode Penentuan Target & Pace")
    metode_target = st.radio(
        "Pilih pendekatan target Anda:",
        [
            "1. Mode Pemula — Hanya ingin finis dengan aman & nyaman",
            "2. Mode Realistis — Hitung dari Easy Run pace saya saat ini",
            "3. Mode Ambisius — Saya punya target waktu finis impian",
        ],
        label_visibility="collapsed"
    )

    jam_finis, menit_finis, detik_finis = 0, 0, 0
    ez_m, ez_s = 7, 0

    if "Realistis" in metode_target:
        st.info("💡 Masukkan rata-rata pace saat Anda berlari santai (bisa sambil ngobrol).")
        c1, c2 = st.columns(2)
        ez_m = c1.number_input("Pace Santai – Menit", min_value=3, max_value=15, value=7)
        ez_s = c2.number_input("Pace Santai – Detik", min_value=0, max_value=59, value=0)

        jarak_km    = jarak_ke_km[jarak_target]
        ez_sec_tmp  = (ez_m * 60) + ez_s
        rp_sec_tmp  = ez_sec_tmp - 70
        if rp_sec_tmp > 0:
            total_tmp = rp_sec_tmp * jarak_km
            j_p = int(total_tmp // 3600)
            m_p = int((total_tmp % 3600) // 60)
            s_p = int(total_tmp % 60)
            pm  = int(rp_sec_tmp // 60)
            ps  = int(rp_sec_tmp % 60)
            st.success(
                f"Prediksi: Easy pace **{ez_m}:{ez_s:02d}/km** → "
                f"Race Pace **{pm}:{ps:02d}/km** → "
                f"Estimasi finis {jarak_target}: **{j_p}j {m_p}m {s_p}d**"
            )

    elif "Ambisius" in metode_target:
        st.warning("Masukkan target waktu finis impian Anda.")
        cj, cm, cs = st.columns(3)
        jam_finis   = cj.number_input("Jam",   min_value=0, max_value=10, value=0)
        menit_finis = cm.number_input("Menit", min_value=0, max_value=59, value=25)
        detik_finis = cs.number_input("Detik", min_value=0, max_value=59, value=0)

    st.markdown("---")

    st.markdown("### 🩺 Riwayat Medis & Kebiasaan Lari")
    col3, col4, col5 = st.columns(3)
    with col3:
        cedera = st.selectbox(
            "Riwayat cedera 6 bulan terakhir?",
            ["Tidak ada, sehat 100%", "Ada nyeri ringan", "Ya, pernah cedera berat"]
        )
    with col4:
        frekuensi = st.radio(
            "Berapa kali lari per minggu saat ini?",
            ["< 1x", "1–2x", "3–4x", "> 4x"]
        )
    with col5:
        speedwork = st.radio(
            "Familiar dengan latihan Interval/Kecepatan?",
            ["Tidak tahu", "Pernah sesekali", "Ya, Rutin"]
        )

    st.markdown("---")

    # ─── KALENDER – tanggal lomba & mulai ───
    st.markdown("### 🗓️ Kalender Program")
    st.markdown(
        "<p style='color:#94a3b8;font-size:0.88rem;margin-bottom:4px;'>"
        "Pilih tanggal lomba Anda. Jadwal dari Hal Higdon akan langsung disesuaikan "
        "sehingga <strong style='color:#fdba74;'>hari Race Day selalu tampil di kolom paling kanan</strong> "
        "tabel, dan Long Run setiap minggu juga jatuh di hari yang sama.</p>",
        unsafe_allow_html=True
    )

    hari_ini = datetime.date.today()
    col_l, col_r = st.columns(2)
    with col_l:
        default_lomba = hari_ini + datetime.timedelta(days=56)
        tanggal_lomba = st.date_input(
            "🏁 Tanggal Hari H Lomba",
            value=default_lomba,
            min_value=hari_ini + datetime.timedelta(days=7)
        )
    with col_r:
        tanggal_mulai = st.date_input(
            "🏃 Mulai Berlatih",
            value=hari_ini,
            min_value=hari_ini,
            max_value=tanggal_lomba - datetime.timedelta(days=1)
        )

    sisa_hari   = (tanggal_lomba - tanggal_mulai).days
    sisa_waktu  = max(1, (sisa_hari // 7) + 1)
    durasi_str  = format_durasi(sisa_hari)
    nama_hari_lomba_str = NAMA_HARI_STANDAR[tanggal_lomba.weekday()]

    st.markdown(
        f"""<div class="duration-display">
            <span style="font-size:1.8rem;">⏳</span>
            <div>
                <div style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.1rem;color:#fdba74;">
                    Durasi Persiapan: {durasi_str}
                </div>
                <div style="font-family:'Space Grotesk',sans-serif;font-size:0.88rem;color:#94a3b8;margin-top:4px;">
                    Mulai {tanggal_mulai.strftime('%d %b %Y')} &rarr; Lomba {tanggal_lomba.strftime('%d %b %Y')}
                    &nbsp;·&nbsp; Race Day: <strong style="color:#fdba74;">{nama_hari_lomba_str}</strong>
                    &nbsp;·&nbsp; Kolom <strong style="color:#fdba74;">{nama_hari_lomba_str}</strong> = Long Run &amp; Race Day di tabel
                </div>
            </div>
        </div>""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col_btn = st.columns([1, 2, 1])
    with col_btn[1]:
        tombol = st.button("🔍 Analisis & Hasilkan Jadwal Saya", use_container_width=True)

    if tombol:
        if not nama.strip():
            st.error("❌ Nama lengkap harus diisi!")
            st.stop()

        pesan_peringatan = ""
        level_tersedia   = list(hal_higdon_db[jarak_target].keys())
        rp_sec           = 999
        jarak_km         = jarak_ke_km[jarak_target]

        if "Realistis" in metode_target:
            ez_sec      = (ez_m * 60) + ez_s
            rp_sec      = ez_sec - 70
            total_detik = rp_sec * jarak_km
            jam_finis   = int(total_detik // 3600)
            menit_finis = int((total_detik % 3600) // 60)
            detik_finis = int(total_detik % 60)
        elif "Ambisius" in metode_target:
            total_detik = (jam_finis * 3600) + (menit_finis * 60) + detik_finis
            if total_detik > 0:
                rp_sec = total_detik / jarak_km

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

        level_final      = base_level
        resiko_ditemukan = False
        rp_sec_aman      = rp_sec
        level_aman       = base_level

        batas_bawah_db = {"5K": 3, "10K": 4, "Half Marathon": 8, "Marathon": 12}
        batas_bawah    = batas_bawah_db[jarak_target]
        if sisa_waktu < batas_bawah:
            pesan_peringatan += (
                f"🚨 **WAKTU KRITIS:** Persiapan aman minimal {jarak_target} = {batas_bawah} minggu. "
                f"Anda hanya punya {sisa_waktu} minggu ({sisa_hari} hari). Risiko cedera tinggi.\n\n"
            )

        if "Ya, pernah cedera berat" in cedera:
            pesan_peringatan += "⚠️ **RISIKO MEDIS:** Riwayat cedera berat terdeteksi. "
            resiko_ditemukan  = True
            opsi_aman = [k for k in level_tersedia if "Novice" in k or "Walker" in k]
            level_aman = opsi_aman[0] if opsi_aman else level_tersedia[0]
            if rp_sec_aman < 480:
                rp_sec_aman = 480
        elif rp_sec <= 330 and frekuensi in ["< 1x", "1–2x"]:
            pesan_peringatan += "⚠️ **RISIKO OVERTRAINING:** Pace ambisius tapi frekuensi latihan minim. "
            resiko_ditemukan  = True
            opsi_aman = [k for k in level_tersedia if "Novice" in k]
            level_aman = opsi_aman[-1] if opsi_aman else level_tersedia[0]
            if rp_sec_aman < 420:
                rp_sec_aman = 420
        elif rp_sec <= 270 and speedwork == "Tidak tahu":
            pesan_peringatan += "⚠️ **RISIKO TEKNIS:** Pace elite butuh adaptasi interval yang belum dimiliki. "
            resiko_ditemukan  = True
            opsi_aman = [k for k in level_tersedia if "Intermediate" in k]
            level_aman = opsi_aman[-1] if opsi_aman else level_tersedia[len(level_tersedia)//2]
            if rp_sec_aman < 330:
                rp_sec_aman = 330

        if resiko_ditemukan:
            total_detik_aman = rp_sec_aman * jarak_km
            jam_a   = int(total_detik_aman // 3600)
            menit_a = int((total_detik_aman % 3600) // 60)
            pesan_peringatan += (
                f"\n\n🛡️ **REKOMENDASI AMAN:** Program **{level_aman}** | "
                f"Estimasi {jam_a}j {menit_a}m.\n\n"
                f"💡 Jadwal ambisius ({level_final}) tetap tersedia sebagai opsi ke-2."
            )

        if "Pemula" in metode_target and not pesan_peringatan:
            opsi = [k for k in level_tersedia if "Novice" in k]
            level_final = opsi[0] if opsi else level_tersedia[0]

        total_detik_baru = rp_sec * jarak_km
        jam_finis   = int(total_detik_baru // 3600)
        menit_finis = int((total_detik_baru % 3600) // 60)
        detik_finis = int(total_detik_baru % 60)

        user_data = {
            "nama": nama.strip(),
            "jarak": jarak_target,
            "level": level_final,
            "sisa_waktu": sisa_waktu,
            "sisa_hari": sisa_hari,
            "durasi_str": durasi_str,
            "metode_target": metode_target,
            "rp_sec": rp_sec,
            "pesan_peringatan": pesan_peringatan,
            "jam_finis": jam_finis,
            "menit_finis": menit_finis,
            "detik_finis": detik_finis,
            "tanggal_lomba": tanggal_lomba.strftime("%Y-%m-%d"),
            "tanggal_mulai": tanggal_mulai.strftime("%Y-%m-%d"),
            "resiko_ditemukan": resiko_ditemukan,
            "level_aman": level_aman,
            "rp_sec_aman": rp_sec_aman,
        }
        try:
            simpan_data(user_data)
        except Exception:
            pass

        st.session_state.user_data = user_data
        st.session_state.page      = "jadwal"
        st.rerun()


# ══════════════════════════════════════════
# PAGE 2 – JADWAL
# ══════════════════════════════════════════
elif st.session_state.page == "jadwal":
    data = st.session_state.user_data

    tanggal_lomba_obj = datetime.datetime.strptime(data["tanggal_lomba"], "%Y-%m-%d").date()
    nama_hari_race    = NAMA_HARI_STANDAR[tanggal_lomba_obj.weekday()]

    st.markdown(f"""
    <h1>JADWAL LATIHAN</h1>
    <p class="hero-subtitle">Program untuk {data['nama']} · {data['jarak']} · {data['level']}</p>
    <div style="margin-bottom:24px;">
        <span class="stat-badge">📅 {data['durasi_str']}</span>
        <span class="stat-badge">🏁 Lomba {data['tanggal_lomba']} ({nama_hari_race})</span>
        <span class="stat-badge">📌 Race Day = kolom kanan: {nama_hari_race}</span>
    </div>
    """, unsafe_allow_html=True)

    if data.get("pesan_peringatan"):
        st.warning(data["pesan_peringatan"])

    col_back = st.columns([1, 5])
    with col_back[0]:
        if st.button("⬅️ Kembali"):
            st.session_state.page = "onboarding"
            st.rerun()

    st.markdown("---")

    def render_metrik_zona(rp_sec_target):
        zona = hitung_zona_dari_rp(rp_sec_target)
        zona["Long_Aman"] = f"{format_waktu(rp_sec_target + 20)} - {format_waktu(rp_sec_target + 60)}"
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Easy (Santai)", zona["Easy"])
        c2.metric("Long Run",      zona["Long_Aman"])
        c3.metric("Tempo",         zona["Tempo"])
        c4.metric("Interval",      zona["Interval"])
        return zona

    # ─── RENDER TABEL ───
    if data.get("resiko_ditemukan"):
        st.info("⚠️ **Mode Dual-Track:** 2 opsi jadwal tersedia.")

        st.markdown("### 🛡️ Opsi 1 – Jadwal Rekomendasi Aman")
        st.success(f"Program: **{data['level_aman']}** | Race Pace: **{format_waktu(data['rp_sec_aman'])}/km**")
        zona_aman = render_metrik_zona(data["rp_sec_aman"])
        tb_ui_aman, tb_pdf_aman, header_ui_aman, _ = generate_full_table(data, data["level_aman"], data["rp_sec_aman"])
        st.table(tb_ui_aman)

        st.markdown("---")
        st.markdown("### 🎯 Opsi 2 – Jadwal Target Ambisius (Risiko Tinggi)")
        st.error(f"Program: **{data['level']}** | Race Pace: **{format_waktu(data['rp_sec'])}/km**")
        zona_ambisi = render_metrik_zona(data["rp_sec"])
        tb_ui_ambisi, tb_pdf_ambisi, header_ui_ambisi, _ = generate_full_table(data, data["level"], data["rp_sec"])
        st.table(tb_ui_ambisi)
        tabel_rapi_pdf = tb_pdf_ambisi
        zona_pdf       = zona_ambisi
        header_ui_pdf  = header_ui_ambisi

    else:
        st.markdown("### 🎯 Zona Pace & Intensitas Latihan")
        if "Pemula" in data["metode_target"]:
            st.info("💡 **Mode Finish Happy:** Lari santai = bisa ngobrol (RPE 3–4/10).")
        elif "Realistis" in data["metode_target"]:
            st.success(
                f"Prediksi Finis: **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** "
                f"| Race Pace: **{format_waktu(data['rp_sec'])}/km**"
            )
        else:
            st.success(
                f"Target Finis: **{data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}** "
                f"| Race Pace: **{format_waktu(data['rp_sec'])}/km**"
            )

        zona_normal = render_metrik_zona(data["rp_sec"])
        tb_ui_normal, tb_pdf_normal, header_ui_normal, _ = generate_full_table(data, data["level"], data["rp_sec"])
        st.table(tb_ui_normal)
        tabel_rapi_pdf = tb_pdf_normal
        zona_pdf       = zona_normal
        header_ui_pdf  = header_ui_normal

    # ─── LEGEND ───
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.82rem;color:#94a3b8;'>"
        f"🏃 = Sesi Latihan &nbsp;·&nbsp; 🛌 = Istirahat/Recovery &nbsp;·&nbsp; "
        f"🎯 = Race Day &nbsp;·&nbsp; "
        f"<strong style='color:#fdba74;'>Kolom {nama_hari_race}</strong> = Long Run setiap minggu "
        f"(jadwal Hal Higdon dirotasi sehingga hari race selalu di kanan).</p>",
        unsafe_allow_html=True
    )

    # ─── DOWNLOAD PDF ───
    st.markdown("---")
    try:
        if data.get("resiko_ditemukan"):
            # Dual-track: kirim opsi aman (hal.1) + ambisius (hal.2) + edukasi (hal.3)
            pdf_bytes = buat_pdf(
                data,
                jadwal_tabel    = tb_pdf_aman,
                zona            = zona_aman,
                header_ui       = header_ui_aman,
                nama_hari_race  = nama_hari_race,
                jadwal_tabel_2  = tb_pdf_ambisi,
                zona_2          = zona_ambisi,
                header_ui_2     = header_ui_ambisi,
                level_aman_label   = f"OPSI AMAN: {data['level_aman']}",
                level_ambisi_label = f"OPSI AMBISIUS: {data['level']}",
            )
            label_btn = "📥 Download PDF (3 Halaman: Aman + Ambisius + Edukasi)"
        else:
            # Normal: 1 jadwal + edukasi
            pdf_bytes = buat_pdf(
                data,
                jadwal_tabel   = tabel_rapi_pdf,
                zona           = zona_pdf,
                header_ui      = header_ui_pdf,
                nama_hari_race = nama_hari_race,
            )
            label_btn = "📥 Download Jadwal PDF (2 Halaman)"

        col_dl = st.columns([1, 2, 1])
        with col_dl[1]:
            st.download_button(
                label=label_btn,
                data=pdf_bytes,
                file_name=f"RunSmart_{data['nama'].replace(' ','_')}_{data['jarak']}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except Exception as e:
        st.error(f"Gagal membuat PDF: {e}")

    # ─── PUSAT EDUKASI ───
    st.markdown("---")
    st.markdown("### 🎓 Pusat Edukasi Lari")
    with st.expander("📖 Buka Kamus Lari & Aturan Emas", expanded=False):
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📉 Tapering", "🏃 Long Run", "🔄 Stepback",
            "🚴 Cross-Training", "⏱️ Tempo", "⚡ Interval", "💡 Hard-Easy"
        ])
        with tab1:
            st.markdown("""
### Apa itu Tapering?
**Tapering** adalah fase pengurangan beban latihan menjelang hari H lomba.
- **Tujuan:** Mengisi ulang energi otot yang terkuras selama bulan latihan.
- **Durasi:** Marathon = 3 minggu | Half Marathon/10K = 1–2 minggu.
- **Tips:** Jangan panik saat tubuh terasa berat — itu normal!
            """)
        with tab2:
            st.markdown("""
### Long Run & Aturan Kecepatan
**Long Run** adalah sesi terpenting per minggu — membangun stamina dan mental.
- **Aturan Emas:** SELALU berlari **lebih lambat** dari target race pace.
- Di RunSmart, Long Run selalu dijadwalkan di hari yang sama dengan Race Day (kolom kanan).
- Naikkan jarak maksimal **10% per minggu** (10% Rule).
            """)
        with tab3:
            st.markdown("""
### Stepback / Recovery Week
Jarak tidak selalu naik — ada minggu di mana jarak **turun**. Ini adalah **Stepback**.
- **Pola umum:** Naik 3 minggu → turun 1 minggu → naik lagi.
- Ini **bukan** kemunduran — ini bagian penting dari program!
            """)
        with tab4:
            st.markdown("""
### Cross-Training
Olahraga aerobik selain lari selama 30–60 menit.
- ✅ **Boleh:** Bersepeda, renang, jalan cepat, elliptical.
- ❌ **Dilarang:** Futsal, basket, badminton — risiko keseleo mendadak.
            """)
        with tab5:
            st.markdown("""
### Lari Tempo
Bukan sprint! Tempo = lari di **ambang batas anaerobik**.
1. Pemanasan 15 menit jogging pelan.
2. Akselerasi ke race pace & tahan 5–15 menit.
3. Pendinginan 10 menit jogging pelan.
            """)
        with tab6:
            st.markdown("""
### Latihan Interval (contoh: 4×400m)
1. Pemanasan jogging 1–2 km.
2. Lari **secepat mungkin** sejauh 400m.
3. Jalan/jogging pelan 2 menit (recovery).
4. Ulangi 4 kali.
5. Pendinginan jogging 1 km.
            """)
        with tab7:
            st.markdown("""
### Prinsip Hard-Easy Days
Salah satu pilar utama metodologi Hal Higdon:
- **Setelah sesi berat** (Interval, Tempo, Long Run), WAJIB ada sesi ringan atau istirahat.
- **Tidak boleh** 2 hari berat berurutan — otot perlu 24-48 jam untuk pulih.
- **Contoh:** Selasa Interval → Rabu Easy 4.8km → Kamis Tempo → Jumat Istirahat.
            """)