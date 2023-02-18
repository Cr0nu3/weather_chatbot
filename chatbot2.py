from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import asyncio
import telegram
import datetime
import logging

now = datetime.datetime.now()
current = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

access_token = '6224809326:AAF5cUUi1uA4FYuxSSo2G-fAHlQDbHeaa1M'
apikey = "e37623335f8207e2349d2f777f87ccb8"
city = "Seoul"
lang = "kr"

# =============================  날씨 정보 알아오기   ========================================= #
# 16일치 날씨 정보 조회
full_Url =f"http://api.openweathermap.org/data/2.5/forecast?id=524901&q={city}&appid={apikey}&lang={lang}&units=metric"
res_org = requests.get(full_Url).json()

temp = res_org['list'][0]['main']['temp']
temp_min = res_org['list'][0]['main']['temp_min']
temp_max = res_org['list'][0]['main']['temp_max']
description = res_org['list'][0]['weather'][0]['description']
dt_txt = res_org['list'][0]['dt_txt']

print("##################################################################")
print(res_org['list'][0])
print("온도: ", temp)
print("최저 온도: ", temp_min)
print("최고 온도: ", temp_max)
print("날씨: ", description)
print("시간: ", dt_txt)
print("###############################################################\n\n")


######################### Telegram Bot Starter ##################################
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=access_token)
chat_id = "5776464183"

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if '날씨' in text:
        reply = "오늘 날씨는 " + str(res_org['list'][0]['weather'][0]['description']) + "입니다."
    elif '최고' in text:
        reply = "오늘 최고 온도는 " + str(temp_max) + "입니다."
    elif '최저' in text:
        reply = "오늘 최저 온도는 " + str(temp_min) + "입니다."
    else:
        reply = "알아들을 수 없는 단어가 있습니다."

    update.message.reply_text(reply)

updater = Updater(access_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()
##################### Telegram setting done ############################