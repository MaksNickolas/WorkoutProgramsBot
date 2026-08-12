LEVELS = {
    1: {"reps": 8, "label": "Начальный"},
    2: {"reps": 12, "label": "Средний"},
    3: {"reps": 15, "label": "Продвинутый"}
}

# === КРАСИВЫЕ НАЗВАНИЯ УПРАЖНЕНИЙ (КИРИЛЛИЦА) ===
EXERCISES = {
    # === ДОМ (ПН) ===
    "ryvok_giri": "Рывок гири одной рукой",
    "tyaga_ganteli_v_naklone": "Тяга гантели в наклоне",
    "zhim_ganteley_stoya": "Жим гантелей стоя",
    "podem_na_biceps": "Подъем на бицепс с гантелями",

    # === ДОМ (ВТ) ===
    "zhim_ganteley_legha": "Жим гантелей лежа",
    "razvodka_ganteley": "Разводка гантелей",
    "armeyskiy_zhim_sidya": "Армейский жим сидя",
    "tyaga_giri_k_podborodku": "Тяга гири к подбородку",

    # === ДОМ (СР) ===
    "sgibanie_zapyastiy_sidya": "Сгибание запястий сидя",
    "obratnye_sgibaniya": "Обратные сгибания",
    "skruchivaniya_s_gantelyu_na_grudi": "Скручивания с гантелью на груди",
    "planka_s_girey_na_spine": "Планка с гирей на спине",

    # === ДОМ (ПТ) ===
    "zhim_ganteley_tolchkovyy": "Жим гантелей толчковый (швунг)",
    "tyaga_giri_dvumya_rukami_v_raznohvat": "Тяга гири двумя руками в разнохват",
    "vrascheniya_giri_melnica": "Вращения гири «Мельница»",

    # === ДОМ (СБ) ===
    "prisedaniya_s_girey_na_grudi": "Приседания с гирей на груди",
    "vypady_s_gantelyami": "Выпады с гантелями",
    "berpi_s_otzhimaniem": "Берпи с отжиманием",

    # === УЛИЦА (ПН) ===
    "podtyagivaniya_shirokim_hvatom_s_vesom": "Подтягивания широким хватом с весом (рюкзак)",
    "vyhod_siloy_na_2_ruki": "Выход силой на 2 руки",
    "avstraliyskie_podtyagivaniya": "Австралийские подтягивания (ноги на земле)",

    # === УЛИЦА (ВТ) ===
    "otzhimaniya_na_bruzyah_s_vesom": "Отжимания на брусьях с весом",
    "otzhimaniya_ot_skami_nogami_vverh": "Отжимания от скамьи ногами вверх",
    "podtyagivaniya_obratnym_hvatom": "Подтягивания обратным хватом",

    # === УЛИЦА (СР) ===
    "vzryvnye_podtyagivaniya_do_grudi": "Взрывные подтягивания (до груди)",
    "hlopkovye_otzhimaniya": "Хлопковые отжимания",
    "podem_nog_k_turniku": "Подъем ног к турнику",

    # === УЛИЦА (ПТ) ===
    "podtyagivaniya_za_golovu": "Подтягивания за голову",
    "ugolok_na_turnike": "Уголок на турнике (удержание)",
    "tyaga_nog_v_vise": "Тяга ног в висе",

    # === УЛИЦА (СБ) ===
    "krugovaya_10_20_30": "Круговая: 10 подтягиваний + 20 отжиманий + 30 приседаний",

    # === ДАЧА (ПН) ===
    "otzhimaniya_v_stoyke_u_steny": "Отжимания в стойке на руках у стены",
    "planka_na_odnoy_ruke": "Планка на одной руке",
    "prisedaniya_pistoletikom": "Приседания пистолетиком (на одной ноге)",
    "skalolaz": "Скалолаз (в упоре лежа колени к груди)",

    # === ДАЧА (ВТ) ===
    "otzhimaniya_s_uzkoy_postanovkoy": "Отжимания с узкой постановкой рук (алмазные)",
    "otzhimaniya_nogami_na_stule": "Отжимания ногами на стуле",
    "obratnye_otzhimaniya_ot_stula": "Обратные отжимания от стула",
    "supermen_progib": "Супермен (прогиб лежа)",

    # === ДАЧА (СР) ===
    "skruchivaniya_s_pryamymi_nogami": "Скручивания с прямыми ногами",
    "nozhnicy": "Ножницы (лежа)",
    "berpi_bez_pryzhka": "Берпи без прыжка",
    "beg_na_meste_s_zahlyustom": "Бег на месте с захлестом",

    # === ДАЧА (ПТ) ===
    "otzhimaniya_shirokim_hvatom_dacha": "Отжимания широким хватом",
    "bokovaya_planka": "Боковая планка",
    "vypady_nazad": "Выпады назад",

    # === ДАЧА (СБ) — ИСПРАВЛЕНО! ===
    "burpi_polnye": "Бурпи (полные)",
    "prisedaniya_sumo": "Приседания сумо",
    "planka_s_podnyatoy_nogoy": "Планка с поднятой ногой",

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
            {"id": "ryvok_giri", "sets": 5, "weight": True, "reps_per_set": 3},
            {"id": "tyaga_ganteli_v_naklone", "sets": 5, "weight": True, "reps_per_set": 5},
            {"id": "zhim_ganteley_stoya", "sets": 5, "weight": True, "reps_per_set": 5},
            {"id": "podem_na_biceps", "sets": 5, "weight": True, "reps_per_set": 8},
        ],
        "вт": [
            {"id": "zhim_ganteley_legha", "sets": 4, "weight": True, "reps_per_set": 12},
            {"id": "razvodka_ganteley", "sets": 4, "weight": True, "reps_per_set": 15},
            {"id": "armeyskiy_zhim_sidya", "sets": 4, "weight": True, "reps_per_set": 10},
            {"id": "tyaga_giri_k_podborodku", "sets": 4, "weight": True, "reps_per_set": 12},
        ],
        "ср": [
            {"id": "sgibanie_zapyastiy_sidya", "sets": 5, "weight": True, "reps_per_set": 20},
            {"id": "obratnye_sgibaniya", "sets": 5, "weight": True, "reps_per_set": 15},
            {"id": "skruchivaniya_s_gantelyu_na_grudi", "sets": 4, "weight": True, "reps_per_set": 25},
            {"id": "planka_s_girey_na_spine", "sets": 3, "weight": False, "reps_per_set": 60},
        ],
        "чт": [{"id": "otdyh_rastyazhka", "sets": 0, "weight": False}],
        "пт": [
            {"id": "zhim_ganteley_tolchkovyy", "sets": 6, "weight": True, "reps_per_set": 3},
            {"id": "tyaga_giri_dvumya_rukami_v_raznohvat", "sets": 5, "weight": True, "reps_per_set": 5},
            {"id": "vrascheniya_giri_melnica", "sets": 4, "weight": True, "reps_per_set": 6},
        ],
        "сб": [
            {"id": "prisedaniya_s_girey_na_grudi", "sets": 5, "weight": True, "reps_per_set": 20},
            {"id": "vypady_s_gantelyami", "sets": 4, "weight": True, "reps_per_set": 15},
            {"id": "berpi_s_otzhimaniem", "sets": 5, "weight": False, "reps_per_set": 10},
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "улица": {
        "пн": [
            {"id": "podtyagivaniya_shirokim_hvatom_s_vesom", "sets": 5, "weight": True, "reps_per_set": 5},
            {"id": "vyhod_siloy_na_2_ruki", "sets": 5, "weight": False, "reps_per_set": 5},
            {"id": "avstraliyskie_podtyagivaniya", "sets": 5, "weight": False, "reps_per_set": 12},
        ],
        "вт": [
            {"id": "otzhimaniya_na_bruzyah_s_vesom", "sets": 4, "weight": True, "reps_per_set": 10},
            {"id": "otzhimaniya_ot_skami_nogami_vverh", "sets": 4, "weight": False, "reps_per_set": 15},
            {"id": "podtyagivaniya_obratnym_hvatom", "sets": 4, "weight": True, "reps_per_set": 10},
        ],
        "ср": [
            {"id": "vzryvnye_podtyagivaniya_do_grudi", "sets": 6, "weight": False, "reps_per_set": 3},
            {"id": "hlopkovye_otzhimaniya", "sets": 5, "weight": False, "reps_per_set": 5},
            {"id": "podem_nog_k_turniku", "sets": 4, "weight": False, "reps_per_set": 15},
        ],
        "чт": [{"id": "otdyh", "sets": 0, "weight": False}],
        "пт": [
            {"id": "podtyagivaniya_za_golovu", "sets": 5, "weight": True, "reps_per_set": 8},
            {"id": "ugolok_na_turnike", "sets": 5, "weight": False, "reps_per_set": 20},
            {"id": "tyaga_nog_v_vise", "sets": 4, "weight": False, "reps_per_set": 20},
        ],
        "сб": [
            {"id": "krugovaya_10_20_30", "sets": 5, "weight": False, "reps_per_set": 1}
        ],
        "вс": [{"id": "aktivnyy_otdyh", "sets": 0, "weight": False}]
    },
    "дача": {
        "пн": [
            {"id": "otzhimaniya_v_stoyke_u_steny", "sets": 5, "weight": False, "reps_per_set": 20},
            {"id": "planka_na_odnoy_ruke", "sets": 3, "weight": False, "reps_per_set": 45},
            {"id": "prisedaniya_pistoletikom", "sets": 5, "weight": False, "reps_per_set": 5},
            {"id": "skalolaz", "sets": 4, "weight": False, "reps_per_set": 30},
        ],
        "вт": [
            {"id": "otzhimaniya_s_uzkoy_postanovkoy", "sets": 5, "weight": False, "reps_per_set": 15},
            {"id": "otzhimaniya_nogami_na_stule", "sets": 5, "weight": False, "reps_per_set": 20},
            {"id": "obratnye_otzhimaniya_ot_stula", "sets": 5, "weight": False, "reps_per_set": 15},
            {"id": "supermen_progib", "sets": 4, "weight": False, "reps_per_set": 20},
        ],
        "ср": [
            {"id": "skruchivaniya_s_pryamymi_nogami", "sets": 5, "weight": False, "reps_per_set": 25},
            {"id": "nozhnicy", "sets": 4, "weight": False, "reps_per_set": 30},
            {"id": "berpi_bez_pryzhka", "sets": 5, "weight": False, "reps_per_set": 15},
            {"id": "beg_na_meste_s_zahlyustom", "sets": 5, "weight": False, "reps_per_set": 60},
        ],
        "чт": [{"id": "otdyh_rastyazhka", "sets": 0, "weight": False}],
        "пт": [
            {"id": "otzhimaniya_shirokim_hvatom_dacha", "sets": 5, "weight": False, "reps_per_set": 15},
            {"id": "bokovaya_planka", "sets": 4, "weight": False, "reps_per_set": 30},
            {"id": "vypady_nazad", "sets": 5, "weight": False, "reps_per_set": 20},
        ],
        "сб": [
            {"id": "burpi_polnye", "sets": 5, "weight": False, "reps_per_set": 10},
            {"id": "prisedaniya_sumo", "sets": 5, "weight": False, "reps_per_set": 20},
            {"id": "planka_s_podnyatoy_nogoy", "sets": 4, "weight": False, "reps_per_set": 30},
        ],
        "вс": [{"id": "yoga_rastyazhka", "sets": 0, "weight": False}]
    }
}

# === ЭСПАНДЕРЫ (ТОЛЬКО РЕКОМЕНДАЦИЯ) ===
EXPANDER_RECOMMENDATION = {
    "дом": {
        "пн": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "вт": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
        "ср": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "сб": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
    },
    "улица": {
        "пн": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "вт": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
        "ср": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "сб": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
    },
    "дача": {
        "пн": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "вт": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
        "ср": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода (2 силовых + 2 объемных)",
        "пт": "💪 В конце тренировки: Эспандер 35-40 кг — 5 подходов по 6-8 раз (силовой)",
        "сб": "💪 В конце тренировки: Эспандер 35-40 кг — 4 подхода по 15-20 раз (объемный)",
    }
}


def get_exercise_name(exercise_id):
    return EXERCISES.get(exercise_id, exercise_id)


def get_expander_text(program, day):
    return EXPANDER_RECOMMENDATION.get(program, {}).get(day, "")


DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]