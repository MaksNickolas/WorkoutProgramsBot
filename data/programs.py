LEVELS = {
    1: {"reps": 8, "label": "Начальный"},
    2: {"reps": 12, "label": "Средний"},
    3: {"reps": 15, "label": "Продвинутый"}
}

# === КРАСИВЫЕ НАЗВАНИЯ УПРАЖНЕНИЙ (КИРИЛЛИЦА) ===
EXERCISES = {
    # === ДОМ (ПН - СИЛА НОГ + ВЕРХ) ===
    "prisedaniya_s_girey_na_grudi_5x5": "Приседания с гирей/гантелями на груди (5×5, тяжело)",
    "rumynskaya_tyaga_s_gantelyami": "Румынская тяга с гантелями (бицепс бедра)",
    "zhim_ganteley_stoya_5x5": "Жим гантелей стоя (5×5)",
    "tyaga_ganteli_k_poyasu": "Тяга гантели к поясу (5×5)",

    # === ДОМ (ВТ - ОБЪЕМ ГРУДИ + ПЛЕЧИ) ===
    "zhim_ganteley_legha_4x12": "Жим гантелей лежа (4×12)",
    "razvodka_ganteley_4x15": "Разводка гантелей (4×15, растяжка)",
    "armeyskiy_zhim_sidya_4x12": "Армейский жим сидя (4×12)",
    "tyaga_giri_k_podborodku_4x12": "Тяга гири к подбородку (4×12, трапеции)",

    # === ДОМ (СР - РУКИ/ПРЕСС/ПРЕДПЛЕЧЬЯ) ===
    "sgibanie_zapyastiy_5x20": "Сгибание запястий (5×20, до жжения)",
    "obratnye_sgibaniya_5x15": "Обратные сгибания (5×15)",
    "skruchivaniya_s_gantelyu_4x25": "Скручивания с гантелью (4×25)",
    "planka_s_girey_na_spine": "Планка с гирей на спине (3×60 сек)",

    # === ДОМ (ПТ - ОБЪЕМ СПИНЫ + ВЗРЫВ) ===
    "podtyagivaniya_5x8": "Подтягивания (или тяга сверху, 5×8)",
    "zhim_ganteley_tolchkovyy_6x3": "Жим гантелей толчковый (швунг, 6×3)",
    "tyaga_giri_dvumya_rukami_5x5": "Тяга гири двумя руками (5×5)",
    "melnica_s_girey_4x6": "Мельница с гирей (4×6, косые)",

    # === ДОМ (СБ - ВЫНОСЛИВОСТЬ НОГ) ===
    "prisedaniya_s_girey_5x20": "Приседания с гирей на груди (5×20, быстро)",
    "vypady_v_hodbe_s_gantelyami": "Выпады в ходьбе с гантелями (4×15, каждая нога)",
    "berpi_s_otzhimaniem_5x10": "Берпи с отжиманием (5×10)",
    "podem_na_noski_s_girey": "Подъем на носки с гирей (5×25, икры)",

    # === УЛИЦА (ПН - СИЛА НОГ + СПИНА) ===
    "prisedaniya_pistoletikom_5x5": "Приседания пистолетиком (5×5, каждая нога)",
    "vyprygivaniya_iz_priseda": "Выпрыгивания из приседа (4×10, взрыв)",
    "podtyagivaniya_shirokim_hvatom_s_vesom_5x5": "Подтягивания широким хватом с весом (5×5)",
    "vyhod_siloy_5_popytok": "Выход силой (5 попыток)",

    # === УЛИЦА (ВТ - ОБЪЕМ ГРУДИ + ПЛЕЧИ) ===
    "otzhimaniya_na_bruzyah_s_vesom_4x10": "Отжимания на брусьях с весом (4×10)",
    "otzhimaniya_nogami_vverh_4x15": "Отжимания ногами вверх (4×15)",
    "podtyagivaniya_obratnym_hvatom_4x10": "Подтягивания обратным хватом (4×10)",

    # === УЛИЦА (СР - ВЗРЫВ/ПРЕСС) ===
    "vzryvnye_podtyagivaniya_6x3": "Взрывные подтягивания (6×3)",
    "hlopkovye_otzhimaniya_5x5": "Хлопковые отжимания (5×5)",
    "podem_nog_k_turniku_4x15": "Подъем ног к турнику (4×15)",

    # === УЛИЦА (ПТ - ОБЪЕМ СПИНЫ) ===
    "podtyagivaniya_za_golovu_5x8": "Подтягивания за голову (5×8)",
    "ugolok_na_turnike_5x20sec": "Уголок на турнике (5×20 сек)",
    "tyaga_nog_v_vise_4x20": "Тяга ног в висе (4×20)",

    # === УЛИЦА (СБ - ВЫНОСЛИВОСТЬ НОГ) ===
    "krugovaya_20_10_15": "Круговая: 20 приседаний + 10 выпрыгиваний + 15 выпадов (5 кругов на время)",
    "berpi_5x10": "Берпи (5×10)",
    "zabeganiya_na_gorku": "Забегания на горку/скамью (5×30 сек)",

    # === ДАЧА (ПН - СИЛА/СТАТИКА НОГ) ===
    "prisedaniya_pistoletikom_5x5": "Приседания пистолетиком (5×5, каждая нога)",
    "prisedaniya_u_steny_3x60sec": "Приседания у стены (стульчик, 3×60 сек)",
    "planka_na_odnoy_ruke_3x45sec": "Планка на одной руке (3×45 сек)",
    "skalolaz_4x30sec": "Скалолаз (4×30 сек, колени к груди)",

    # === ДАЧА (ВТ - ОБЪЕМ ГРУДИ/ТРИЦЕПС) ===
    "almaznye_otzhimaniya_5x15": "Алмазные отжимания (5×15)",
    "otzhimaniya_nogami_na_stule_5x20": "Отжимания ногами на стуле (5×20)",
    "obratnye_otzhimaniya_ot_stula_5x15": "Обратные отжимания от стула (5×15)",
    "supermen_progib_4x20": "Супермен (прогиб лежа, 4×20)",

    # === ДАЧА (СР - ПРЕСС + ВЫНОСЛИВОСТЬ) ===
    "skruchivaniya_s_pryamymi_nogami_5x25": "Скручивания с прямыми ногами (5×25)",
    "nozhnicy_4x30sec": "Ножницы (4×30 сек)",
    "berpi_bez_pryzhka_5x12": "Берпи без прыжка (5×12)",
    "beg_na_meste_s_zahlyustom_5x1min": "Бег на месте с захлестом (5×1 мин)",

    # === ДАЧА (ПТ - ПЛЕЧИ/СПИНА) ===
    "otzhimaniya_shirokim_hvatom_5x15": "Отжимания широким хватом (5×15)",
    "bokovaya_planka_4x30sec": "Боковая планка (4×30 сек)",
    "vypady_nazad_5x20": "Выпады назад (5×20, каждая нога)",

    # === ДАЧА (СБ - ВЫНОСЛИВОСТЬ НОГ + ТАЗ) ===
    "burpi_polnye_s_pryzhkom_5x15": "Бурпи полные с прыжком (5×15)",
    "prisedaniya_sumo_s_pauzoy_5x25": "Приседания сумо с паузой внизу (5×25)",
    "planka_s_podnyatoy_nogoy_4x30sec": "Планка с поднятой ногой (4×30 сек)",
    "vyprygivaniya_iz_seda_4x12": "Выпрыгивания из седа (4×12)",

    # === ОБЩИЕ ===
    "otdyh_rastyazhka": "Отдых / Растяжка",
    "aktivnyy_otdyh": "Активный отдых",
    "yoga_rastyazhka": "Йога / Растяжка",
    "otdyh": "Отдых"
}

