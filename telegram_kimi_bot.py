import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
from typing import Dict

# Set these as environment variables or replace with your keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "YOUR_OPENROUTER_API_KEY")

SYSTEM_PROMPT = """You are a helpful and friendly AI assistant named Kimi. 
You are powered by Kimi K2.5 AI model from Moonshot.
- Be concise and friendly
- Help with coding, research, writing, questions
- Be honest if you don't know something"""

MODEL_CONFIG = {
    "model": "kimi/kimi-k2.5",
    "max_tokens": 4096,
}

class KimiAgent:
    def __init__(self, system_prompt: str = SYSTEM_PROMPT):
        self.system_prompt = system_prompt
        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
        self.conversations: Dict[int, list] = {}
    
    def _get_conversation(self, user_id: int) -> list:
        if user_id not in self.conversations:
            self.conversations[user_id] = [
                {"role": "system", "content": self.system_prompt}
            ]
        return self.conversations[user_id]
    
    def chat(self, user_id: int, message: str) -> str:
        messages = self._get_conversation(user_id)
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model=MODEL_CONFIG["model"],
                messages=messages,
                max_tokens=MODEL_CONFIG["max_tokens"]
            )
            
            assistant_message = response.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_message})
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self, user_id: int):
        if user_id in self.conversations:
            del self.conversations[user_id]

agent = KimiAgent()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Hi! I'm Kimi Bot powered by Kimi K2.5 AI.\n\n"
        "I can help with coding, research, writing & more!\n\n"
        "Commands:\n"
        "/reset - New conversation"
    )

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    agent.reset_conversation(user_id)
    await update.message.reply_text("✅ Done! New conversation started.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text
    
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing"
    )
    
    response = agent.chat(user_id, user_message)
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Kimi Bot running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()