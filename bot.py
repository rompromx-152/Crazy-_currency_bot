import requests
import os

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL_ID')

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
v = data['Valute']
date = data['Date'].split('T')[0]

text = f"""📅 <b>Курсы ЦБ РФ на {date}</b>

🇺🇸 USD — {v['USD']['Value']} ₽
🇪🇺 EUR — {v['EUR']['Value']} ₽
🇨🇳 CNY — {v['CNY']['Value']} ₽
🇬🇧 GBP — {v['GBP']['Value']} ₽
🇹🇷 TRY — {v['TRY']['Value']} ₽

Источник: Банк России"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={"chat_id": CHANNEL, "text": text, "parse_mode": "HTML"}
)

print("Отправлено!")