# === ПРОГРАММЫ ===
PROGRAMS = {
    "дом": {
        "пн": [
            {"id": "prisedaniya_s_girey_na_grudi_5x5", "sets": 5, "weight": True},
            {"id": "rumynskaya_tyaga_s_gantelyami", "sets": 4, "weight": True},
            {"id": "zhim_ganteley_stoya_5x5", "sets": 5, "weight": True},
            {"id": "tyaga_ganteli_k_poyasu", "sets": 5, "weight": True},
        ],
        "вт": [
            {"id": "zhim_ganteley_legha_4x12", "sets": 4, "weight": True},
            {"id": "razvodka_ganteley_4x15", "sets": 4, "weight": True},
            {"id": "armeyskiy_zhim_sidya_4x12", "sets": 4, "weight": True},
            {"id": "tyaga_giri_k_podborodku_4x12", "sets": 4, "weight": True},
        ],
        "ср": [
            {"id": "sgibanie_zapyastiy_5x20", "sets": 5, "weight": True},
            {"id": "obratnye_sgibaniya_5x15", "sets": 5, "weight": True},
            {"id": "skruchivaniya_s_gantelyu_4x25", "sets": 4, "weight": True},
            {"id": "planka_s_girey_na_spine", "sets": 3, "weight": False},
        ],
        "чт": [{"id": "otdyh_rastyazhka", "sets": 0, "weight": False}],
        "пт": [
            {"id": "podtyagivaniya_5x8", "sets": 5, "weight": True},
            {"id": "zhim_ganteley_tolchkovyy_6x3", "sets": 6, "weight": True},
            {"id": "tyaga_giri_dvumya_rukami_5x5", "sets": 5, "weight": True},
            {"id": "melnica_s_girey_4x6", "sets": 4, "weight": True},
        ],
        "сб": [
            {"id": "prisedaniya_s_girey_5x20", "sets": 5, "weight": True},
            {"id": "vypady_v_hodbe_s_gantelyami", "sets": 4, "weight": True},
            {"id": "berpi_s_otzhimaniem_5x10", "sets": 5, "weight": False},
            {"id": "podem_na_noski_s_girey", "sets": 5, "weight": True},
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "улица": {
        "пн": [
            {"id": "prisedaniya_pistoletikom_5x5", "sets": 5, "weight": False},
            {"id": "vyprygivaniya_iz_priseda", "sets": 4, "weight": False},
            {"id": "podtyagivaniya_shirokim_hvatom_s_vesom_5x5", "sets": 5, "weight": True},
            {"id": "vyhod_siloy_5_popytok", "sets": 5, "weight": False},
        ],
        "вт": [
            {"id": "otzhimaniya_na_bruzyah_s_vesom_4x10", "sets": 4, "weight": True},
            {"id": "otzhimaniya_nogami_vverh_4x15", "sets": 4, "weight": False},
            {"id": "podtyagivaniya_obratnym_hvatom_4x10", "sets": 4, "weight": True},
        ],
        "ср": [
            {"id": "vzryvnye_podtyagivaniya_6x3", "sets": 6, "weight": False},
            {"id": "hlopkovye_otzhimaniya_5x5", "sets": 5, "weight": False},
            {"id": "podem_nog_k_turniku_4x15", "sets": 4, "weight": False},
        ],
        "чт": [{"id": "otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"id": "podtyagivaniya_za_golovu_5x8", "sets": 5, "weight": True},
            {"id": "ugolok_na_turnike_5x20sec", "sets": 5, "weight": False},
            {"id": "tyaga_nog_v_vise_4x20", "sets": 4, "weight": False},
        ],
        "сб": [
            {"id": "krugovaya_20_10_15", "sets": 5, "weight": False},
            {"id": "berpi_5x10", "sets": 5, "weight": False},
            {"id": "zabeganiya_na_gorku", "sets": 5, "weight": False},
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "дача": {
        "пн": [
            {"id": "prisedaniya_pistoletikom_5x5", "sets": 5, "weight": False},
            {"id": "prisedaniya_u_steny_3x60sec", "sets": 3, "weight": False},
            {"id": "planka_na_odnoy_ruke_3x45sec", "sets": 3, "weight": False},
            {"id": "skalolaz_4x30sec", "sets": 4, "weight": False},
        ],
        "вт": [
            {"id": "almaznye_otzhimaniya_5x15", "sets": 5, "weight": False},
            {"id": "otzhimaniya_nogami_na_stule_5x20", "sets": 5, "weight": False},
            {"id": "obratnye_otzhimaniya_ot_stula_5x15", "sets": 5, "weight": False},
            {"id": "supermen_progib_4x20", "sets": 4, "weight": False},
        ],
        "ср": [
            {"id": "skruchivaniya_s_pryamymi_nogami_5x25", "sets": 5, "weight": False},
            {"id": "nozhnicy_4x30sec", "sets": 4, "weight": False},
            {"id": "berpi_bez_pryzhka_5x12", "sets": 5, "weight": False},
            {"id": "beg_na_meste_s_zahlyustom_5x1min", "sets": 5, "weight": False},
        ],
        "чт": [{"id": "otdyh_rastyazhka", "sets": 0, "weight": False}],
        "пт": [
            {"id": "otzhimaniya_shirokim_hvatom_5x15", "sets": 5, "weight": False},
            {"id": "bokovaya_planka_4x30sec", "sets": 4, "weight": False},
            {"id": "vypady_nazad_5x20", "sets": 5, "weight": False},
        ],
        "сб": [
            {"id": "burpi_polnye_s_pryzhkom_5x15", "sets": 5, "weight": False},
            {"id": "prisedaniya_sumo_s_pauzoy_5x25", "sets": 5, "weight": False},
            {"id": "planka_s_podnyatoy_nogoy_4x30sec", "sets": 4, "weight": False},
            {"id": "vyprygivaniya_iz_seda_4x12", "sets": 4, "weight": False},
        ],
        "вс": [{"id": "yoga_rastyazhka", "sets": 0, "weight": False}]
    }
}

# === РЕКОМЕНДАЦИЯ ПО ЭСПАНДЕРАМ (В КОНЦЕ) ===
EXPANDER_RECOMMENDATION = {
    "дом": {
        "пн": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "вт": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
        "ср": "💪 В конце: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "сб": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
    },
    "улица": {
        "пн": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "вт": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
        "ср": "💪 В конце: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "сб": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
    },
    "дача": {
        "пн": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "вт": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
        "ср": "💪 В конце: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце: Эспандер 35-40 кг — 5×6-8 (силовой)",
        "сб": "💪 В конце: Эспандер 35-40 кг — 4×15-20 (объемный)",
    }
}


def get_exercise_name(exercise_id):
    return EXERCISES.get(exercise_id, exercise_id)


def get_expander_text(program, day):
    return EXPANDER_RECOMMENDATION.get(program, {}).get(day, "")


DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]