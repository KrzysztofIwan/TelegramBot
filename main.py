from handlers import help_handler, classifier_handler, task_handler, full_pipeline_handler, stats_handler
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import load_token
import json

if __name__ == '__main__':
    token = load_token()
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('start', help_handler.start_handle))
    application.add_handler(CommandHandler('help', help_handler.help_handle))
    application.add_handler(CommandHandler('task', task_handler.handle))
    application.add_handler(CommandHandler('full_pipeline', full_pipeline_handler.handle))
    application.add_handler(CommandHandler('classifier', classifier_handler.handle))
    application.add_handler(CommandHandler('stats', stats_handler.handle))
    application.run_polling()