from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Witaj, jestem gotowy do działania!")

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("to jest węzeł do tasków")

async def full_pipeline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("to jest węzeł do full_pipeline")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Dostępne komendy:\n"
        "/start - Uruchamia bota\n"
        "/help - Wyświetla tę listę pomocy\n"
        "/task - prace nad taskami\n"
        "/full_pipeline - praca nad full_pipeline"
    )
    await update.message.reply_text(help_text)

def load_token(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['token']

if __name__ == '__main__':
    token = load_token('data/setup_api.json')
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('task', task))
    application.add_handler(CommandHandler('full_pipeline', full_pipeline))

    application.run_polling()