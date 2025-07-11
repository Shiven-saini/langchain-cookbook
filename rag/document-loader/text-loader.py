from langchain_community.document_loaders import TextLoader

loader = TextLoader("./raw-text.txt")

document = loader.load()
print(len(document))