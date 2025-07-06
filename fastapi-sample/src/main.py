from fastapi import FastAPI
from .models import ChatRequest, ChatResponse
from .agent.agent import GeminiClient

def main():
    app = FastAPI()
    agent = GeminiClient()

    @app.get("/")
    async def root():
        return {"response": "API is running"}

    @app.post("/chat")
    async def chat(request: ChatRequest) -> ChatResponse:
        response = agent.chat(request.prompt)
        print("RESPONSE: ", response)
        return ChatResponse(response=response.content)

    return app

app = main()
