import openai
import os
from dotenv import load_dotenv
from carchat_backend.schemas.chat import ChatRequest, ChatResponse

load_dotenv()  # Laad API sleutel uit .env bestand
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(request: ChatRequest) -> ChatResponse:
    prompt = f"Beantwoord als een professionele verkoper van een autobedrijf: {request.message}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )

    reply = response.choices[0].message.content.strip()
    return ChatResponse(reply=reply)
