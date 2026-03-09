from telegram import Update
from telegram.ext import ContextTypes

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if not args:
        await update.message.reply_text("Musisz podać parametr zadania!")
    
    action = args[0].lower()
    match action:
        case "tokenize":
            await update.message.reply_text("Uruchamiam tokenizację tekstu...")

        case "remove_stopwords":
            await update.message.reply_text("Usuwam stop-words (słowa pospolite)...")
            
        case "lemmatize":
            await update.message.reply_text("Rozpoczynam lematyzację (sprowadzanie do formy podstawowej)...")
            
        case "stemming":
            await update.message.reply_text("Wykonuję stemming (obcinanie końcówek)...")
            
        case "stats":
            await update.message.reply_text("Obliczam statystyki wystąpień słów...")
            
        case "n-grams":
            await update.message.reply_text("Generuję N-gramy dla podanego tekstu...")
            
        case "plot_histogram":
            await update.message.reply_text("Przygotowuję histogram częstości...")
            
        case "plot_wordcloud":
            await update.message.reply_text("Generuję chmurę tagów (WordCloud)...")
        case _:
            await update.message.reply_text(f"Podałeś akcje której nie rozumiem <b>{action}</b>", parse_mode='HTML')
    