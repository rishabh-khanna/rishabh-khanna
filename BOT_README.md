# 🤖 Kimi Telegram Bot

An AI-powered Telegram bot built with Python, Kimi K2.5, and deployed with full CI/CD pipeline.

## 🚀 Features

- 🤖 Powered by **Kimi K2.5** AI via OpenRouter
- 💬 Conversational AI with memory per user
- 🔄 Deploys automatically via **GitHub Actions**
- 📊 Includes CI pipeline with tests and linting

## 🛠️ Tech Stack

- **Language**: Python 3.11+
- **AI**: OpenRouter API (Kimi K2.5)
- **Bot**: python-telegram-bot
- **CI/CD**: GitHub Actions

## 📦 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

```bash
export TELEGRAM_BOT_TOKEN="your_token"
export OPENROUTER_API_KEY="your_key"
python telegram_kimi_bot.py
```

## 🔄 CI/CD Pipeline

This project includes full CI/CD:

### CI Pipeline (`.github/workflows/ci.yml`)
- ✅ Runs tests on every push
- ✅ Code linting and quality checks
- ✅ Prevents bad code from merging

### CD Pipeline (`.github/workflows/deploy.yml`)
- ✅ Auto-deploys to server on push to main
- ✅ SSH deployment with PM2 process manager
- ✅ Manual trigger option

## 📁 Project Structure

```
.
├── telegram_kimi_bot.py   # Main bot code
├── agent.py               # Reusable AI agent
├── requirements.txt      # Python dependencies
└── .github/
    └── workflows/
        ├── ci.yml        # CI pipeline
        └── deploy.yml   # CD pipeline
```

---

<div align="center">

**Built with 💚 by Rishabh Khanna**

[LinkedIn](https://linkedin.com/in/r1shabhkhanna) | [Email](mailto:rishabh-khanna@outlook.com)

</div>