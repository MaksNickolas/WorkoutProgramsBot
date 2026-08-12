LEVELS = {
    1: {"reps": 8, "label": "Начальный"},
    2: {"reps": 12, "label": "Средний"},
    3: {"reps": 15, "label": "Продвинутый"}
}

PROGRAMS = {
    "дом": {
        "пн": [
            {"name": "Рывок гири одной рукой", "sets": 5, "weight": True},
            {"name": "Тяга гантели в наклоне", "sets": 5, "weight": True},
            {"name": "Жим гантелей стоя", "sets": 5, "weight": True},
            {"name": "Подъем на бицепс с гантелями", "sets": 5, "weight": True},
            {"name": "Эспандер 35-40 кг (силовой)", "sets": 5, "weight": False},
        ],
        "вт": [
            {"name": "Жим гантелей лежа", "sets": 4, "weight": True},
            {"name": "Разводка гантелей", "sets": 4, "weight": True},
            {"name": "Армейский жим сидя", "sets": 4, "weight": True},
            {"name": "Тяга гири к подбородку", "sets": 4, "weight": True},
            {"name": "Эспандер 35-40 кг (объемный)", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Сгибание запястий сидя", "sets": 5, "weight": True},
            {"name": "Обратные сгибания", "sets": 5, "weight": True},
            {"name": "Скручивания с гантелью", "sets": 4, "weight": True},
            {"name": "Эспандер 35-40 кг (комбо)", "sets": 4, "weight": False},
        ],
        "чт": [{"name": "Отдых / Растяжка", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Жим гантелей толчковый", "sets": 6, "weight": True},
            {"name": "Тяга гири двумя руками", "sets": 5, "weight": True},
            {"name": "Мельница с гирей", "sets": 4, "weight": True},
            {"name": "Эспандер 35-40 кг (силовой)", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Приседания с гирей", "sets": 5, "weight": True},
            {"name": "Выпады с гантелями", "sets": 4, "weight": True},
            {"name": "Берпи с отжиманием", "sets": 5, "weight": False},
        ],
        "вс": [{"name": "Активный отдых", "sets": 0, "weight": False}]
    },
    "улица": {
        "пн": [
            {"name": "Подтягивания широким хватом", "sets": 5, "weight": True},
            {"name": "Выход силой (попытки)", "sets": 5, "weight": False},
            {"name": "Австралийские подтягивания", "sets": 5, "weight": False},
            {"name": "Эспандер 35-40 кг (силовой)", "sets": 5, "weight": False},
        ],
        "вт": [
            {"name": "Отжимания на брусьях", "sets": 4, "weight": True},
            {"name": "Отжимания ногами вверх", "sets": 4, "weight": False},
            {"name": "Подтягивания обратным хватом", "sets": 4, "weight": True},
            {"name": "Эспандер 35-40 кг (объемный)", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Взрывные подтягивания", "sets": 6, "weight": False},
            {"name": "Хлопковые отжимания", "sets": 5, "weight": False},
            {"name": "Подъем ног к турнику", "sets": 4, "weight": False},
            {"name": "Эспандер 35-40 кг (комбо)", "sets": 4, "weight": False},
        ],
        "чт": [{"name": "Отдых / Растяжка", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Подтягивания за голову", "sets": 5, "weight": True},
            {"name": "Уголок на турнике", "sets": 5, "weight": False},
            {"name": "Тяга ног в висе", "sets": 4, "weight": False},
            {"name": "Эспандер 35-40 кг (силовой)", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Круговая (10 подт+20 отж+30 присед)", "sets": 5, "weight": False}
        ],
        "вс": [{"name": "Активный отдых", "sets": 0, "weight": False}]
    },
    "дача": {
        "пн": [
            {"name": "Отжимания в стойке у стены", "sets": 5, "weight": False},
            {"name": "Планка на одной руке", "sets": 3, "weight": False},
            {"name": "Приседания пистолетиком", "sets": 5, "weight": False},
            {"name": "Скалолаз", "sets": 4, "weight": False},
        ],
        "вт": [
            {"name": "Алмазные отжимания", "sets": 5, "weight": False},
            {"name": "Отжимания ногами на стуле", "sets": 5, "weight": False},
            {"name": "Обратные отжимания", "sets": 5, "weight": False},
            {"name": "Супермен", "sets": 4, "weight": False},
        ],
        "ср": [
            {"name": "Скручивания с прямыми ногами", "sets": 5, "weight": False},
            {"name": "Ножницы", "sets": 4, "weight": False},
            {"name": "Берпи без прыжка", "sets": 5, "weight": False},
            {"name": "Бег на месте с захлестом", "sets": 5, "weight": False},
        ],
        "чт": [{"name": "Отдых / Растяжка", "sets": 0, "weight": False}],
        "пт": [
            {"name": "Отжимания широким хватом", "sets": 5, "weight": False},
            {"name": "Боковая планка", "sets": 4, "weight": False},
            {"name": "Выпады назад", "sets": 5, "weight": False},
        ],
        "сб": [
            {"name": "Бурпи (полные)", "sets": 5, "weight": False},
            {"name": "Приседания сумо", "sets": 5, "weight": False},
            {"name": "Планка с поднятой ногой", "sets": 4, "weight": False},
        ],
        "вс": [{"name": "Йога / Растяжка", "sets": 0, "weight": False}]
    }
}

DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]