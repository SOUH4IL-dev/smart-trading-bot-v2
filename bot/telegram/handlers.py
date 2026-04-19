from telegram import Update
from telegram.ext import ContextTypes
from core.strategy import analyze
from core.monitor import monitor_trade

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Use: /signal EURUSD")
        return

    symbol = context.args[0].upper()
    result = analyze(symbol)

    await update.message.reply_text(result)


async def monitor(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Use: /monitor EURUSD")
        return

    symbol = context.args[0].upper()
    result = monitor_trade(symbol)

    await update.message.reply_text(result)