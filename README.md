# 🤖 Smart Trading Bot v2

### MT5 • Telegram • Algorithmic Trading Engine

An advanced modular trading bot built with **Python**, integrated with **MetaTrader 5** and **Telegram**, designed to deliver real-time trading signals using a structured and scalable architecture.

---

## 📌 Overview

**Smart Trading Bot v2** is a more advanced evolution of the basic signal bot, focusing on:

* Clean architecture (modular design)
* Scalable trading logic
* Real-time signal generation
* Trade lifecycle monitoring

This project is designed for developers who want to build **professional algorithmic trading systems**.

---

## 🧠 Strategy Engine

The bot combines multiple technical indicators:

* **Trend Detection** → EMA (20 / 50)
* **Momentum Filter** → RSI (14)
* **Volatility Control** → ATR (14)

### 📈 Buy Conditions

* EMA20 > EMA50
* RSI between 40 – 65

### 📉 Sell Conditions

* EMA20 < EMA50
* RSI between 35 – 60

### 🎯 Risk Model

* Stop Loss → 1.5 × ATR
* Take Profit → 3 × ATR

---

## ⚙️ Features

* 📊 Market analysis (M5 timeframe)
* 📩 Telegram bot integration
* 🧩 Modular architecture (core / utils / handlers)
* ⏱️ Session filtering (London & New York)
* 🚫 Spread filtering (avoid bad trades)
* 🔁 Trade monitoring system
* 🧾 Logging system

---

## 📁 Project Structure

```id="rgby3f"
bot/
│
├── bot.py                  # Entry point
├── config.py              # Environment config
├── requirements.txt
├── .env
│
├── core/
│   ├── mt5_handler.py     # MT5 connection & data
│   ├── strategy.py        # Trading logic
│   ├── monitor.py         # Trade lifecycle
│
├── telegram/
│   └── handlers.py        # Telegram commands
│
├── utils/
│   └── session.py         # Trading sessions
```

---

## 💬 Telegram Commands

| Command           | Description             |
| ----------------- | ----------------------- |
| `/signal EURUSD`  | Generate trading signal |
| `/monitor EURUSD` | Check trade status      |

---

## 🔐 Environment Setup

Create a `.env` file:

```env id="q4tf7e"
TELEGRAM_TOKEN=your_token_here
```

---

## 🛠️ Installation

```bash id="qz7a5p"
git clone https://github.com/your-username/smart-trading-bot.git
cd smart-trading-bot
pip install -r requirements.txt
```

---

## ▶️ Run the Bot

```bash id="9w0c2u"
python bot.py
```

---

## 📦 Tech Stack

* Python 3.9+
* MetaTrader 5 API
* pandas
* ta (Technical Analysis)
* python-telegram-bot
* pytz

---

## 📈 Roadmap

### v2 (current)

* Modular architecture ✅
* Signal + monitoring system ✅

### v3 (planned)

* 🤖 Auto trade execution
* 📊 Web dashboard
* 📡 WebSocket / real-time streaming
* 🧠 AI-based signals
* 📉 Backtesting engine

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Trading financial markets involves significant risk.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 👨‍💻 Author

**Souhail**
GitHub: https://github.com/SOUH4IL-dev

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
