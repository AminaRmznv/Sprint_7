# Sprint_7

Данный проект содержит тесты для API сервиса "qa-scooter".


## Описание файлов

### Файлы конфигурации:
- `config`: содержит URL'ы для различных методов API.

### Файлы с вспомогательными функциями:
- `helper`: содержит функцию `register_new_courier_and_return_login_password` для регистрации нового курьера.

### Файлы с фикстурами:
- `conftest`: содержит фикстуру `new_courier`, которая возвращает данные о новом курьере.

### Файлы с тестами:
- `test_courier_creation`: содержит тесты, связанные с созданием курьеров.
- `test_courier_login`: содержит тесты для проверки входа курьера.
- `test_order_creation`: содержит тесты для создания заказов.
- `test_receiving_list_of_orders`: содержит тест для получения списка заказов.

### Предварительные условия

Для работы с проектом необходимо иметь установленные:

- Python 3
- Библиотеку `requests`
- Инструмент для тестирования `pytest`
- Фреймворк для генерации отчётов `allure-pytest`

### Установка

Чтобы установить необходимые зависимости, выполните:

`pip3 install -r requirements.txt` 
