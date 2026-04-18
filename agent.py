import os
from openai import OpenAI
from typing import List, Dict, Any, Optional

class Agent:
    def __init__(
        self,
        model: str = "gpt-4o",
        system_prompt: str = "You are a helpful assistant.",
        provider: str = "openai",  # "openai", "grok", or "groq"
        api_key: Optional[str] = None
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.provider = provider
        
        key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("GROK_API_KEY") or os.getenv("GROQ_API_KEY")
        
        if provider == "groq":
            self.client = OpenAI(
                api_key=key,
                base_url="https://api.groq.com/openai/v1"
            )
        elif provider == "grok":
            self.client = OpenAI(
                api_key=key,
                base_url="https://api.x.ai/v1"
            )
        else:
            self.client = OpenAI(api_key=key)
        
        self.messages: List[Dict[str, Any]] = [{"role": "system", "content": system_prompt}]
    
    def chat(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        
        assistant_message = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def reset(self):
        self.messages = [{"role": "system", "content": self.system_prompt}]
    
    def get_history(self) -> List[Dict[str, Any]]:
        return self.messages.copy()