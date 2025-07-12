from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:4b"
)

response_stream = model.stream("Tell me about alpha centauri")

for i in response_stream:
    print(i.content, end='')