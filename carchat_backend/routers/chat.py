from fastapi import APIRouter
from carchat_backend.schemas.chat import ChatRequest, ChatResponse
from carchat_backend.services.chatbot import get_chat_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    return get_chat_response(request)
