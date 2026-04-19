from core.strategy import active_trades
from core.mt5_handler import get_data
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
import MetaTrader5 as mt5

def monitor_trade(symbol):

    if symbol not in active_trades:
        return "❌ No active trade"

    trade = active_trades[symbol]

    df = get_data(symbol, mt5.TIMEFRAME_M5, 100)
    if df is None or df.empty:
        return "❌ No data"

    close = df['close']

    ema20 = EMAIndicator(close, 20).ema_indicator()
    ema50 = EMAIndicator(close, 50).ema_indicator()
    rsi = RSIIndicator(close, 14).rsi()

    if trade["type"] == "BUY":
        if ema20.iloc[-1] < ema50.iloc[-1] or rsi.iloc[-1] > 70:
            del active_trades[symbol]
            return "⚠ EXIT BUY"

    if trade["type"] == "SELL":
        if ema20.iloc[-1] > ema50.iloc[-1] or rsi.iloc[-1] < 30:
            del active_trades[symbol]
            return "⚠ EXIT SELL"

    return "✅ Trade valid"