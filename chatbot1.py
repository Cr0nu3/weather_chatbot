from telegram import Update
from multiprocessing import Queue
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

accessToken = "6224809326:AAF5cUUi1uA4FYuxSSo2G-fAHlQDbHeaa1M" # 텔레그램 봇 생성시 획득한 본인의 엑세스 토큰을 넣어주세요

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if '안녕' in text:
        reply = "안녕하세요!"
    elif '고마워' in text:
        reply = "서비스를 이용해주셔서 감사합니다 :)"
    else:
        reply = "알아들을 수 없는 단어가 있습니다."
    update.message.reply_text(reply)


updater = Updater(accessToken)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()