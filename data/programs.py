LEVELS = {
    1: {"reps": 8, "label": "Начальный"},
    2: {"reps": 12, "label": "Средний"},
    3: {"reps": 15, "label": "Продвинутый"}
}

# === УПРАЖНЕНИЯ С ID И КРАСИВЫМИ НАЗВАНИЯМИ ===
EXERCISES = {
    # ДОМ
    "ryvok_giri": "Рывок гири одной рукой",
    "tyaga_ganteli": "Тяга гантели в наклоне",
    "zhim_ganteley_stoya": "Жим гантелей стоя",
    "podem_na_biceps": "Подъем на бицепс с гантелями",
    "espander_silovoy": "Эспандер 35-40 кг (силовой)",
    "zhim_ganteley_legha": "Жим гантелей лежа",
    "razvodka_ganteley": "Разводка гантелей",
    "armeyskiy_zhim": "Армейский жим сидя",
    "tyaga_giri_k_podborodku": "Тяга гири к подбородку",
    "espander_obemnyy": "Эспандер 35-40 кг (объемный)",
    "sgibanie_zapyastiy": "Сгибание запястий сидя",
    "obratnye_sgibaniya": "Обратные сгибания",
    "skruchivaniya_s_gantelyu": "Скручивания с гантелью",
    "espander_kombo": "Эспандер 35-40 кг (комбо)",
    "zhim_tolchkovyy": "Жим гантелей толчковый",
    "tyaga_giri_dvumya_rukami": "Тяга гири двумя руками",
    "melnica_s_girey": "Мельница с гирей",
    "prisedaniya_s_girey": "Приседания с гирей",
    "vypady_s_gantelyami": "Выпады с гантелями",
    "berpi_s_otzhimaniyem": "Берпи с отжиманием",

    # УЛИЦА
    "podtyagivaniya_shirokim_hvatom": "Подтягивания широким хватом",
    "vyhod_siloy": "Выход силой (попытки)",
    "avstraliyskie_podtyagivaniya": "Австралийские подтягивания",
    "otzhimaniya_na_bruzyah": "Отжимания на брусьях",
    "otzhimaniya_nogami_vverh": "Отжимания ногами вверх",
    "podtyagivaniya_obratnym_hvatom": "Подтягивания обратным хватом",
    "vzryvnye_podtyagivaniya": "Взрывные подтягивания",
    "hlopkovye_otzhimaniya": "Хлопковые отжимания",
    "podem_nog_k_turniku": "Подъем ног к турнику",
    "podtyagivaniya_za_golovu": "Подтягивания за голову",
    "ugolok_na_turnike": "Уголок на турнике",
    "tyaga_nog_v_vise": "Тяга ног в висе",
    "krugovaya_10_20_30": "Круговая (10 подт+20 отж+30 присед)",

    # ДАЧА
    "otzhimaniya_v_stoyke_u_steny": "Отжимания в стойке у стены",
    "planka_na_odnoy_ruke": "Планка на одной руке",
    "prisedaniya_pistoletikom": "Приседания пистолетиком",
    "skalolaz": "Скалолаз",
    "almaznye_otzhimaniya": "Алмазные отжимания",
    "otzhimaniya_nogami_na_stule": "Отжимания ногами на стуле",
    "obratnye_otzhimaniya": "Обратные отжимания",
    "supermen": "Супермен",
    "skruchivaniya_s_pryamymi_nogami": "Скручивания с прямыми ногами",
    "nozhnicy": "Ножницы",
    "berpi_bez_pryzhka": "Берпи без прыжка",
    "beg_na_meste_s_zahlyustom": "Бег на месте с захлестом",
    "otzhimaniya_shirokim_hvatom": "Отжимания широким хватом",
    "bokovaya_planka": "Боковая планка",
    "vypady_nazad": "Выпады назад",
    "burpi_polnye": "Бурпи (полные)",
    "prisedaniya_sumo": "Приседания сумо",
    "planka_s_podnyatoy_nogoy": "Планка с поднятой ногой",
}

