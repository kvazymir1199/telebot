from telebot import types

button_info_1 = {
    "Расписание": 'select_day',
    "Все каталоги": 'back',
}
button_info_2 = {
    "Расписание": 'select_day',
    "Доп. уроки": 'addition_lessons',
    "Теория уроков": "theory",
    "Преподаватели": 'teachers',
    "Список учеников": 'students',
    "Интересные задачи": 'question_1',
    "Календарь учебного года": 'kalendar'
}
button_info_3 = {
    "Понедельник": "monday",
    "Вторник": "tuesday",
    "Среда": "wednesday",
    "Четверг": "thursday",
    "Пятница": "friday",
    "Назад": "back"
}
button_info_4 = {
    "Алгебра": "algebra",
    "Геометрия": "geometria",
    "Русский язык": "russian",
    "Физика": "physics",
    "Вероятность и статистика": "VS",
    "Назад": "back"
}


def create_mark_up(_object, _dict):
    for name, callback_data in _dict.items():
        _object.add(types.InlineKeyboardButton(name, callback_data=callback_data))


button_start_markup = types.InlineKeyboardMarkup()
button_catalog_markup = types.InlineKeyboardMarkup()
button_day_of_weeks_markup = types.InlineKeyboardMarkup()
button_lessons_markup = types.InlineKeyboardMarkup()

create_mark_up(button_start_markup, button_info_1)
create_mark_up(button_catalog_markup, button_info_2)
create_mark_up(button_day_of_weeks_markup, button_info_3)
create_mark_up(button_lessons_markup, button_info_4)

markup_back = types.InlineKeyboardMarkup(
    keyboard=[
        [
            types.InlineKeyboardButton("Назад", callback_data='back')
        ]
    ]
)
