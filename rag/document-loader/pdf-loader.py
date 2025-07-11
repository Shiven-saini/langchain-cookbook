from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./LLM.pdf")

document = loader.load()

print(len(document))

for i in document:
    print(i.page_content)
    print("="*40)