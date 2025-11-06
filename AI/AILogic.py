import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv() # Load environment variables from .env file

# Initialize Azure ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["ApiKey"]),
    api_version="2024-12-01-preview",
)

# Initialize message history with system instructions
messages=[
    SystemMessage("You are a helpful assistant that is called Skrotnissen."),
    SystemMessage("You answer in a friendly, concise manner and as short as possible without lossing any detail or helpfullness."),
    SystemMessage("Use the product database to help the user find products they are looking for. If you don't find any products that match the user's request, politely inform them that no products were found."),
]

def get_ai_response(userInput: str, database: dict) -> str:
    global messages

    messages.append(SystemMessage(f"Here is the product database you can use to help the user: {database}"))
    messages.append(UserMessage(userInput)) # Add user input to message history

    # Get AI response from the model
    response = client.complete(
        messages=messages,
        model="gpt-4o-mini"
    )

    ai_response = response.choices[0].message.content # Extract AI's reply

    messages.append(AssistantMessage(ai_response)) # Add AI's response to message history

    return ai_response # Return the AI's response