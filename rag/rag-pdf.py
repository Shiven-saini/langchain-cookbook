from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma

file_location = r"./document-loader/LLM.pdf"

loader = PyPDFLoader(file_location)

documents = loader.load()

## Split the documents object
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

document_chunks = splitter.split_documents(documents)
print(len(document_chunks))

## Embedd the chunks data.
model = OllamaEmbeddings(model="nomic-embed-text:latest")

# embeddings = model.embed_documents(

#     [chunk.page_content for chunk in document_chunks]

# )

## Storing the embeddings in a vector store.
## No need of creating embeddings separately.

db = Chroma.from_documents(document_chunks, model)

similar_embeddings = db.similarity_search("Deepseek", k=4)

for i in similar_embeddings:
    print(i.page_content)
    print('='*40)