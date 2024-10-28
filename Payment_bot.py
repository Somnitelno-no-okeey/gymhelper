import hashlib
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Данные для Robokassa
MERCHANT_LOGIN = 'MERCHANT_LOGIN'  # Пример 
PASSWORD_1 = 'ПАРОЛЬ_1'  # Указан пример(Как только пройду регистрацию на robokassa заменю данные)
PAYMENT_URL = 'https://auth.robokassa.ru/Merchant/Index.aspx'  

API_TOKEN = '8012238655:AAEz1H4xz08oC7QebeAQ4Own8NdqQ19TXUQ'  
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Чтобы оплатить услугу, введи /pay")

@dp.message_handler(commands=['pay'])
async def process_payment(message: types.Message):
    amount = "100.00"  
    inv_id = "12345"  
    description = "Оплата услуги"  # Описание платежа
    signature = f"{MERCHANT_LOGIN}:{amount}:{inv_id}:{PASSWORD_1}"  
    crc = hashlib.md5(signature.encode()).hexdigest()  

    # Cсылка на оплату
    payment_link = (
        f"{PAYMENT_URL}?MerchantLogin={MERCHANT_LOGIN}"
        f"&OutSum={amount}&InvId={inv_id}&Description={description}"
        f"&SignatureValue={crc}&IsTest=1"  
    )

    await message.answer(f"Для оплаты перейдите по ссылке: {payment_link}")

# Запуск бота
if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
