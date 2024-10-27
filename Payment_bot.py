import hashlib
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Данные для Robokassa
MERCHANT_LOGIN = 'Ваш_MERCHANT_LOGIN'  # Замените на ваш Merchant Login
PASSWORD_1 = 'Ваш_ПАРОЛЬ_1'  # Замените на ваш пароль 1 для API
PAYMENT_URL = 'https://auth.robokassa.ru/Merchant/Index.aspx'  # URL для отправки платежей

# Данные для Telegram бота
API_TOKEN = '8012238655:AAEz1H4xz08oC7QebeAQ4Own8NdqQ19TXUQ'  # Замените на ваш Telegram API токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Чтобы оплатить услугу, введи /pay")

# Обработчик команды /pay для создания ссылки на оплату
@dp.message_handler(commands=['pay'])
async def process_payment(message: types.Message):
    amount = "100.00"  # Сумма платежа
    inv_id = "12345"  # Уникальный номер заказа
    description = "Оплата услуги"  # Описание платежа
    signature = f"{MERCHANT_LOGIN}:{amount}:{inv_id}:{PASSWORD_1}"  # Формируем сигнатуру
    crc = hashlib.md5(signature.encode()).hexdigest()  # Хешируем сигнатуру

    # Создаем ссылку на оплату
    payment_link = (
        f"{PAYMENT_URL}?MerchantLogin={MERCHANT_LOGIN}"
        f"&OutSum={amount}&InvId={inv_id}&Description={description}"
        f"&SignatureValue={crc}&IsTest=1"  # Используйте IsTest=0 для боевого режима
    )

    await message.answer(f"Для оплаты перейдите по ссылке: {payment_link}")

# Запуск бота
if name == '__main__':
    executor.start_polling(dp, skip_updates=True)