from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

async def help_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "<b>🛠 Dostępne komendy:</b>\n\n"
        "🚀 /start - Uruchamia bota\n"
        "❓ /help - Wyświetla listę pomocy\n\n"
        "<b>📋 Zadania (/task):</b>\n"
        "• <code>tokenize</code>\n"
        "• <code>remove_stopwords</code>\n"
        "• <code>lemmatize</code>\n"
        "• <code>stemming</code>\n"
        "• <code>stats</code>\n"
        "• <code>n-grams</code>\n"
        "• <code>plot_histogram</code>\n"
        "• <code>plot_wordcloud</code>\n\n"
        "⚙️ /full_pipeline - Praca nad full_pipeline\n"
        "🧠 /classifier - Praca nad classifier\n"
        "📊 /stats - Statystyki ogólne"
    )
    
    await update.message.reply_text(help_text, parse_mode=ParseMode.HTML)

async def start_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Witaj, jestem gotowy do działania!")
