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

.stCheckbox label {
    background: var(--bg-card2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    color: var(--text-2) !important;
    transition: all 0.2s !important;
}
.stCheckbox label:hover {
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

# Bobot beban latihan per tipe sesi (untuk sorting Hard/Easy)
# Semakin tinggi = semakin berat
BOBOT_LATIHAN = {
    "interval": 10, "x 400": 10, "x 800": 10, "x 200": 9, "x hill": 8,
    "hill": 8, "tempo": 8, "fartlek": 7,
    "pace": 6, "cepat": 6,
    "long": 5,  # long run bukan "berat" tapi panjang — kita handle terpisah
    "km": 3, "lari": 3, "jalan": 2,
    "cross": 2, "cross training": 2, "sepeda": 2,
    "istirahat": 0,
}

def bobot_sesi(teks: str) -> int:
    """Hitung bobot sesi latihan berdasarkan kata kunci."""
    t = teks.lower()
    for kw, b in BOBOT_LATIHAN.items():
        if kw in t:
            return b
    return 1

def is_istirahat_murni(teks: str) -> bool:
    t = teks.lower()
    return "istirahat" in t and not any(
        x in t for x in ["lari", "km", "cross", "pace", "tempo", "jalan", "interval", "hill"]
    )

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
# SMART DAY MAPPING
# ─────────────────────────────────────────
def petakan_jadwal_ke_hari_user(
    menu_db: dict,
    hari_user: list,
    tanggal_race_day: datetime.date,
    tgl_awal_minggu: datetime.date,
    is_race_week: bool,
    jarak: str,
) -> dict:
    """
    Memetakan jadwal DB (7 hari Hal Higdon) ke hari pilihan user.

    Aturan utama:
    1. Tabel selalu tampilkan SEMUA 7 hari (Senin-Minggu), tapi hari
       yang TIDAK dipilih user otomatis = Istirahat.
    2. Kolom paling kanan = hari race_day (hari lomba). Kolom ini
       selalu berisi Long Run (atau Race Day di minggu terakhir).
    3. Sesi latihan dari DB didistribusikan ke hari-hari yang dipilih
       user (kecuali kolom race_day) dengan pola HARD-EASY alternating.
    4. Hari berat tidak pernah berurutan (kecuali terpaksa, dan hanya
       Easy+Easy yang boleh berurutan).
    5. Jumlah sesi = jumlah hari yang dipilih user; kelebihan sesi DB
       digabung (sesi ringan), kekurangan diisi Istirahat.

    Returns:
        dict {nama_hari: teks_sesi} untuk semua 7 hari.
    """

    # Hari lomba (nama hari dalam seminggu, misal "Jumat")
    nama_hari_race = NAMA_HARI_STANDAR[tanggal_race_day.weekday()]

    # Pastikan hari race ada di pilihan user (jika tidak, tetap masuk sebagai race/long run)
    hari_user_set = set(hari_user)

    # ── Ambil semua sesi dari DB ──
    # Kita pisahkan slot Long Run (biasanya "Minggu" di DB Hal Higdon)
    # dan slot-slot lain.
    semua_slot_db = {}
    for h in NAMA_HARI_STANDAR:
        semua_slot_db[h] = menu_db.get(h, "Istirahat")

    # Cari slot "Long Run" di DB — biasanya slot Minggu, atau slot terberat
    # yang mengandung kata "Long", "jarak", atau nilai km terbesar.
    def km_dari_teks(teks):
        import re
        nums = re.findall(r"(\d+(?:\.\d+)?)\s*km", teks.lower())
        return max((float(n) for n in nums), default=0.0)

    # Cari slot dengan km terbesar sebagai kandidat long run
    slot_long_run = semua_slot_db.get("Minggu", "Istirahat")
    km_max = km_dari_teks(slot_long_run)
    for h, teks in semua_slot_db.items():
        if h == "Minggu":
            continue
        km = km_dari_teks(teks)
        if km > km_max:
            km_max = km
            slot_long_run = teks

    # Kumpulkan sesi latihan (non-istirahat, non-long-run dari slot Minggu)
    sesi_latihan = []
    for h in NAMA_HARI_STANDAR:
        teks = semua_slot_db[h]
        if h == "Minggu":
            continue  # slot Minggu = long run, sudah dihandle
        if is_istirahat_murni(teks):
            continue
        sesi_latihan.append(teks)

    # ── Hasil akhir: mulai dengan semua hari = Istirahat ──
    hasil = {h: "Istirahat" for h in NAMA_HARI_STANDAR}

    # ── Kolom Race Day = Long Run atau RACE DAY ──
    if is_race_week:
        # Cari apakah DB punya slot "Lomba" / "Race"
        slot_race = None
        for h, teks in semua_slot_db.items():
            if any(x in teks.lower() for x in ["lomba", "marathon", "maraton", "race", "half marathon"]):
                slot_race = teks
                break
        hasil[nama_hari_race] = slot_race if slot_race else f"RACE DAY! {jarak}"
    else:
        hasil[nama_hari_race] = slot_long_run

    # ── Hari latihan user (kecuali race_day) ──
    hari_latihan_tersedia = [
        h for h in hari_user
        if h != nama_hari_race
    ]

    if not hari_latihan_tersedia:
        return hasil  # hanya race day yang dipilih

    n_slot = len(hari_latihan_tersedia)

    # ── Distribusi sesi ke slot yang tersedia ──
    if len(sesi_latihan) == 0:
        # Tidak ada sesi latihan di DB (jarang), isi dengan lari ringan
        for h in hari_latihan_tersedia:
            hasil[h] = "Lari ringan 3.2 km"
        return hasil

    if len(sesi_latihan) > n_slot:
        # Lebih banyak sesi dari slot: gabungkan sesi-sesi ringan
        # Pisahkan sesi berat (bobot >= 7) dan ringan (bobot < 7)
        sesi_berat = [s for s in sesi_latihan if bobot_sesi(s) >= 7]
        sesi_ringan = [s for s in sesi_latihan if bobot_sesi(s) < 7]

        # Gabungkan sesi ringan menjadi lebih sedikit
        # Maksimal satu sesi per slot tersedia
        sesi_gabung = []
        # Prioritas: ambil semua sesi berat dulu (maks n_slot-1 sisi berat)
        for s in sesi_berat[:n_slot - 1]:
            sesi_gabung.append(s)
        # Sisa slot diisi gabungan sesi ringan
        sisa_slot = n_slot - len(sesi_gabung)
        # Bagi sesi_ringan ke sisa_slot bucket
        buckets = [""] * max(sisa_slot, 1)
        for i, s in enumerate(sesi_ringan):
            b = i % max(sisa_slot, 1)
            if buckets[b]:
                buckets[b] += " + " + s
            else:
                buckets[b] = s
        for b in buckets:
            if b:
                sesi_gabung.append(b)
        # Pastikan panjang = n_slot
        sesi_gabung = sesi_gabung[:n_slot]
        while len(sesi_gabung) < n_slot:
            sesi_gabung.append("Istirahat")
        sesi_latihan_final = sesi_gabung

    elif len(sesi_latihan) < n_slot:
        # Lebih sedikit sesi dari slot: isi kekurangan dengan Istirahat
        sesi_latihan_final = sesi_latihan + ["Istirahat"] * (n_slot - len(sesi_latihan))
    else:
        sesi_latihan_final = list(sesi_latihan)

    # ── Terapkan pola HARD-EASY ──
    # Sort sesi: berat, ringan, berat, ringan, ... (alternating)
    sesi_berat_f = sorted(
        [s for s in sesi_latihan_final if bobot_sesi(s) >= 6],
        key=bobot_sesi, reverse=True
    )
    sesi_ringan_f = sorted(
        [s for s in sesi_latihan_final if bobot_sesi(s) < 6],
        key=bobot_sesi, reverse=True
    )

    # Alternating: hard, easy, hard, easy...
    sesi_alternating = []
    hi, ei = 0, 0
    for i in range(n_slot):
        if i % 2 == 0 and hi < len(sesi_berat_f):
            sesi_alternating.append(sesi_berat_f[hi])
            hi += 1
        elif ei < len(sesi_ringan_f):
            sesi_alternating.append(sesi_ringan_f[ei])
            ei += 1
        elif hi < len(sesi_berat_f):
            sesi_alternating.append(sesi_berat_f[hi])
            hi += 1
        else:
            sesi_alternating.append("Istirahat")

    # Pastikan tidak ada 2 sesi berat berturutan
    # (jika terpaksa karena semua berat, pisahkan dengan sesi ringan)
    sesi_final = list(sesi_alternating)
    for i in range(1, len(sesi_final)):
        if bobot_sesi(sesi_final[i]) >= 7 and bobot_sesi(sesi_final[i-1]) >= 7:
            # Cari sesi ringan yang belum terpakai atau swap dengan istirahat
            # Sisipkan istirahat (ubah sesi[i] jadi easy jika ada pengganti)
            # Cari index sesi ringan pertama setelah i
            swap_idx = None
            for j in range(i+1, len(sesi_final)):
                if bobot_sesi(sesi_final[j]) < 6:
                    swap_idx = j
                    break
            if swap_idx:
                sesi_final[i], sesi_final[swap_idx] = sesi_final[swap_idx], sesi_final[i]
            # else: biarkan saja (tidak ada opsi lain)

    # ── Assign ke hari user ──
    for i, h in enumerate(hari_latihan_tersedia):
        if i < len(sesi_final):
            hasil[h] = sesi_final[i]
        else:
            hasil[h] = "Istirahat"

    return hasil


# ─────────────────────────────────────────
# PDF CLASS
# ─────────────────────────────────────────
class PDFLatihan(FPDF):
    def footer(self):
        self.set_y(-13)
        self.set_font("helvetica", "I", 7)
        self.set_text_color(140, 140, 140)
        self.cell(0, 8, "RunSmart - Asisten Lari Cerdas | Metodologi Hal Higdon", align="C")

def clean_pdf_text(s):
    """Hapus karakter non-latin1."""
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
    """Potong teks agar tidak melebihi panjang maksimum."""
    t = teks.strip()
    if len(t) > maks_karakter:
        return t[:maks_karakter - 2] + ".."
    return t

def buat_pdf(data, jadwal_tabel, zona, ada_interval):
    """
    Membuat PDF jadwal latihan landscape A4.

    FIX utama:
    - Semua 7 hari selalu ditampilkan (kolom tetap 7 + kolom minggu).
    - Lebar kolom dihitung ulang dari ukuran halaman aktual.
    - Teks di setiap sel SELALU dipotong sebelum di-render (tidak pernah
      melebihi lebar sel) -> menghilangkan FPDFException.
    - Glosarium menggunakan cell() per baris (bukan multi_cell dengan
      width=0 yang bisa menyebabkan overflow jika margin salah).
    """
    # ── Setup halaman ──
    # A4 Landscape: 297 x 210 mm
    MARGIN_L = 8
    MARGIN_R = 8
    MARGIN_T = 14

    pdf = PDFLatihan(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(MARGIN_L, MARGIN_T, MARGIN_R)
    pdf.add_page()

    PAGE_W = 297  # mm landscape
    USABLE_W = PAGE_W - MARGIN_L - MARGIN_R  # ~281 mm

    # ── HEADER BANNER ──
    pdf.set_fill_color(249, 115, 22)
    pdf.rect(0, 0, PAGE_W, 22, "F")
    pdf.set_font("helvetica", "B", 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(MARGIN_L, 4)
    pdf.cell(
        USABLE_W, 8,
        clean_pdf_text(f"RUNSMART  |  Rencana: {data['level']} {data['jarak']}  |  {data['nama']}"),
        align="L"
    )
    pdf.set_font("helvetica", "", 8)
    pdf.set_xy(MARGIN_L, 13)
    pdf.cell(
        USABLE_W, 6,
        clean_pdf_text(
            f"Mulai: {data['tanggal_mulai']}   Lomba: {data['tanggal_lomba']}"
            f"   Hari Latihan: {', '.join(data['hari_terpilih'])}"
        ),
        align="L"
    )
    pdf.ln(14)

    # ── INFO ZONA TARGET ──
    pdf.set_fill_color(245, 245, 245)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 8)
    target_str = clean_pdf_text(
        f"Target Finis: {data['jam_finis']:02d}:{data['menit_finis']:02d}:{data['detik_finis']:02d}"
        f"   RP: {zona['RP']}"
        f"   Easy: {zona['Easy']}"
        f"   Tempo: {zona['Tempo']}"
        f"   Interval: {zona['Interval']}"
        f"   Long: {zona['Long']}"
    )
    pdf.cell(USABLE_W, 7, target_str, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
    pdf.ln(3)

    # ── TENTUKAN KOLOM ──
    # Selalu 7 hari + 1 kolom minggu
    if jadwal_tabel:
        kolom_hari = [k for k in jadwal_tabel[0].keys() if k != "Minggu Ke-"]
    else:
        kolom_hari = NAMA_HARI_STANDAR

    # Lebar kolom: kolom minggu lebih lebar, 7 hari dibagi rata
    LEBAR_MINGGU = 26  # mm
    LEBAR_HARI = (USABLE_W - LEBAR_MINGGU) / max(len(kolom_hari), 1)
    TINGGI_BARIS = 9

    # Hitung maks karakter yang muat di setiap sel hari
    # Helvetica 7pt: ~1.8 mm per karakter (konservatif)
    MAKS_CHAR_HARI = max(6, int(LEBAR_HARI / 1.85))
    MAKS_CHAR_MINGGU = max(6, int(LEBAR_MINGGU / 1.85))

    # ── HEADER TABEL ──
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 7)
    pdf.cell(LEBAR_MINGGU, TINGGI_BARIS, "MINGGU", border=1, align="C", fill=True)
    for h in kolom_hari:
        pdf.cell(LEBAR_HARI, TINGGI_BARIS, clean_pdf_text(h[:10].upper()), border=1, align="C", fill=True)
    pdf.ln()

    # ── ISI TABEL ──
    for idx, row in enumerate(jadwal_tabel):
        even = idx % 2 == 0
        if even:
            pdf.set_fill_color(248, 249, 252)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.set_text_color(30, 41, 59)

        # Label minggu
        minggu_raw = str(row.get("Minggu Ke-", "-")).replace("\n", " ").replace("Tapering", "Taper")
        minggu_clean = potong_teks(clean_pdf_text(minggu_raw), MAKS_CHAR_MINGGU)
        pdf.set_font("helvetica", "", 6.5)
        pdf.cell(LEBAR_MINGGU, TINGGI_BARIS, minggu_clean, border=1, align="C", fill=True)

        for hari in kolom_hari:
            teks_raw = str(row.get(hari, "-"))
            # Bersihkan emoji dan karakter khusus
            teks_clean = clean_pdf_text(
                teks_raw
                .replace("🛌 ", "").replace("🏃 ", "").replace("➖ ", "")
                .replace("🏁", "").replace("🎯 ", "").replace("📉", "")
                .replace("✅", "").replace("⬛", "")
                .replace("\n", " ").strip()
            )
            teks_potong = potong_teks(teks_clean, MAKS_CHAR_HARI)

            is_race = "RACE DAY" in teks_raw.upper() or "RACE DAY" in teks_clean.upper()
            if is_race:
                pdf.set_font("helvetica", "B", 7)
                pdf.set_text_color(200, 50, 0)
            else:
                pdf.set_font("helvetica", "", 6.5)
                pdf.set_text_color(30, 41, 59)

            pdf.cell(LEBAR_HARI, TINGGI_BARIS, teks_potong, border=1, align="C", fill=True)

        pdf.set_text_color(30, 41, 59)
        pdf.ln()

    # ── GLOSARIUM ──
    # Gunakan lebar eksplisit (USABLE_W) agar tidak overflow
    pdf.ln(3)
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8)
    pdf.cell(USABLE_W, 7, "PANDUAN & GLOSARIUM ISTILAH LATIHAN",
             border=0, new_x="LMARGIN", new_y="NEXT", fill=True, align="C")
    pdf.set_text_color(30, 41, 59)
    pdf.ln(2)

    if ada_interval:
        pdf.set_font("helvetica", "B", 7)
        interval_lines = [
            "INTERVAL (cth 4x400m):",
            "1) Pemanasan 1-2 km  2) Lari cepat sejauh instruksi",
            "3) Jalan/joging pelan 2-3 menit  4) Ulangi sesuai set  5) Pendinginan 1 km",
        ]
        for line in interval_lines:
            pdf.set_x(MARGIN_L)
            pdf.cell(USABLE_W, 4, clean_pdf_text(line), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("helvetica", "", 7)
        pdf.ln(1)

    glosarium_items = [
        ("ISTIRAHAT", "Vital untuk pemulihan otot. Tubuh bertambah kuat saat istirahat."),
        ("LARI SANTAI", "Fokus jarak. Wajib bisa berlari sambil mengobrol (Conversational Pace)."),
        ("LARI TARGET/PACE", "Berlari persis di kecepatan Race Pace (RP) Anda."),
        ("LARI TEMPO", "Latih ambang anaerobik: pemanasan -> akselerasi ke RP -> pendinginan."),
        ("LONG RUN", "Daya tahan mingguan, SELALU lebih lambat dari target race pace."),
        ("CROSS TRAINING", "Sepeda/renang 30-60 menit. DILARANG: futsal, basket (risiko keseleo)."),
        ("TAPERING", "Pengurangan beban latihan 1-3 minggu sebelum lomba."),
        ("HARD-EASY", "Sesi berat tidak pernah berurutan. Setelah latihan keras, istirahat/santai."),
    ]

    pdf.set_font("helvetica", "", 7)
    # Dua kolom glosarium untuk menghemat ruang
    half = USABLE_W / 2 - 2
    col_items = [glosarium_items[i::2] for i in range(2)]  # split jadi 2 kolom
    max_rows = max(len(c) for c in col_items)

    for row_i in range(max_rows):
        pdf.set_x(MARGIN_L)
        for col_i, col in enumerate(col_items):
            if row_i < len(col):
                istilah, arti = col[row_i]
                baris = f"  {istilah}: {arti}"
                baris_clean = potong_teks(clean_pdf_text(baris), int(half / 1.65))
                pdf.set_font("helvetica", "B", 7)
                # Hanya cetak istilah bold
                istilah_clean = potong_teks(clean_pdf_text(f"  {istilah}: "), 20)
                pdf.cell(len(istilah_clean) * 1.65, 4, istilah_clean)
                pdf.set_font("helvetica", "", 7)
                arti_clean = potong_teks(clean_pdf_text(arti), int(half / 1.65) - 20)
                pdf.cell(half - len(istilah_clean) * 1.65, 4, arti_clean)
            else:
                pdf.cell(half, 4, "")
        pdf.ln()

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
        <span class="stat-badge">📄 Export PDF</span>
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

        jarak_km = jarak_ke_km[jarak_target]
        ez_sec_tmp = (ez_m * 60) + ez_s
        rp_sec_tmp = ez_sec_tmp - 70
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
        jam_finis    = cj.number_input("Jam",   min_value=0, max_value=10, value=0)
        menit_finis  = cm.number_input("Menit", min_value=0, max_value=59, value=25)
        detik_finis  = cs.number_input("Detik", min_value=0, max_value=59, value=0)

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

    # ─── HARI LATIHAN ───
    st.markdown("### 📅 Pilih Hari Latihan Anda")
    st.markdown(
        "<p style='color:var(--text-2);font-size:0.88rem;margin-bottom:4px;'>"
        "Centang hari-hari yang bisa digunakan untuk berlatih. "
        "Hari yang tidak dipilih otomatis menjadi Istirahat.</p>"
        "<p style='color:#fdba74;font-size:0.82rem;margin-bottom:12px;'>"
        "💡 Hari lomba (Race Day) akan selalu tampil di kolom paling kanan jadwal. "
        "Long Run selalu dijadwalkan di hari yang sama dengan Race Day.</p>",
        unsafe_allow_html=True
    )

    col_hari = st.columns(7)
    hari_terpilih = []
    default_hari = [True, True, False, True, False, True, True]
    for i, hari in enumerate(NAMA_HARI_STANDAR):
        with col_hari[i]:
            if st.checkbox(hari, value=default_hari[i], key=f"hari_{i}"):
                hari_terpilih.append(hari)

    if len(hari_terpilih) < 3:
        st.warning("⚠️ Disarankan memilih minimal 3 hari latihan per minggu untuk hasil optimal.")

    st.markdown("---")

    st.markdown("### 🗓️ Kalender Program")
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

    sisa_hari  = (tanggal_lomba - tanggal_mulai).days
    sisa_waktu = max(1, (sisa_hari // 7) + 1)
    durasi_str = format_durasi(sisa_hari)

    # Tampilkan hari race day
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
                    &nbsp;·&nbsp; Race Day jatuh pada: <strong style="color:#fdba74;">{nama_hari_lomba_str}</strong>
                    &nbsp;·&nbsp; Kolom {nama_hari_lomba_str} = Long Run &amp; Race Day
                </div>
            </div>
        </div>""",
        unsafe_allow_html=True
    )

    # Peringatan jika hari lomba tidak ada di hari terpilih
    if nama_hari_lomba_str not in hari_terpilih:
        st.info(
            f"ℹ️ Hari lomba ({nama_hari_lomba_str}) tidak ada di hari latihan yang Anda pilih. "
            f"Sistem tetap menampilkan kolom {nama_hari_lomba_str} sebagai Race Day & Long Run."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col_btn = st.columns([1, 2, 1])
    with col_btn[1]:
        tombol = st.button("🔍 Analisis & Hasilkan Jadwal Saya", use_container_width=True)

    if tombol:
        if not nama.strip():
            st.error("❌ Nama lengkap harus diisi!")
            st.stop()
        if len(hari_terpilih) == 0:
            st.error("❌ Pilih minimal 1 hari latihan!")
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

        level_final  = base_level
        resiko_ditemukan = False
        rp_sec_aman  = rp_sec
        level_aman   = base_level

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
            pesan_peringatan += f"⚠️ **RISIKO OVERTRAINING:** Pace ambisius tapi frekuensi latihan minim. "
            resiko_ditemukan  = True
            opsi_aman = [k for k in level_tersedia if "Novice" in k]
            level_aman = opsi_aman[-1] if opsi_aman else level_tersedia[0]
            if rp_sec_aman < 420:
                rp_sec_aman = 420
        elif rp_sec <= 270 and speedwork == "Tidak tahu":
            pesan_peringatan += f"⚠️ **RISIKO TEKNIS:** Pace elite butuh adaptasi interval yang belum dimiliki. "
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
        jam_finis    = int(total_detik_baru // 3600)
        menit_finis  = int((total_detik_baru % 3600) // 60)
        detik_finis  = int(total_detik_baru % 60)

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
            "hari_terpilih": hari_terpilih,
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

    nama_hari_race = NAMA_HARI_STANDAR[
        datetime.datetime.strptime(data["tanggal_lomba"], "%Y-%m-%d").date().weekday()
    ]

    st.markdown(f"""
    <h1>JADWAL LATIHAN</h1>
    <p class="hero-subtitle">Program untuk {data['nama']} · {data['jarak']} · {data['level']}</p>
    <div style="margin-bottom:24px;">
        <span class="stat-badge">📅 {data['durasi_str']}</span>
        <span class="stat-badge">🏁 Lomba {data['tanggal_lomba']} ({nama_hari_race})</span>
        <span class="stat-badge">📌 Hari Latihan: {', '.join(data['hari_terpilih'])}</span>
        <span class="stat-badge">🏃 Long Run = kolom {nama_hari_race}</span>
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
        c2.metric("Long Run", zona["Long_Aman"])
        c3.metric("Tempo", zona["Tempo"])
        c4.metric("Interval", zona["Interval"])
        return zona

    # ─────────────────────────────────────────
    # GENERATOR TABEL JADWAL
    # ─────────────────────────────────────────
    def generate_full_table(target_level, target_rp_sec):
        """
        Menghasilkan tabel jadwal dengan kolom tetap 7 hari (Senin-Minggu).
        Kolom hari race_day selalu berada di POSISI PALING KANAN dalam
        tampilan tabel (diurutkan ulang).

        Hari yang tidak dipilih user = Istirahat.
        Long Run selalu ada di kolom hari race_day.
        """
        jarak        = data["jarak"]
        sisa_waktu   = data["sisa_waktu"]
        hari_user    = data["hari_terpilih"]  # hari yang dipilih user

        tanggal_lomba = datetime.datetime.strptime(data["tanggal_lomba"], "%Y-%m-%d").date()
        tanggal_mulai = datetime.datetime.strptime(data["tanggal_mulai"], "%Y-%m-%d").date()
        nama_hari_race_day = NAMA_HARI_STANDAR[tanggal_lomba.weekday()]

        # Urutan kolom: semua 7 hari, tapi race_day dipindah ke paling kanan
        kolom_urut = [h for h in NAMA_HARI_STANDAR if h != nama_hari_race_day] + [nama_hari_race_day]

        durasi_ideal  = hal_higdon_db[jarak][target_level]["durasi_minggu"]
        jadwal_mentah = hal_higdon_db[jarak][target_level]["jadwal"]
        jadwal_terpilih = {}

        base_level_str = "Novice"
        if "Intermediate" in target_level:
            base_level_str = "Intermediate"
        elif "Advance" in target_level or "Advanced" in target_level:
            base_level_str = "Advanced"

        # Pilih minggu-minggu yang dipakai
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

            # Hitung tanggal
            tgl_race_minggu = tanggal_lomba - datetime.timedelta(days=(minggu_terakhir - m) * 7)
            # Awal minggu = 6 hari sebelum tanggal race di minggu ini
            # (race day bisa hari apapun, bukan harus Minggu)
            tgl_awal_minggu = tgl_race_minggu - datetime.timedelta(days=6)

            label_ui  = f"M-{m}\n{tgl_awal_minggu.strftime('%d %b')} –\n{tgl_race_minggu.strftime('%d %b')}"
            label_pdf = f"M-{m} | {tgl_awal_minggu.strftime('%d %b')} - {tgl_race_minggu.strftime('%d %b')}"
            if is_taper:
                label_ui  += "\n(Taper)"
                label_pdf += " (Taper)"

            # ── Petakan jadwal DB ke hari user ──
            konten_per_hari = petakan_jadwal_ke_hari_user(
                menu_db=menu_db,
                hari_user=hari_user,
                tanggal_race_day=tanggal_lomba,
                tgl_awal_minggu=tgl_awal_minggu,
                is_race_week=is_race_week,
                jarak=jarak,
            )

            baris_ui  = {"Minggu Ke-": label_ui}
            baris_pdf = {"Minggu Ke-": label_pdf}

            # Bangun baris dengan urutan kolom yang benar (race_day di kanan)
            for hari_kolom in kolom_urut:
                # Hitung tanggal hari ini dalam minggu
                idx_standar = NAMA_HARI_STANDAR.index(hari_kolom)
                tgl_hari    = tgl_awal_minggu + datetime.timedelta(days=idx_standar)

                if tgl_hari < tanggal_mulai:
                    teks_ui  = "➖ Blm Mulai"
                    teks_pdf = "- Blm Mulai"
                elif tgl_hari > tanggal_lomba:
                    teks_ui  = "🏁 Selesai"
                    teks_pdf = "Selesai"
                elif tgl_hari == tanggal_lomba:
                    teks_ui  = f"🎯 RACE DAY!\n{jarak}"
                    teks_pdf = f"RACE DAY! {jarak}"
                else:
                    menu = konten_per_hari.get(hari_kolom, "Istirahat")
                    if is_istirahat_murni(menu):
                        teks_ui  = f"🛌 {menu}"
                        teks_pdf = menu
                    elif any(x in menu.lower() for x in ["km", "tempo", "interval", "hill", "pace"]):
                        teks_ui  = f"🏃 {menu}"
                        teks_pdf = menu
                    else:
                        teks_ui  = menu
                        teks_pdf = menu

                baris_ui[hari_kolom]  = teks_ui
                baris_pdf[hari_kolom] = teks_pdf

            tabel_ui.append(baris_ui)
            tabel_pdf.append(baris_pdf)

        return tabel_ui, tabel_pdf

    # ─── RENDER ───
    if data.get("resiko_ditemukan"):
        st.info("⚠️ **Mode Dual-Track:** 2 opsi jadwal untuk dipertimbangkan.")

        st.markdown("### 🛡️ Opsi 1 – Jadwal Rekomendasi Aman")
        st.success(f"Program: **{data['level_aman']}** | Race Pace: **{format_waktu(data['rp_sec_aman'])}/km**")
        zona_aman = render_metrik_zona(data["rp_sec_aman"])
        tb_ui_aman, tb_pdf_aman = generate_full_table(data["level_aman"], data["rp_sec_aman"])
        st.table(tb_ui_aman)

        st.markdown("---")
        st.markdown("### 🎯 Opsi 2 – Jadwal Target Ambisius (Risiko Tinggi)")
        st.error(f"Program: **{data['level']}** | Race Pace: **{format_waktu(data['rp_sec'])}/km**")
        zona_ambisi = render_metrik_zona(data["rp_sec"])
        tb_ui_ambisi, tb_pdf_ambisi = generate_full_table(data["level"], data["rp_sec"])
        st.table(tb_ui_ambisi)
        tabel_rapi_pdf, zona_pdf = tb_pdf_ambisi, zona_ambisi

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
        tb_ui_normal, tb_pdf_normal = generate_full_table(data["level"], data["rp_sec"])
        st.table(tb_ui_normal)
        tabel_rapi_pdf, zona_pdf = tb_pdf_normal, zona_normal

    # ─── LEGEND HARD-EASY ───
    st.markdown("---")
    st.markdown(
        "<p style='font-size:0.82rem;color:#94a3b8;'>"
        "🏃 = Sesi Latihan &nbsp;·&nbsp; 🛌 = Istirahat/Recovery &nbsp;·&nbsp; "
        "🎯 = Race Day &nbsp;·&nbsp; "
        "<strong style='color:#fdba74;'>Pola Hard-Easy:</strong> "
        "Sesi berat tidak pernah berurutan — setelah latihan keras selalu ada sesi ringan/istirahat. "
        f"Kolom <strong style='color:#fdba74;'>{nama_hari_race}</strong> = Long Run setiap minggu."
        "</p>",
        unsafe_allow_html=True
    )

    # ─── DOWNLOAD PDF ───
    st.markdown("---")
    try:
        pdf_bytes = buat_pdf(data, tabel_rapi_pdf, zona_pdf, True)
        col_dl = st.columns([1, 2, 1])
        with col_dl[1]:
            st.download_button(
                label="📥 Download Jadwal PDF",
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
            """)
        with tab2:
            st.markdown("""
### Long Run & Aturan Kecepatan
**Long Run** adalah sesi terpenting per minggu — membangun stamina dan mental.
- **Aturan Emas:** SELALU berlari **lebih lambat** dari target race pace.
- Di RunSmart, Long Run selalu dijadwalkan di hari yang sama dengan Race Day.
            """)
        with tab3:
            st.markdown("""
### Stepback / Recovery Week
Jarak tidak selalu naik — ada minggu di mana jarak **turun**. Ini adalah **Stepback**.
- **Pola umum:** Naik 3 minggu → turun 1 minggu → naik lagi.
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
- **Tidak boleh** 2 hari berat berturutan — otot perlu 24-48 jam untuk pulih.
- RunSmart secara otomatis mengatur pola ini berdasarkan hari yang Anda pilih.
- **Contoh:** Selasa Interval → Rabu Easy 4.8km → Kamis Tempo → Jumat Istirahat.
            """)