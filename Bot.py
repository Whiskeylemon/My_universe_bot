from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8042036116:AAGpADS23mUew77uj6weB4yOgq7J6NPsScY'  # сюда вставь свой токен от BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я твой бот!')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))

app.run_polling()
