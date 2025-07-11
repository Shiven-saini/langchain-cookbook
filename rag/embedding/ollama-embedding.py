from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model="nomic-embed-text:latest")

embeddings = embedding_model.embed_documents(

    [
        "Hi there!",
        "Oh, Hello!",
        "What's your name?",
        "Hello world"
    ]

)

print(len(embeddings[0]))
print(len(embeddings[1]))



# for i in embeddings:
#     print(i)
#     print('='*40)