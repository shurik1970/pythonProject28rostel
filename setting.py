"""Действующие данные для авторизации в системе"""
import os
import string



invalid_firstname = "JUIYJ8"
invalid_lastname = "hgjhgy67"
invalid_phone = "89991234567"
invalid_email = "VasyPupkin@mail.ru"
invalid_password = "GHk7679gjhk"
invalid_password_confirm = "GHk7679gjhk"




firstname = "Иван"
lastname = "Иванов"
valid_phone = '89513313441'
valid_login = 'login'
valid_password = 'Homework70'
valid_ls = '734092279946'
valid_email = 'sanny70@mail.ru'
valid_password_confirm = 'Homework70'


def generate_string_rus(n):
    return 'б' * n


def generate_string_en(n):
    return 'x' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'