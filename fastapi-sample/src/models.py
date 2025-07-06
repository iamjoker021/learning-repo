from pydantic import BaseModel

class ChatRequest(BaseModel):
    """
    The user request/prompt 
    """
    prompt: str

class ChatResponse(BaseModel):
    """
    The AI response
    """
    response: str
