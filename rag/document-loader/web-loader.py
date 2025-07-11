from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://youtube.com/")

document = loader.load()

print(len(document))