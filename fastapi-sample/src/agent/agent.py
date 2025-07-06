import os
from langchain_google_genai import ChatGoogleGenerativeAI
from ..utils.load_prompt import load_prompt

from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = os.getenv("LLM_MODEL_NAME")
API_KEY = os.getenv("GEMINI_API_KEY")
TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))
MAX_RETRIES = int(os.getenv("LLM_TMAX_RETRIES", "2"))
SYSTEM_PROMPT = load_prompt("src/agent/prompts/system_prompt.md")

class GeminiClient():

    def __init__(self,
                 model_name=MODEL_NAME, 
                 api_key=API_KEY, 
                 temperature=TEMPERATURE, 
                 max_retries=MAX_RETRIES,
                 system_prompt=SYSTEM_PROMPT) -> None:
        self.system_prompt = system_prompt
        self.llm = ChatGoogleGenerativeAI(
                    model=model_name,
                    temperature=temperature,
                    api_key=api_key,
                    max_retries=max_retries,
                )
        
    def chat(self, prompt: str):
        return self.llm.invoke([self.system_prompt, prompt])
