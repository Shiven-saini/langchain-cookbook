from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:4b"
)


response_batch = model.batch(["Tell me about Alpha centauri", "Tell me about Proxima Centauri"])

for i in response_batch:
    print(i.content)
    print('='*30)