# === ПРОГРАММЫ С ID УПРАЖНЕНИЙ ===
PROGRAMS = {
    "дом": {
        "пн": [
            {"id": "ryvok_giri", "sets": 5, "weight": True},
            {"id": "tyaga_ganteli", "sets": 5, "weight": True},
            {"id": "zhim_ganteley_stoya", "sets": 5, "weight": True},
            {"id": "podem_na_biceps", "sets": 5, "weight": True},
            {"id": "espander_silovoy", "sets": 5, "weight": False},
        ],
        "вт": [
            {"id": "zhim_ganteley_legha", "sets": 4, "weight": True},
            {"id": "razvodka_ganteley", "sets": 4, "weight": True},
            {"id": "armeyskiy_zhim", "sets": 4, "weight": True},
            {"id": "tyaga_giri_k_podborodku", "sets": 4, "weight": True},
            {"id": "espander_obemnyy", "sets": 4, "weight": False},
        ],
        "ср": [
            {"id": "sgibanie_zapyastiy", "sets": 5, "weight": True},
            {"id": "obratnye_sgibaniya", "sets": 5, "weight": True},
            {"id": "skruchivaniya_s_gantelyu", "sets": 4, "weight": True},
            {"id": "espander_kombo", "sets": 4, "weight": False},
        ],
        "чт": [{"id": "otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"id": "zhim_tolchkovyy", "sets": 6, "weight": True},
            {"id": "tyaga_giri_dvumya_rukami", "sets": 5, "weight": True},
            {"id": "melnica_s_girey", "sets": 4, "weight": True},
            {"id": "espander_silovoy", "sets": 5, "weight": False},
        ],
        "сб": [
            {"id": "prisedaniya_s_girey", "sets": 5, "weight": True},
            {"id": "vypady_s_gantelyami", "sets": 4, "weight": True},
            {"id": "berpi_s_otzhimaniyem", "sets": 5, "weight": False},
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "улица": {
        "пн": [
            {"id": "podtyagivaniya_shirokim_hvatom", "sets": 5, "weight": True},
            {"id": "vyhod_siloy", "sets": 5, "weight": False},
            {"id": "avstraliyskie_podtyagivaniya", "sets": 5, "weight": False},
            {"id": "espander_silovoy", "sets": 5, "weight": False},
        ],
        "вт": [
            {"id": "otzhimaniya_na_bruzyah", "sets": 4, "weight": True},
            {"id": "otzhimaniya_nogami_vverh", "sets": 4, "weight": False},
            {"id": "podtyagivaniya_obratnym_hvatom", "sets": 4, "weight": True},
            {"id": "espander_obemnyy", "sets": 4, "weight": False},
        ],
        "ср": [
            {"id": "vzryvnye_podtyagivaniya", "sets": 6, "weight": False},
            {"id": "hlopkovye_otzhimaniya", "sets": 5, "weight": False},
            {"id": "podem_nog_k_turniku", "sets": 4, "weight": False},
            {"id": "espander_kombo", "sets": 4, "weight": False},
        ],
        "чт": [{"id": "otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"id": "podtyagivaniya_za_golovu", "sets": 5, "weight": True},
            {"id": "ugolok_na_turnike", "sets": 5, "weight": False},
            {"id": "tyaga_nog_v_vise", "sets": 4, "weight": False},
            {"id": "espander_silovoy", "sets": 5, "weight": False},
        ],
        "сб": [
            {"id": "krugovaya_10_20_30", "sets": 5, "weight": False}
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "дача": {
        "пн": [
            {"id": "otzhimaniya_v_stoyke_u_steny", "sets": 5, "weight": False},
            {"id": "planka_na_odnoy_ruke", "sets": 3, "weight": False},
            {"id": "prisedaniya_pistoletikom", "sets": 5, "weight": False},
            {"id": "skalolaz", "sets": 4, "weight": False},
        ],
        "вт": [
            {"id": "almaznye_otzhimaniya", "sets": 5, "weight": False},
            {"id": "otzhimaniya_nogami_na_stule", "sets": 5, "weight": False},
            {"id": "obratnye_otzhimaniya", "sets": 5, "weight": False},
            {"id": "supermen", "sets": 4, "weight": False},
        ],
        "ср": [
            {"id": "skruchivaniya_s_pryamymi_nogami", "sets": 5, "weight": False},
            {"id": "nozhnicy", "sets": 4, "weight": False},
            {"id": "berpi_bez_pryzhka", "sets": 5, "weight": False},
            {"id": "beg_na_meste_s_zahlyustom", "sets": 5, "weight": False},
        ],
        "чт": [{"id": "otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"id": "otzhimaniya_shirokim_hvatom", "sets": 5, "weight": False},
            {"id": "bokovaya_planka", "sets": 4, "weight": False},
            {"id": "vypady_nazad", "sets": 5, "weight": False},
        ],
        "сб": [
            {"id": "burpi_polnye", "sets": 5, "weight": False},
            {"id": "prisedaniya_sumo", "sets": 5, "weight": False},
            {"id": "planka_s_podnyatoy_nogoy", "sets": 4, "weight": False},
        ],
        "вс": [{"id": "yoga_rastyazhka", "sets": 0, "weight": False}]
    }
}


# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===
def get_exercise_name(exercise_id):
    """Возвращает красивое название упражнения по ID"""
    return EXERCISES.get(exercise_id, exercise_id)


def get_exercise_id_by_name(name):
    """Возвращает ID упражнения по названию (для обратной совместимости)"""
    for key, value in EXERCISES.items():
        if value == name:
            return key
    return name


DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]