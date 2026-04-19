from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange
from core.mt5_handler import get_data, get_spread
from utils.session import session_filter
import MetaTrader5 as mt5

active_trades = {}

def analyze(symbol):

    if not session_filter():
        return "⏳ Session closed"

    spread = get_spread(symbol)
    if spread is None:
        return "❌ Symbol not found"

    if spread > 30:
        return f"⚠ Spread too high ({spread})"

    df = get_data(symbol, mt5.TIMEFRAME_M5, 200)

    if df is None or df.empty:
        return "❌ No data"

    close = df['close']
    high = df['high']
    low = df['low']

    ema20 = EMAIndicator(close, 20).ema_indicator()
    ema50 = EMAIndicator(close, 50).ema_indicator()
    rsi = RSIIndicator(close, 14).rsi()
    atr = AverageTrueRange(high, low, close, 14).average_true_range()

    price = close.iloc[-1]

    signal = "NO TRADE"
    sl = tp = None

    if ema20.iloc[-1] > ema50.iloc[-1] and 40 < rsi.iloc[-1] < 65:
        signal = "BUY"
        sl = price - (1.5 * atr.iloc[-1])
        tp = price + (3 * atr.iloc[-1])

    elif ema20.iloc[-1] < ema50.iloc[-1] and 35 < rsi.iloc[-1] < 60:
        signal = "SELL"
        sl = price + (1.5 * atr.iloc[-1])
        tp = price - (3 * atr.iloc[-1])

    if signal != "NO TRADE":
        active_trades[symbol] = {"type": signal, "entry": price}

    return f"""
📊 {symbol}

Signal: {signal}
Entry: {round(price,5)}
SL: {round(sl,5) if sl else '-'}
TP: {round(tp,5) if tp else '-'}
"""