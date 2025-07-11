from langchain_ollama import OllamaLLM, ChatOllama

model = ChatOllama(
    model="gemma3:4b",
)

response = model.invoke("The sky is")

print(response.content)