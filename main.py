from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Witaj! Twój bot w działa.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Dostępne komendy:\n"
        "/start - Uruchamia bota\n"
        "/help - Wyświetla tę listę pomocy"
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

    application.run_polling()