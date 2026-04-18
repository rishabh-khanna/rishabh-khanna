from dotenv import load_dotenv
from agent import Agent

load_dotenv()

# Using Groq (free tier available!)
# Set your API key: export GROQ_API_KEY="your_key_here"
agent = Agent(
    model="llama-3.3-70b-versatile",
    provider="groq",
    api_key="your_groq_api_key_here"
)

response = agent.chat("Hello! What can you do?")
print("Agent:", response)

print("\n--- Chat History ---")
for msg in agent.get_history():
    print(f"{msg['role']}: {msg['content']}")