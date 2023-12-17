import time

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time.sleep(10)
    await context.bot.send_message(   
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token('6474533873:AAEUK4AtkTfJr3eghfSGM1Y_4di_vW7kIkI').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()