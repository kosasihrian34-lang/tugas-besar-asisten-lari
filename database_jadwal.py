# database_jadwal.py

hal_higdon_db = {
    "5K": {
        "Novice": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 2.4 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 2.4 km", "Minggu": "Jalan 30 menit"},
                2: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 2.8 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 2.8 km", "Minggu": "Jalan 35 menit"},
                3: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 3.2 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Jalan 40 menit"},
                4: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 3.6 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 3.6 km", "Minggu": "Jalan 45 menit"},
                5: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.0 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.0 km", "Minggu": "Jalan 50 menit"},
                6: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.4 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.4 km", "Minggu": "Jalan 55 menit"},
                7: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Jalan 60 menit"},
                8: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Istirahat atau lari/jalan", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"}
            }
        },
        "Intermediate": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "5 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 8.1 km"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Tempo 30 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari cepat 4.8 km", "Minggu": "Lari 8.1 km"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "6 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "Lari 9.7 km"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Tempo 35 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Tes 5K"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "7 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari cepat 6.4 km", "Minggu": "Lari 9.7 km"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Tempo 40 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Lari 11.3 km"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "8 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari cepat 8.1 km", "Minggu": "Lari 11.3 km"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Tempo 30 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"}
            }
        },
        "Advance": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "5 x 400 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 6.4 km", "Minggu": "Lari 60 menit"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "8 x 200 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 6.4 km", "Minggu": "Lari 65 menit"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "6 x 400 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 35 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 8.1 km", "Minggu": "Lari 70 menit"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "9 x 200 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 35 menit", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Tes 5K"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "7 x 400 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 8.1 km", "Minggu": "Lari 75 menit"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "10 x 200 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 9.7 km", "Minggu": "Lari 85 menit"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "8 x 400 m", "Rabu": "Istirahat atau lari ringan", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari cepat 9.7 km", "Minggu": "Lari 90 menit"},
                8: {"Senin": "Lari 3.2 km", "Selasa": "6 x 200 m", "Rabu": "Tempo 30 menit", "Kamis": "Istirahat atau lari ringan", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"}
            }
        },
        "Walkers": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 15 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 15 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 2.4 km", "Minggu": "Jalan 30\u201360 menit"},
                2: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 15 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 15 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 2.8 km", "Minggu": "Jalan 35\u201360 menit"},
                3: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 20 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 20 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 3.2 km", "Minggu": "Jalan 40\u201360 menit"},
                4: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 20 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 20 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 3.6 km", "Minggu": "Jalan 45\u201360 menit"},
                5: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 25 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 25 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 6.4 km", "Minggu": "Jalan 50\u201360 menit"},
                6: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 25 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 25 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 4.4 km", "Minggu": "Jalan 55\u201360 menit"},
                7: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 30 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 30 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 4.8 km", "Minggu": "Jalan 60 menit"},
                8: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 30 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 30 menit", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"}
            }
        }
    },
    "10K": {
        "Novice": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.0 km", "Rabu": "Jalan 30 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 40 menit", "Minggu": "Lari 4.8 km"},
                2: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.0 km", "Rabu": "Jalan 30 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 40 menit", "Minggu": "Lari 5.9 km"},
                3: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.0 km", "Rabu": "Jalan 35 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 50 menit", "Minggu": "Lari 6.4 km"},
                4: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Jalan 35 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 50 menit", "Minggu": "Lari 6.4 km"},
                5: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Jalan 40 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 60 menit", "Minggu": "Lari 7.3 km"},
                6: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Jalan 40 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 60 menit", "Minggu": "Lari 8.1 km"},
                7: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Jalan 45 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari/jalan 60 menit", "Minggu": "Lari 8.9 km"},
                8: {"Senin": "Istirahat atau lari/jalan", "Selasa": "Lari 4.8 km", "Rabu": "Jalan 30 menit", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lari 10 km"}
            }
        },
        "Intermediate": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "Lari 4.8 km", "Rabu": "Lari tempo 35 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 6.4 km"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "Lari 5.9 km", "Rabu": "8 x 400 m pace 5K", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 8.1 km"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "Lari 6.4 km", "Rabu": "Lari tempo 40 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 9.7 km"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "Lari 7.3 km", "Rabu": "9 x 400 m pace 5K", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "Lari tempo 45 menit", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 9.7 km"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.9 km", "Rabu": "10 x 400 m pace 5K", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 11.3 km"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari tempo 50 menit", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Latihan silang 60 menit", "Minggu": "Lari 12.9 km"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "Lari 4.8 km", "Rabu": "5 x 400 m pace 5K", "Kamis": "Lari 1.6-4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"}
            }
        },
        "Advanced": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 30 menit", "Rabu": "6 x 400 m pace 5K", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Total 8.1 km (3.2 km pace)", "Minggu": "Lari 9.7 km"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 40 menit", "Rabu": "7 x 400 m pace 5K", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Total 8.1 km (3.2 km pace)", "Minggu": "Lari 11.3 km"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 50 menit", "Rabu": "8 x 400 m pace 5K", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Total 8.1 km (4.8 km pace)", "Minggu": "Lari 12.9 km (3:1)"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 30 menit", "Rabu": "9 x 400 m pace 5K", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 50 menit", "Rabu": "10 x 400 m pace 5K", "Kamis": "Lari 9.7 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Total 9.7 km (4.8 km pace)", "Minggu": "Lari 12.9 km (3:1)"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 30 menit", "Rabu": "11 x 400 m pace 5K", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Istirahat", "Minggu": "Lomba 8K"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 60 menit", "Rabu": "12 x 400 m pace 5K", "Kamis": "Lari 9.7 km", "Jumat": "Istirahat atau Lari 4.8 km", "Sabtu": "Total 9.7 km (4.8 km pace)", "Minggu": "Lari 16.1 km (3:1)"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "Lari tempo 30 menit", "Rabu": "6 x 400 m pace 5K", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat atau Lari 1.6-4.8 km", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"}
            }
        },
        "Walkers": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 30 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 30 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 4.8 km", "Minggu": "Jalan 45-90 menit"},
                2: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 35 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 35 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 5.9 km", "Minggu": "Jalan 55-90 menit"},
                3: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 40 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 40 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 6.4 km", "Minggu": "Jalan 65-90 menit"},
                4: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 45 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 45 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 7.3 km", "Minggu": "Jalan 75-90 menit"},
                5: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 50 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 50 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 8.1 km", "Minggu": "Jalan 80-90 menit"},
                6: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 55 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 55 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 8.9 km", "Minggu": "Jalan 85-90 menit"},
                7: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 60 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 60 menit", "Jumat": "Istirahat", "Sabtu": "Jalan 9.7 km", "Minggu": "Jalan 90 menit"},
                8: {"Senin": "Istirahat atau jalan", "Selasa": "Jalan 30 menit", "Rabu": "Istirahat atau jalan", "Kamis": "Jalan 30 menit", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Jalan 10K"}
            }
        }
    },
    "Half Marathon": {
        "Novice 1": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "30 menit cross training", "Minggu": "Lari 6.4 km"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "30 menit cross training", "Minggu": "Lari 6.4 km"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 5.6 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 5.6 km", "Jumat": "Istirahat", "Sabtu": "40 menit cross training", "Minggu": "Lari 8.1 km"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 5.9 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 5.9 km", "Jumat": "Istirahat", "Sabtu": "40 menit cross training", "Minggu": "Lari 8.1 km"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "40 menit cross training", "Minggu": "Lari 9.7 km"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 3.2 km atau cross training", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 7.3 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 7.3 km", "Jumat": "Istirahat", "Sabtu": "50 menit cross training", "Minggu": "Lari 11.3 km"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 7.3 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 7.3 km", "Jumat": "Istirahat", "Sabtu": "50 menit cross training", "Minggu": "Lari 12.9 km"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "60 menit cross training", "Minggu": "Lari 14.5 km"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "60 menit cross training", "Minggu": "Lari 16.1 km"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 4.8 km atau cross training", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        },
        "Novice 2": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "60 menit cross training"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "60 menit cross training"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "60 menit cross training"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "60 menit cross training"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "60 menit cross training"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lomba 5K", "Minggu": "60 menit cross training"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "60 menit cross training"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "60 menit cross training"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lomba 10K", "Minggu": "60 menit cross training"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 17.7 km", "Minggu": "60 menit cross training"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "60 menit cross training"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 3.2 km pace", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        },
        "Intermediate 1": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "30 menit cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 6.4 km"},
                2: {"Senin": "30 menit cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km pace", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 8.1 km"},
                3: {"Senin": "40 menit cross training", "Selasa": "Lari 5.9 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 5.9 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lari 9.7 km"},
                4: {"Senin": "40 menit cross training", "Selasa": "Lari 5.9 km", "Rabu": "Lari 8.1 km pace", "Kamis": "Lari 5.9 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 11.3 km"},
                5: {"Senin": "40 menit cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 12.9 km"},
                6: {"Senin": "50 menit cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 9.7 km pace", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 7.3 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 7.3 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km pace", "Minggu": "Lari 14.5 km"},
                8: {"Senin": "50 menit cross training", "Selasa": "Lari 7.3 km", "Rabu": "Lari 11.3 km pace", "Kamis": "Lari 7.3 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 16.1 km"},
                9: {"Senin": "60 menit cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km pace", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 17.7 km"},
                11: {"Senin": "60 menit cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 19.3 km"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 6.4 km pace", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        },
        "Advanced": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "6 \u00d7 hill", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 90 menit (3/1)"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "7 \u00d7 400 m pace 5K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 90 menit"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "7 \u00d7 hill", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "8 \u00d7 400 m pace 5K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 90 menit (3/1)"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "8 \u00d7 hill", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 90 menit"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "8 \u00d7 400 m pace 5K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "4 \u00d7 800 m pace 10K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km pace", "Minggu": "Lari 1:45 (3/1)"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "3 \u00d7 1600 m race pace", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 50 menit", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 1:45"},
                9: {"Senin": "Lari 4.8 km", "Selasa": "5 \u00d7 800 m pace 10K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat atau lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 15K"},
                10: {"Senin": "Lari 4.8 km", "Selasa": "4 \u00d7 1600 m race pace", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 55 menit", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 2:00 (3/1)"},
                11: {"Senin": "Lari 4.8 km", "Selasa": "6 \u00d7 800 m pace 10K", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 60 menit", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km pace", "Minggu": "Lari 2:00"},
                12: {"Senin": "Lari 4.8 km", "Selasa": "6 \u00d7 400 m pace 5K", "Rabu": "Lari 3.2 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        },
        "HM3": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "30 menit cross training", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "30 menit cross training"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "35 menit cross training", "Kamis": "30 menit tempo", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "35 menit cross training"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "40 menit cross training", "Kamis": "Lari 4.8 km pace", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "40 menit cross training"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "45 menit cross training", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "45 menit cross training"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "50 menit cross training", "Kamis": "40 menit tempo", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "50 menit cross training"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "30 menit cross training", "Kamis": "Lari 4.8 km pace", "Jumat": "Istirahat / lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 9.7 km", "Rabu": "50 menit cross training", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "50 menit cross training"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 9.7 km", "Rabu": "50 menit cross training", "Kamis": "50 menit tempo", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "50 menit cross training"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "30 menit cross training", "Kamis": "Lari 4.8 km pace", "Jumat": "Istirahat / lari ringan", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 9.7 km", "Rabu": "60 menit cross training", "Kamis": "Lari 9.7 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "60 menit cross training"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 9.7 km", "Rabu": "60 menit cross training", "Kamis": "60 menit tempo", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "60 menit cross training"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "30 menit cross training", "Kamis": "Lari 4.8 km pace", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        },
        "Walkers": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "30 menit jalan santai", "Rabu": "20 menit jalan ringan", "Kamis": "30 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "30 menit jalan ringan", "Minggu": "4.8 km jalan santai"},
                2: {"Senin": "Istirahat", "Selasa": "30 menit jalan santai", "Rabu": "20 menit jalan ringan", "Kamis": "30 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "30 menit jalan ringan", "Minggu": "4.8 km jalan santai"},
                3: {"Senin": "Istirahat", "Selasa": "35 menit jalan santai", "Rabu": "20 menit jalan ringan", "Kamis": "35 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "20 menit jalan ringan", "Minggu": "3.2 km jalan cepat"},
                4: {"Senin": "Istirahat", "Selasa": "35 menit jalan santai", "Rabu": "25 menit jalan ringan", "Kamis": "35 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "40 menit jalan ringan", "Minggu": "8.1 km jalan santai"},
                5: {"Senin": "Istirahat", "Selasa": "35 menit jalan santai", "Rabu": "25 menit jalan ringan", "Kamis": "35 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "40 menit jalan ringan", "Minggu": "9.7 km jalan santai"},
                6: {"Senin": "Istirahat", "Selasa": "40 menit jalan santai", "Rabu": "25 menit jalan ringan", "Kamis": "40 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "30 menit jalan ringan", "Minggu": "6.4 km jalan cepat"},
                7: {"Senin": "Istirahat", "Selasa": "40 menit jalan santai", "Rabu": "25 menit jalan ringan", "Kamis": "40 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "50 menit jalan ringan", "Minggu": "11.3 km jalan santai"},
                8: {"Senin": "Istirahat", "Selasa": "40 menit jalan santai", "Rabu": "25 menit jalan ringan", "Kamis": "40 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "50 menit jalan ringan", "Minggu": "12.9 km jalan santai"},
                9: {"Senin": "Istirahat", "Selasa": "45 menit jalan santai", "Rabu": "30 menit jalan ringan", "Kamis": "45 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "30 menit jalan ringan", "Minggu": "9.7 km jalan cepat"},
                10: {"Senin": "Istirahat", "Selasa": "45 menit jalan santai", "Rabu": "30 menit jalan ringan", "Kamis": "45 menit jalan santai", "Jumat": "Istirahat", "Sabtu": "60 menit jalan ringan", "Minggu": "14.5 km jalan santai"},
                11: {"Senin": "Istirahat", "Selasa": "45 menit jalan santai", "Rabu": "30 menit jalan ringan", "Kamis": "45 menit jalan santai", "Jumat": "30 menit jalan santai", "Sabtu": "60 menit jalan ringan", "Minggu": "16.1 km jalan santai"},
                12: {"Senin": "Istirahat", "Selasa": "30 menit jalan santai", "Rabu": "20 menit jalan ringan", "Kamis": "30 menit jalan ringan", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"}
            }
        }
    },
    "Marathon": {
        "Novice 1": {
            "durasi_minggu": 18,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Cross training"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Cross training"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Cross training"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "Cross training"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Cross training"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Cross training"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Cross training"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 24.1 km", "Minggu": "Cross training"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 25.7 km", "Minggu": "Cross training"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                13: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 29 km", "Minggu": "Cross training"},
                14: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 22.5 km", "Minggu": "Cross training"},
                15: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 16.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 32.2 km", "Minggu": "Cross training"},
                16: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                17: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Cross training"},
                18: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Marathon"}
            }
        },
        "Novice 2": {
            "durasi_minggu": 18,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari pace 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Cross training"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "Cross training"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari pace 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Cross training"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari pace 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 17.7 km", "Minggu": "Cross training"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari pace 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "Cross training"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari pace 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 22.5 km", "Minggu": "Cross training"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 24.1 km", "Minggu": "Cross training"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari pace 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari pace 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 27.4 km", "Minggu": "Cross training"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 29 km", "Minggu": "Cross training"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari pace 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 21 km", "Minggu": "Cross training"},
                13: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari pace 8.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 30.6 km", "Minggu": "Cross training"},
                14: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                15: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari pace 8.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 32.2 km", "Minggu": "Cross training"},
                16: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari pace 6.4 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                17: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Cross training"},
                18: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 3.2 km", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Marathon"}
            }
        },
        "Intermediate 2": {
            "durasi_minggu": 18,
            "jadwal": {
                1: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 8.1 km", "Minggu": "Lari 16.1 km"},
                2: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Lari 17.7 km"},
                3: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 12.9 km"},
                4: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 21.0 km"},
                5: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Lari 22.5 km"},
                6: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 11.3 km", "Minggu": "Lari 16.1 km"},
                7: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 12.9 km", "Minggu": "Lari 25.7 km"},
                8: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Lari 27.4 km"},
                9: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                10: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 14.5 km", "Minggu": "Lari 30.6 km"},
                11: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 16.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Lari 32.2 km"},
                12: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 19.3 km"},
                13: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 16.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                14: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Lari 19.3 km"},
                15: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 16.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                16: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari pace 6.4 km", "Minggu": "Lari 19.3 km"},
                17: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "Lari 12.9 km"},
                18: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Marathon"}
            }
        },
        "Advanced 1": {
            "durasi_minggu": 18,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "Lari 4.8 km", "Kamis": "3 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 8.1 km", "Minggu": "Lari 16.1 km"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Lari 17.7 km"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari 4.8 km", "Kamis": "4 x 800 m", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 12.9 km"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari 4.8 km", "Kamis": "4 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 21.0 km"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "Lari 11.3 km", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 35 menit", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Lari 22.5 km"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "Lari 11.3 km", "Rabu": "Lari 4.8 km", "Kamis": "5 x 800 m", "Jumat": "Istirahat", "Sabtu": "Lari pace 11.3 km", "Minggu": "Lari 16.1 km"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "Lari 12.9 km", "Rabu": "Lari 6.4 km", "Kamis": "5 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 12.9 km", "Minggu": "Lari 24.1 km"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "Lari 12.9 km", "Rabu": "Lari 6.4 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Lari 27.4 km"},
                9: {"Senin": "Lari 4.8 km", "Selasa": "Lari 14.5 km", "Rabu": "Lari 6.4 km", "Kamis": "6 x 800 m", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                10: {"Senin": "Lari 4.8 km", "Selasa": "Lari 14.5 km", "Rabu": "Lari 6.4 km", "Kamis": "6 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 14.5 km", "Minggu": "Lari 30.6 km"},
                11: {"Senin": "Lari 6.4 km", "Selasa": "Lari 16.1 km", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Lari 32.2 km"},
                12: {"Senin": "Lari 6.4 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari 8.1 km", "Kamis": "7 x 800 m", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 19.3 km"},
                13: {"Senin": "Lari 6.4 km", "Selasa": "Lari 16.1 km", "Rabu": "Lari 8.1 km", "Kamis": "7 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                14: {"Senin": "Lari 8.1 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Lari 19.3 km"},
                15: {"Senin": "Lari 8.1 km", "Selasa": "Lari 16.1 km", "Rabu": "Lari 8.1 km", "Kamis": "8 x 800 m", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                16: {"Senin": "Lari 8.1 km", "Selasa": "Lari 12.9 km", "Rabu": "Lari 8.1 km", "Kamis": "6 x hill (tanjakan)", "Jumat": "Istirahat", "Sabtu": "Lari pace 6.4 km", "Minggu": "Lari 19.3 km"},
                17: {"Senin": "Lari 6.4 km", "Selasa": "Lari 9.7 km", "Rabu": "Lari 6.4 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "Lari 12.9 km"},
                18: {"Senin": "Lari 4.8 km", "Selasa": "4 x 400 m", "Rabu": "Lari 3.2 km", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Marathon"}
            }
        },
        "Advanced 2": {
            "durasi_minggu": 18,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "3 x hill (tanjakan)", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 8.1 km", "Minggu": "Lari 16.1 km"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "Tempo 30 menit", "Rabu": "Lari 4.8 km", "Kamis": "Lari pace 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Lari 17.7 km"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "4 x 800 m", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 12.9 km"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "4 x hill (tanjakan)", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 35 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 21.0 km"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "Tempo 35 menit", "Rabu": "Lari 4.8 km", "Kamis": "Lari pace 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Lari 22.5 km"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "5 x 800 m", "Rabu": "Lari 4.8 km", "Kamis": "Tempo 35 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 11.3 km", "Minggu": "Lari 16.1 km"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "5 x hill (tanjakan)", "Rabu": "Lari 6.4 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 12.9 km", "Minggu": "Lari 25.7 km"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "Tempo 40 menit", "Rabu": "Lari 6.4 km", "Kamis": "Lari pace 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Lari 27.4 km"},
                9: {"Senin": "Lari 6.4 km", "Selasa": "6 x 800 m", "Rabu": "Lari 6.4 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                10: {"Senin": "Lari 4.8 km", "Selasa": "6 x hill (tanjakan)", "Rabu": "Lari 6.4 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 14.5 km", "Minggu": "Lari 30.6 km"},
                11: {"Senin": "Lari 6.4 km", "Selasa": "Tempo 45 menit", "Rabu": "Lari 8.1 km", "Kamis": "Lari pace 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Lari 32.2 km"},
                12: {"Senin": "Lari 6.4 km", "Selasa": "7 x 800 m", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 45 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 9.7 km", "Minggu": "Lari 19.3 km"},
                13: {"Senin": "Lari 6.4 km", "Selasa": "7 x hill (tanjakan)", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 50 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                14: {"Senin": "Lari 8.1 km", "Selasa": "Tempo 45 menit", "Rabu": "Lari 8.1 km", "Kamis": "Lari pace 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Lari 19.3 km"},
                15: {"Senin": "Lari 8.1 km", "Selasa": "8 x 800 m", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 40 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 16.1 km", "Minggu": "Lari 32.2 km"},
                16: {"Senin": "Lari 8.1 km", "Selasa": "6 x hill (tanjakan)", "Rabu": "Lari 8.1 km", "Kamis": "Tempo 30 menit", "Jumat": "Istirahat", "Sabtu": "Lari pace 6.4 km", "Minggu": "Lari 19.3 km"},
                17: {"Senin": "Lari 6.4 km", "Selasa": "Tempo 30 menit", "Rabu": "Lari 6.4 km", "Kamis": "Lari pace 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "Lari 12.9 km"},
                18: {"Senin": "Lari 4.8 km", "Selasa": "4 x 400 m", "Rabu": "Lari 4.8 km", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Marathon"}
            }
        },
        "Novice Supreme": {
            "durasi_minggu": 30,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "Lari 2.4 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "30 menit jalan"},
                2: {"Senin": "Istirahat", "Selasa": "Lari 2.4 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 5.6 km", "Minggu": "35 menit jalan"},
                3: {"Senin": "Istirahat", "Selasa": "Lari 2.4 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "40 menit jalan"},
                4: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 2.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km", "Minggu": "30 menit jalan"},
                5: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "45 menit jalan"},
                6: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 7.2 km", "Minggu": "30 menit jalan"},
                7: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "50 menit jalan"},
                8: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "30 menit jalan"},
                9: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "55 menit jalan"},
                10: {"Senin": "Istirahat", "Selasa": "Lari 3.2 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.8 km", "Minggu": "30 menit jalan"},
                11: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "60 menit jalan"},
                12: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "30 menit jalan"},
                13: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Cross training"},
                14: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 4.8 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Cross training"},
                15: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km", "Minggu": "Cross training"},
                16: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 14.5 km", "Minggu": "Cross training"},
                17: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Cross training"},
                18: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Cross training"},
                19: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                20: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 20.9 km", "Minggu": "Cross training"},
                21: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 16.1 km", "Minggu": "Cross training"},
                22: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 24.1 km", "Minggu": "Cross training"},
                23: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 25.8 km", "Minggu": "Cross training"},
                24: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                25: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 29 km", "Minggu": "Cross training"},
                26: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 14.5 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 22.5 km", "Minggu": "Cross training"},
                27: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 16.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 32.1 km", "Minggu": "Cross training"},
                28: {"Senin": "Istirahat", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 19.3 km", "Minggu": "Cross training"},
                29: {"Senin": "Istirahat", "Selasa": "Lari 6.4 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Cross training"},
                30: {"Senin": "Istirahat", "Selasa": "Lari 4.8 km", "Rabu": "Lari 6.4 km", "Kamis": "Lari 3.2 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Marathon"}
            }
        },
        "Personal Best": {
            "durasi_minggu": 30,
            "jadwal": {
                1: {"Senin": "Lari 4.8 km", "Selasa": "Lari 4.8 km", "Rabu": "3 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "30 menit tempo", "Minggu": "Lari 9.7 km"},
                2: {"Senin": "Lari 4.8 km", "Selasa": "Lari 4.8 km", "Rabu": "3 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "30 menit fartlek", "Minggu": "Lari 11.3 km"},
                3: {"Senin": "Lari 4.8 km", "Selasa": "Lari 6.4 km", "Rabu": "4 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "35 menit tempo", "Minggu": "Lari 9.7 km"},
                4: {"Senin": "Lari 4.8 km", "Selasa": "Lari 6.4 km", "Rabu": "4 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "35 menit fartlek", "Minggu": "Lari 11.3 km"},
                5: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "5 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "35 menit tempo", "Minggu": "Lari 12.9 km"},
                6: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "5 x hill", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                7: {"Senin": "Lari 4.8 km", "Selasa": "Lari 6.4 km", "Rabu": "8 x 200 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "40 menit fartlek", "Minggu": "Lari 11.3 km"},
                8: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "6 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "40 menit tempo", "Minggu": "Lari 12.9 km"},
                9: {"Senin": "Lari 4.8 km", "Selasa": "Lari 9.7 km", "Rabu": "10 x 200 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 8K"},
                10: {"Senin": "Lari 4.8 km", "Selasa": "Lari 6.4 km", "Rabu": "7 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "45 menit fartlek", "Minggu": "Lari 11.3 km"},
                11: {"Senin": "Lari 4.8 km", "Selasa": "Lari 8.1 km", "Rabu": "12 x 200 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "45 menit tempo", "Minggu": "Lari 9.7 km"},
                12: {"Senin": "Lari 4.8 km", "Selasa": "Lari 9.7 km", "Rabu": "8 x 400 m", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                13: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 12.9 km"},
                14: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 14.5 km"},
                15: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 9.7 km"},
                16: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km pace", "Minggu": "Lari 17.7 km"},
                17: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Lari 9.7 km", "Minggu": "Lari 19.3 km"},
                18: {"Senin": "Cross training", "Selasa": "Lari 4.8 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 4.8 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 15K"},
                19: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km", "Minggu": "Lari 22.5 km"},
                20: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 11.3 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 11.3 km pace", "Minggu": "Lari 24.1 km"},
                21: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km pace", "Minggu": "Lari 17.7 km"},
                22: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Lari 27.4 km"},
                23: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km pace", "Minggu": "Lari 29 km"},
                24: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                25: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 32.1 km"},
                26: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 12.9 km", "Minggu": "Lari 19.3 km"},
                27: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 12.9 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 8.1 km pace", "Minggu": "Lari 32.1 km"},
                28: {"Senin": "Cross training", "Selasa": "Lari 8.1 km", "Rabu": "Lari 9.7 km", "Kamis": "Lari 8.1 km", "Jumat": "Istirahat", "Sabtu": "Lari 6.4 km pace", "Minggu": "Lari 19.3 km"},
                29: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 8.1 km", "Kamis": "Lari 6.4 km", "Jumat": "Istirahat", "Sabtu": "Lari 4.8 km", "Minggu": "Lari 12.9 km"},
                30: {"Senin": "Cross training", "Selasa": "Lari 6.4 km", "Rabu": "Lari 6.4 km", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Lari 3.2 km", "Minggu": "Marathon"}
            }
        },
        "Senior Program": {
            "durasi_minggu": 8,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "9.7 km pace", "Rabu": "Peregangan & penguatan", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Maraton"},
                2: {"Senin": "Istirahat", "Selasa": "6.4 km pace", "Rabu": "Peregangan & penguatan", "Kamis": "12.9 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "19.3 km easy"},
                3: {"Senin": "Istirahat", "Selasa": "9.7 km easy pace", "Rabu": "Peregangan & penguatan", "Kamis": "9.7 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "32.1 km easy"},
                4: {"Senin": "Istirahat", "Selasa": "6.4 km pace", "Rabu": "Peregangan & penguatan", "Kamis": "16.1 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "19.3 km easy"},
                5: {"Senin": "Istirahat", "Selasa": "9.7 km easy pace", "Rabu": "Peregangan & penguatan", "Kamis": "9.7 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "25.8 km easy"},
                6: {"Senin": "Istirahat", "Selasa": "6.4 km pace", "Rabu": "Peregangan & penguatan", "Kamis": "12.9 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "19.3 km easy"},
                7: {"Senin": "Istirahat", "Selasa": "9.7 km easy pace", "Rabu": "Peregangan & penguatan", "Kamis": "9.7 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "22.5 km easy"},
                8: {"Senin": "Istirahat", "Selasa": "6.4 km pace", "Rabu": "Peregangan & penguatan", "Kamis": "12.9 km easy", "Jumat": "Peregangan & penguatan", "Sabtu": "Istirahat", "Minggu": "19.3 km easy"}
            }
        },
        "Marathon 3": {
            "durasi_minggu": 24,
            "jadwal": {
                1: {"Senin": "Istirahat", "Selasa": "4.8 km lari", "Rabu": "Sepeda 30 menit", "Kamis": "4.8 km pace", "Jumat": "Istirahat", "Sabtu": "9.7 km lari", "Minggu": "Cross training 60 menit"},
                2: {"Senin": "Istirahat", "Selasa": "6.4 km lari", "Rabu": "Sepeda 30 menit", "Kamis": "30 menit tempo", "Jumat": "Istirahat", "Sabtu": "11.3 km lari", "Minggu": "Cross training 60 menit"},
                3: {"Senin": "Istirahat", "Selasa": "4.8 km lari", "Rabu": "Sepeda 30 menit", "Kamis": "4.8 km lari", "Jumat": "Istirahat", "Sabtu": "8.1 km lari", "Minggu": "Cross training 60 menit"},
                4: {"Senin": "Istirahat", "Selasa": "8.1 km lari", "Rabu": "Sepeda 35 menit", "Kamis": "4.8 km pace", "Jumat": "Istirahat", "Sabtu": "14.5 km lari", "Minggu": "Cross training 65 menit"},
                5: {"Senin": "Istirahat", "Selasa": "8.1 km lari", "Rabu": "Sepeda 35 menit", "Kamis": "35 menit tempo", "Jumat": "Istirahat", "Sabtu": "16.1 km lari", "Minggu": "Cross training 65 menit"},
                6: {"Senin": "Istirahat", "Selasa": "6.4 km lari", "Rabu": "Sepeda 35 menit", "Kamis": "6.4 km lari", "Jumat": "Istirahat", "Sabtu": "12.9 km lari", "Minggu": "Cross training 65 menit"},
                7: {"Senin": "Istirahat", "Selasa": "9.7 km lari", "Rabu": "Sepeda 40 menit", "Kamis": "6.4 km pace", "Jumat": "Istirahat", "Sabtu": "19.3 km lari", "Minggu": "Cross training 70 menit"},
                8: {"Senin": "Istirahat", "Selasa": "11.3 km lari", "Rabu": "Sepeda 40 menit", "Kamis": "40 menit tempo", "Jumat": "Istirahat", "Sabtu": "20.9 km lari", "Minggu": "Cross training 70 menit"},
                9: {"Senin": "Istirahat", "Selasa": "8.1 km lari", "Rabu": "Sepeda 40 menit", "Kamis": "8.1 km lari", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                10: {"Senin": "Istirahat", "Selasa": "11.3 km lari", "Rabu": "Sepeda 45 menit", "Kamis": "6.4 km pace", "Jumat": "Istirahat", "Sabtu": "24.1 km lari", "Minggu": "Cross training 75 menit"},
                11: {"Senin": "Istirahat", "Selasa": "12.9 km lari", "Rabu": "Sepeda 45 menit", "Kamis": "45 menit tempo", "Jumat": "Istirahat", "Sabtu": "25.8 km lari", "Minggu": "Cross training 75 menit"},
                12: {"Senin": "Istirahat", "Selasa": "9.7 km lari", "Rabu": "Sepeda 45 menit", "Kamis": "9.7 km lari", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                13: {"Senin": "Istirahat", "Selasa": "12.9 km lari", "Rabu": "Sepeda 50 menit", "Kamis": "8.1 km pace", "Jumat": "Istirahat", "Sabtu": "27.4 km lari", "Minggu": "Cross training 80 menit"},
                14: {"Senin": "Istirahat", "Selasa": "14.5 km lari", "Rabu": "Sepeda 50 menit", "Kamis": "50 menit tempo", "Jumat": "Istirahat", "Sabtu": "29 km lari", "Minggu": "Cross training 80 menit"},
                15: {"Senin": "Istirahat", "Selasa": "9.7 km lari", "Rabu": "Sepeda 50 menit", "Kamis": "9.7 km lari", "Jumat": "Istirahat", "Sabtu": "20.9 km lari", "Minggu": "Cross training 80 menit"},
                16: {"Senin": "Istirahat", "Selasa": "14.5 km lari", "Rabu": "Sepeda 55 menit", "Kamis": "9.7 km pace", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Half Marathon"},
                17: {"Senin": "Istirahat", "Selasa": "16.1 km lari", "Rabu": "Sepeda 55 menit", "Kamis": "55 menit tempo", "Jumat": "Istirahat", "Sabtu": "32.1 km lari", "Minggu": "Cross training 85 menit"},
                18: {"Senin": "Istirahat", "Selasa": "11.3 km lari", "Rabu": "Sepeda 55 menit", "Kamis": "11.3 km lari", "Jumat": "Istirahat", "Sabtu": "22.5 km lari", "Minggu": "Cross training 85 menit"},
                19: {"Senin": "Istirahat", "Selasa": "16.1 km lari", "Rabu": "Sepeda 60 menit", "Kamis": "11.3 km pace", "Jumat": "Istirahat", "Sabtu": "32.1 km lari", "Minggu": "Cross training 85 menit"},
                20: {"Senin": "Istirahat", "Selasa": "12.9 km lari", "Rabu": "Sepeda 60 menit", "Kamis": "12.9 km lari", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"},
                21: {"Senin": "Istirahat", "Selasa": "16.1 km lari", "Rabu": "Sepeda 60 menit", "Kamis": "60 menit tempo", "Jumat": "Istirahat", "Sabtu": "32.1 km lari", "Minggu": "Cross training 90 menit"},
                22: {"Senin": "Istirahat", "Selasa": "9.7 km lari", "Rabu": "Sepeda 50 menit", "Kamis": "9.7 km lari", "Jumat": "Istirahat", "Sabtu": "19.3 km lari", "Minggu": "Cross training 75 menit"},
                23: {"Senin": "Istirahat", "Selasa": "6.4 km lari", "Rabu": "Sepeda 40 menit", "Kamis": "6.4 km lari", "Jumat": "Istirahat", "Sabtu": "12.9 km lari", "Minggu": "Cross training 60 menit"},
                24: {"Senin": "Istirahat", "Selasa": "8.1 km lari", "Rabu": "Sepeda 30 menit", "Kamis": "Istirahat", "Jumat": "Istirahat", "Sabtu": "1\u20133.2 km lari", "Minggu": "Maraton"}
            }
        },
        "Boston Bound": {
            "durasi_minggu": 12,
            "jadwal": {
                1: {"Senin": "4.8 km lari easy", "Selasa": "3x hill turun 1x", "Rabu": "4.8 km lari easy", "Kamis": "8.1 km tempo", "Jumat": "Istirahat", "Sabtu": "9.7 km pace", "Minggu": "1:20 (lari/jalan 3/1)"},
                2: {"Senin": "6.4 km lari easy", "Selasa": "4x800 m jog 400 m", "Rabu": "6.4 km lari easy", "Kamis": "11.3 km tempo", "Jumat": "Istirahat", "Sabtu": "11.3 km pace", "Minggu": "22.5 km lari easy"},
                3: {"Senin": "6.4 km lari easy", "Selasa": "4x hill turun 1x", "Rabu": "6.4 km lari easy", "Kamis": "11.3 km easy", "Jumat": "Istirahat", "Sabtu": "11.3 km easy", "Minggu": "1:30 (lari/jalan 3/1)"},
                4: {"Senin": "6.4 km lari easy", "Selasa": "5x800 m jog 400 m", "Rabu": "6.4 km lari easy", "Kamis": "8.1 km easy", "Jumat": "Istirahat", "Sabtu": "11.3 km pace", "Minggu": "25.8 km lari easy"},
                5: {"Senin": "6.4 km lari easy", "Selasa": "5x hill turun 2x", "Rabu": "6.4 km lari easy", "Kamis": "12.9 km tempo", "Jumat": "Istirahat", "Sabtu": "Lomba 5K", "Minggu": "1:40 (lari/jalan 3/1)"},
                6: {"Senin": "8.1 km lari easy", "Selasa": "6x800 m jog 400 m", "Rabu": "8.1 km lari easy", "Kamis": "12.9 km easy", "Jumat": "Istirahat", "Sabtu": "12.9 km pace", "Minggu": "29 km lari easy"},
                7: {"Senin": "8.1 km lari easy", "Selasa": "6x hill turun 2x", "Rabu": "8.1 km lari easy", "Kamis": "8.1 km tempo", "Jumat": "Istirahat", "Sabtu": "Lomba 10K", "Minggu": "1:50 (lari/jalan 3/1)"},
                8: {"Senin": "8.1 km lari easy", "Selasa": "7x800 m jog 400 m", "Rabu": "8.1 km lari easy", "Kamis": "12.9 km easy", "Jumat": "Istirahat", "Sabtu": "8.1 km easy", "Minggu": "32.2 km lari easy"},
                9: {"Senin": "8.1 km lari easy", "Selasa": "7x hill turun 3x", "Rabu": "8.1 km lari easy", "Kamis": "8.1 km easy", "Jumat": "Istirahat", "Sabtu": "Half Marathon", "Minggu": "2:00 (lari/jalan 3/1)"},
                10: {"Senin": "8.1 km lari easy", "Selasa": "8x800 m jog 400 m", "Rabu": "8.1 km lari easy", "Kamis": "12.9 km easy", "Jumat": "Istirahat", "Sabtu": "8.1 km pace", "Minggu": "32.2 km lari easy"},
                11: {"Senin": "8.1 km lari easy", "Selasa": "8x hill turun 3x", "Rabu": "8.1 km lari easy", "Kamis": "9.7 km tempo", "Jumat": "Istirahat", "Sabtu": "6.5 km pace", "Minggu": "19.3 km lari easy"},
                12: {"Senin": "8.1 km lari easy", "Selasa": "4x800 m jog 400 m", "Rabu": "4.8 km lari easy", "Kamis": "6.4 km easy", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "3.2 km lari easy"}
            }
        }
    },
    
    "Base_Training": {
        "Novice": {
            "durasi_minggu": 12,
            "jadwal": {
                "1": {"Senin": "Istirahat", "Selasa": "2.4 km lari", "Rabu": "4.8 km lari", "Kamis": "2.4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "2": {"Senin": "Istirahat", "Selasa": "2.4 km lari", "Rabu": "4.8 km lari", "Kamis": "2.4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "5.6 km lari"},
                "3": {"Senin": "Istirahat", "Selasa": "2.4 km lari", "Rabu": "4.8 km lari", "Kamis": "2.4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "4": {"Senin": "Istirahat", "Selasa": "3.2 km lari", "Rabu": "4.8 km lari", "Kamis": "2.4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "6.4 km lari"},
                "5": {"Senin": "Istirahat", "Selasa": "3.2 km lari", "Rabu": "4.8 km lari", "Kamis": "3.2 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "6": {"Senin": "Istirahat", "Selasa": "3.2 km lari", "Rabu": "4.8 km lari", "Kamis": "3.2 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "7.2 km lari"},
                "7": {"Senin": "Istirahat", "Selasa": "3.2 km lari", "Rabu": "4.8 km lari", "Kamis": "3.2 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "8": {"Senin": "Istirahat", "Selasa": "4 km lari", "Rabu": "4.8 km lari", "Kamis": "3.2 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "8.1 km lari"},
                "9": {"Senin": "Istirahat", "Selasa": "4 km lari", "Rabu": "4.8 km lari", "Kamis": "4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "10": {"Senin": "Istirahat", "Selasa": "4 km lari", "Rabu": "4.8 km lari", "Kamis": "4 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "8.9 km lari"},
                "11": {"Senin": "Istirahat", "Selasa": "4.8 km lari", "Rabu": "4.8 km lari", "Kamis": "4.8 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "4.8 km lari"},
                "12": {"Senin": "Istirahat", "Selasa": "4.8 km lari", "Rabu": "4.8 km lari", "Kamis": "4.8 km lari", "Jumat": "Istirahat", "Sabtu": "Jalan 30 menit", "Minggu": "9.7 km lari"}
            }
        },
        "Intermediate": {
            "durasi_minggu": 12,
            "jadwal": {
                "1": {"Senin": "4.8 km lari + kekuatan", "Selasa": "4.8 km lari", "Rabu": "3x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "30 menit tempo", "Minggu": "9.7 km lari"},
                "2": {"Senin": "4.8 km lari + kekuatan", "Selasa": "4.8 km lari", "Rabu": "3x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "30 menit fartlek", "Minggu": "11.3 km lari"},
                "3": {"Senin": "4.8 km lari + kekuatan", "Selasa": "6.4 km lari", "Rabu": "4x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "35 menit tempo", "Minggu": "9.7 km lari"},
                "4": {"Senin": "4.8 km lari + kekuatan", "Selasa": "6.4 km lari", "Rabu": "4x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "35 menit fartlek", "Minggu": "11.3 km lari"},
                "5": {"Senin": "4.8 km lari + kekuatan", "Selasa": "8.1 km lari", "Rabu": "5x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "35 menit tempo", "Minggu": "12.9 km lari"},
                "6": {"Senin": "4.8 km lari + kekuatan", "Selasa": "8.1 km lari", "Rabu": "5x hill", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                "7": {"Senin": "4.8 km lari + kekuatan", "Selasa": "6.4 km lari", "Rabu": "8x200 m", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "40 menit fartlek", "Minggu": "11.3 km lari"},
                "8": {"Senin": "4.8 km lari + kekuatan", "Selasa": "8.1 km lari", "Rabu": "6x400 m", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "40 menit tempo", "Minggu": "12.9 km lari"},
                "9": {"Senin": "4.8 km lari + kekuatan", "Selasa": "9.7 km lari", "Rabu": "10x200 m", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 8K"},
                "10": {"Senin": "4.8 km lari + kekuatan", "Selasa": "6.4 km lari", "Rabu": "7x400 m", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "45 menit fartlek", "Minggu": "11.3 km lari"},
                "11": {"Senin": "4.8 km lari + kekuatan", "Selasa": "8.1 km lari", "Rabu": "12x200 m", "Kamis": "4.8 km lari + kekuatan", "Jumat": "Istirahat", "Sabtu": "45 menit tempo", "Minggu": "12.9 km lari"},
                "12": {"Senin": "4.8 km lari + kekuatan", "Selasa": "9.7 km lari", "Rabu": "8x400 m", "Kamis": "4.8 km lari", "Jumat": "Istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"}
            }
        },
        "Advanced": {
            "durasi_minggu": 12,
            "jadwal": {
                "1": {"Senin": "4.8 km lari + kekuatan", "Selasa": "5x tanjakan", "Rabu": "4.8 km lari + peregangan", "Kamis": "40 menit tempo", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit fartlek", "Minggu": "9.7 km lari"},
                "2": {"Senin": "4.8 km lari + kekuatan", "Selasa": "6x tanjakan", "Rabu": "6.4 km lari + peregangan", "Kamis": "40 menit fartlek", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit tempo", "Minggu": "11.3 km lari"},
                "3": {"Senin": "4.8 km lari + kekuatan", "Selasa": "7x tanjakan", "Rabu": "8.1 km lari + peregangan", "Kamis": "45 menit tempo", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit fartlek", "Minggu": "12.9 km lari"},
                "4": {"Senin": "4.8 km lari + kekuatan", "Selasa": "8x tanjakan", "Rabu": "9.7 km lari + peregangan", "Kamis": "45 menit fartlek", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit tempo", "Minggu": "14.5 km lari"},
                "5": {"Senin": "4.8 km lari + kekuatan", "Selasa": "9x tanjakan", "Rabu": "4.8 km lari + peregangan", "Kamis": "30 menit tempo", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "4.8 km lari / istirahat", "Minggu": "Lomba 5K"},
                "6": {"Senin": "4.8 km lari + kekuatan", "Selasa": "10x tanjakan", "Rabu": "4.8 km lari + peregangan", "Kamis": "45 menit fartlek", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit fartlek", "Minggu": "16.1 km lari"},
                "7": {"Senin": "4.8 km lari + kekuatan", "Selasa": "16x 200 m", "Rabu": "4.8 km lari + peregangan", "Kamis": "30 menit tempo", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "4.8 km lari / istirahat", "Minggu": "Lomba 8K"},
                "8": {"Senin": "4.8 km lari + kekuatan", "Selasa": "10x 400 m", "Rabu": "4.8 km lari + peregangan", "Kamis": "45 menit fartlek", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit tempo", "Minggu": "16.1 km lari"},
                "9": {"Senin": "4.8 km lari + kekuatan", "Selasa": "16x 200 m", "Rabu": "4.8 km lari + peregangan", "Kamis": "30 menit tempo", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "4.8 km lari / istirahat", "Minggu": "Lomba 10K"},
                "10": {"Senin": "4.8 km lari + kekuatan", "Selasa": "10x 400 m", "Rabu": "4.8 km lari + peregangan", "Kamis": "45 menit fartlek", "Jumat": "4.8 km lari + kekuatan", "Sabtu": "30 menit fartlek", "Minggu": "16.1 km lari"},
                "11": {"Senin": "4.8 km lari + kekuatan", "Selasa": "16x 200 m", "Rabu": "4.8 km lari + peregangan", "Kamis": "30 menit tempo", "Jumat": "4.8 km lari / istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 5K"},
                "12": {"Senin": "4.8 km lari + kekuatan", "Selasa": "10x 400 m", "Rabu": "4.8 km lari", "Kamis": "30 menit fartlek", "Jumat": "4.8 km lari / istirahat", "Sabtu": "Istirahat", "Minggu": "Lomba 10K"}
            }
        }
    }
}
