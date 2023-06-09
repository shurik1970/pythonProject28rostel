                           
# **Итоговый проект по автоматизации тестирования.**

## [Объект тестирования: сайт "Ростелеком"]([https://b2c.passport.rt.ru)]

### Для тестирования сайта были использованы:

1- _разбиение на классы эквивалентности_
2- _анализ граничных значений_
3- _тестирование состояний и переходов_

#### Окружение:

Выпуск	Windows 10 Pro
Версия	22H2
Дата установки	‎10.‎08.‎2021
Сборка ОС	19045.2788
Взаимодействие	Windows Feature Experience Pack 120.2212.4190.0

### **папка pages:**
auth_page.py - распределённые по классам в зависимости от тематики тестов.
base_page.py - для получения главной страницы сайта и пути текущей страницы
config.py - Основной URL темтируемого сайта.
locators.py - ссылки на веб элементы на сайте.
setting.py - данные используемые для процесса тестирования.

##### **папка tests.**

в папке располагаются файлы с тестами с расширением py. 
тесты запускаются как с помощью консоли: pytest tests/test_выбранная папка.py
так и с помощью кнопки "RUN"

test_auth_page.py - тест позитивных сценариев аутентификации
test_negativ_auth_page.py - тест негативных сценариев аутентификации
test_new_pass.py - страница восстановления пароля
test_reg_page.py - позитивные сценарии страницы регистрации
