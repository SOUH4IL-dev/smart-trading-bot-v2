import MetaTrader5 as mt5
import pandas as pd
import logging

def init_mt5():
    if not mt5.initialize():
        logging.error("MT5 init failed")
        quit()

def get_data(symbol, timeframe, n=300):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)

    if rates is None:
        return None

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def get_spread(symbol):
    info = mt5.symbol_info(symbol)
    if info is None:
        return None
    return info.spread