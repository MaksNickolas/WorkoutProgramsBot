LEVELS = {
    1: {"reps": 8, "label": "Начальный"},
    2: {"reps": 12, "label": "Средний"},
    3: {"reps": 15, "label": "Продвинутый"}
}

PROGRAMS = {
    "дом": {
        "пн": [
            {"name": "Ryvok_giri", "sets": 5, "weight": True},
            {"name": "Tyaga_ganteli", "sets": 5, "weight": True},
            {"name": "Zhim_ganteley_stoya", "sets": 5, "weight": True},
            {"name": "Podem_na_biceps", "sets": 5, "weight": True},
            {"name": "Espander_silovoy", "sets": 5, "weight": False},
        ],
        "вт": [
            {"name": "Zhim_ganteley_legha", "sets": 4, "weight": True},
            {"name": "Razvodka_ganteley", "sets": 4, "weight": True},
            {"name": "Armeyskiy_zhim", "sets": 4, "weight": True},
            {"name": "Tyaga_giri_k_podborodku", "sets": 4, "weight": True},
            {"name": "Espander_obemnyy", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Sgibanie_zapyastiy", "sets": 5, "weight": True},
            {"name": "Obratnye_sgibaniya", "sets": 5, "weight": True},
            {"name": "Skruchivaniya_s_gantelyu", "sets": 4, "weight": True},
            {"name": "Espander_kombo", "sets": 4, "weight": False},
        ],
        "чт": [{"name": "Otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Zhim_tolchkovyy", "sets": 6, "weight": True},
            {"name": "Tyaga_giri_dvumya_rukami", "sets": 5, "weight": True},
            {"name": "Melnica_s_girey", "sets": 4, "weight": True},
            {"name": "Espander_silovoy", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Prisedaniya_s_girey", "sets": 5, "weight": True},
            {"name": "Vypady_s_gantelyami", "sets": 4, "weight": True},
            {"name": "Berpi_s_otzhimaniyem", "sets": 5, "weight": False},
        ],
        "вс": [{"name": "Aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "улица": {
        "пн": [
            {"name": "Podtyagivaniya_shirokim_hvatom", "sets": 5, "weight": True},
            {"name": "Vyhod_siloy", "sets": 5, "weight": False},
            {"name": "Avstraliyskie_podtyagivaniya", "sets": 5, "weight": False},
            {"name": "Espander_silovoy", "sets": 5, "weight": False},
        ],
        "вт": [
            {"name": "Otzhimaniya_na_bruzyah", "sets": 4, "weight": True},
            {"name": "Otzhimaniya_nogami_vverh", "sets": 4, "weight": False},
            {"name": "Podtyagivaniya_obratnym_hvatom", "sets": 4, "weight": True},
            {"name": "Espander_obemnyy", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Vzryvnye_podtyagivaniya", "sets": 6, "weight": False},
            {"name": "Hlopkovye_otzhimaniya", "sets": 5, "weight": False},
            {"name": "Podem_nog_k_turniku", "sets": 4, "weight": False},
            {"name": "Espander_kombo", "sets": 4, "weight": False},
        ],
        "чт": [{"name": "Otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Podtyagivaniya_za_golovu", "sets": 5, "weight": True},
            {"name": "Ugolok_na_turnike", "sets": 5, "weight": False},
            {"name": "Tyaga_nog_v_vise", "sets": 4, "weight": False},
            {"name": "Espander_silovoy", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Krugovaya_10_20_30", "sets": 5, "weight": False}
        ],
        "вс": [{"name": "Aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "дача": {
        "пн": [
            {"name": "Otzhimaniya_v_stoyke_u_steny", "sets": 5, "weight": False},
            {"name": "Planka_na_odnoy_ruke", "sets": 3, "weight": False},
            {"name": "Prisedaniya_pistoletikom", "sets": 5, "weight": False},
            {"name": "Skalolaz", "sets": 4, "weight": False},
        ],
        "вт": [
            {"name": "Almaznye_otzhimaniya", "sets": 5, "weight": False},
            {"name": "Otzhimaniya_nogami_na_stule", "sets": 5, "weight": False},
            {"name": "Obratnye_otzhimaniya", "sets": 5, "weight": False},
            {"name": "Supermen", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Skruchivaniya_s_pryamymi_nogami", "sets": 5, "weight": False},
            {"name": "Nozhnicy", "sets": 4, "weight": False},
            {"name": "Berpi_bez_pryzhka", "sets": 5, "weight": False},
            {"name": "Beg_na_meste_s_zahlyustom", "sets": 5, "weight": False},
        ],
        "чт": [{"name": "Otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Otzhimaniya_shirokim_hvatom", "sets": 5, "weight": False},
            {"name": "Bokovaya_planka", "sets": 4, "weight": False},
            {"name": "Vypady_nazad", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Burpi_polnye", "sets": 5, "weight": False},
            {"name": "Prisedaniya_sumo", "sets": 5, "weight": False},
            {"name": "Planka_s_podnyatoy_nogoy", "sets": 4, "weight": False},
        ],
        "вс": [{"name": "Yoga_rastyazhka", "sets": 0, "weight": False}]
    }
}

DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]