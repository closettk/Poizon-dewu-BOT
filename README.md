# Poizon-dewu-BOT
Telegram бот для расчета стоимости доставки на aiogram3


https://github.com/closettk/Poizon-dewu-BOT/assets/132755051/39506d4b-e094-455f-8c0d-ea709e3da8bc

Есть вопрос/По написанию ботов пишите мне tg @benetter


В боте, помимо расчета стоимости услуг, есть функция для отправки рекламного поста всем юзерам /addpost и информации о количестве юзеров /countusers

1)В каждом файле поменяйте токен и айди на свой

2)tg.db создается сама при первом запуске

3)В thirdhandlers.py считаем кол-во активных юзеров, а также меняем курс юаня

4)В sechandlers.py создаем рекламный пост, а также отменяем любое действие /cancel
После отправки поста бот сам почистит недоступных юзеров, после чего вы можете проверить кол-во активных с помощью /countusers

5)calculator.py нужен для расчета стоимости. Здесь все меняете под себя

6)handlers.py основной файл
При первом написании /start бот высылает ссылку на ваш канал, а в следующий раз такого нет, чтобы не было спамма
