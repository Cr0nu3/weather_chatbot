from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging


################# 날씨 정보 얻어오기(API) 시작 ##############################
import requests

apikey = "e37623335f8207e2349d2f777f87ccb8" # 오픈웨어맵 사이트 가입시 받은 본인의 API 키를 넣어주세요
city = "Seoul"
lang = "kr"

full_Url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&q={city}&appid={apikey}&lang={lang}&units=metric" # 분당 60번만 가능, 하루 간격 16일치 날씨 정보 조회

response_org = requests.get(full_Url).json()
# print(response_org['list'])
print("###############################################################\n\n")
print(response_org['list'][0])
print("온도: ", response_org['list'][0]['main']['temp'])
print("최저 온도: ", response_org['list'][0]['main']['temp_min'])
print("최고 온도: ", response_org['list'][0]['main']['temp_max'])
print("습도", response_org['list'][0]['main']['humidity'])
print("날씨: ", response_org['list'][0]['weather'][0]['description'])
print("시간: ", response_org['list'][0]['dt_txt'])
print("###############################################################\n\n")

################# 날씨 정보 얻어오기(API) 끝 ##############################

accessToken = "6224809326:AAF5cUUi1uA4FYuxSSo2G-fAHlQDbHeaa1M" # 텔레그램 봇 생성시 획득한 본인의 엑세스 토큰을 넣어주세요

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def echo(update: Update, context: CallbackContext) -> None:

    text = update.message.text
    print(text)
    if '날씨' in text:
        reply = "오늘 날씨는 "+str(response_org['list'][0]['weather'][0]['description'])+" 입니다."
    elif '최고' in text:
        reply = "오늘 최고 온도는 "+str(response_org['list'][0]['main']['temp_max'])+" 도 입니다."
    elif '최저' in text:
        reply = "오늘 최저 온도는 "+str(response_org['list'][0]['main']['temp_min'])+" 도 입니다."
    elif '온도' in text:
        reply = "오늘 온도는 "+str(response_org['list'][0]['main']['temp'])+" 도 입니다."
    elif '습도' in text:
        reply = "오늘 습도는 "+str(response_org['list'][0]['main']['humidity'])+" 입니다."
    elif '안녕' in text:
        reply = "안녕하세요. 주인님!!"
    else:
        reply = "무슨말인지 못알아 들었습니다. 주인님!!"

    update.message.reply_text(reply)

updater = Updater(accessToken)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.stopPolling()
updater.start_polling()
updater.idle()