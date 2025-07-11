from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


file = r"../document-loader/LLM.pdf"

loader = PyPDFLoader(file)
document = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

document_chunks = splitter.split_documents(document, [{"author": "Shiven Saini", "title": "LLM-Backbone"}])

for i in document_chunks:
    print(i)
    print('='*50)