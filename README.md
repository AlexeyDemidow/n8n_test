# n8n_test
Небольшой, но полный поток «контакт‑форма → обработка → запись в таблицу → уведомление → пополнение базы знаний».
 После задания вы сможете:
  - Отправить простой запрос (будто клиент заполнил форму на сайте).
  - Увидеть новую строку в Google Sheets.
  - Получить уведомление в Telegram.
  - Замечать, что база «Элитные часы» пополнилась, если клиент интересовался конкретной маркой (Rolex, Omega или Patek).
---
## Подготовка к работе
Чтобы всё работало нужно иметь в наличии апи-ключи.
### AI Агент
- Создаем нод АИ Агента
- Переходим на https://openrouter.ai/ → регистрируемся → настройки → API Keys → Create API Key<br>
- Полученный ключ вставляем в `Credential to connect with` модели
- Выбираем нужную модель
### Google Sheets
- Создаем нод Google Sheets
- В `Credential to connect with` выбираем `Create new credential`
- Входим в/создаем Google-аккаунт
### Telegram
- Через `@BotFather` сделайте бота, скопируйте токен
- Узнайте свой chat_id узнаёте у `@userinfobot`
- Создаем нод Telegram и копируем токен и chat_id в нужные поля
### Webhook URL
Для получения URL создайте Webhook нод и открыв его увидим Test URL для тестирования и Production URL для продакшена.
Один из этих URL копируем и вставляем в 
```
  curl -X POST <Webhook_URL> \
  -H "Content-Type: application/json" \
  -d '{"name":"Анна","email":"anna@mail.ru","message":"Интересует Rolex Submariner"}'
```
### Запуск
- Импортируем `test_workflow.json` и `errors_workflow.json` из архива в n8n.cloud
- Клонируйте репозиторий `git clone`
- Установите зависимости `pip install -r requirements.txt`
- Cоздайте `.env` файл и заполняем его по образцу `.env.example`
- Запустите `script.py`
