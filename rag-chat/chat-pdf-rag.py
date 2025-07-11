from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Setting up the ollama model and embeddings model
model = ChatOllama(
    model="gemma3:4b",
    temperature=0.1
)

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Setting up the pdf parser and loading the Document object files
file_path = "./attention.pdf"
loader = PyPDFLoader(file_path)

documents = loader.load()

# Chunking the parsed document object file
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

document_chunks = splitter.split_documents(documents)

# Creating a vector store chroma database file to store the chunks embeddings
db = Chroma(
    documents = document_chunks,
    embedding_function=embedding_model,
    collection_name="research-paper"
)


