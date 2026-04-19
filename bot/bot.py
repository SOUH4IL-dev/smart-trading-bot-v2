from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN
from telegram.handlers import signal, monitor
from core.mt5_handler import init_mt5

def main():

    init_mt5()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("monitor", monitor))

    print("🚀 BOT RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()