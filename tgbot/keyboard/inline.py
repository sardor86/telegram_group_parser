from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Добавить группу/канал', callback_data='add_group'))
    keyboard.insert(InlineKeyboardButton('Удалить группу/канал', callback_data='delete_group'))
    keyboard.insert(InlineKeyboardButton('Получить все группы/каналы', callback_data='get_all_group'))
    keyboard.insert(InlineKeyboardButton('Добавить ключевое слово', callback_data='add_words'))
    keyboard.insert(InlineKeyboardButton('Удалить ключевое слово', callback_data='delete_words'))
    keyboard.insert(InlineKeyboardButton('Получить все ключевые слова', callback_data='get_all_words'))
    keyboard.insert(InlineKeyboardButton('Получить все данные пользователей', callback_data='get_all_users'))

    return keyboard
