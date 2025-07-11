from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.storage import InMemoryStore
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain_core.documents import Document

import uuid


# Creating loader document object
file_path="./document-loader/LLM.pdf"
loader = PyPDFLoader(file_path)

documents = loader.load()

# Split the documents file object
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

# Setting up the chroma database and embeddings
model = ChatOllama(
    model='gemma3:4b',
    temperature=0.7
)

# Prompt and text prompt template setup
prompt_text = "Remember only return the final summar. Make sure don't to add anything else other than summary text. Summarize the following document:\n\n{doc}"
prompt = ChatPromptTemplate.from_template(prompt_text)

# Setting up the summarize chain
summarize_chain = {"doc": lambda x: x.page_content} | prompt | model | StrOutputParser()

# Batch the chunk texts to generate summary
summaries = summarize_chain.batch(chunks, {"max_concurrency": 5} )

# To create a vector store with chroma and storing the summary embeddings linking each id.
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

vector_store = Chroma(
    embedding_function=embedding_model,
    collection_name="pdf-chunks-summary",
)

# Storage layer for the parent documents storage.
data_store = InMemoryStore()
id_key="doc_id"

# Indexing the summaries in our vector store, whilst retaining the original document in our document store.
retriever = MultiVectorRetriever(
    vectorstore=vector_store,
    docstore=data_store,
    id_key=id_key
)

doc_ids = [str(uuid.uuid4()) for _ in chunks]

summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})
    for i, s in enumerate(summaries)
]

# Add the document summaries to the vector store for similarity search
retriever.vectorstore.add_documents(summary_docs)

# Store the original documents in the document store, linked to their ids in summaries
# This allows us to first search summaries efficiently, then fetch the docs when needed.
retriever.docstore.mset(list(zip(doc_ids, chunks)))

# user_query = input("Enter your query: ")

# retrieved_docs = retriever.invoke(user_query)

# retrieved_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt_template = ChatPromptTemplate.from_messages(

    [
        ('system', "Answer the question based only on the context below. If the question cannot be answered using the information & context provided even if you know, answer with 'I don't know'"),
        ('human', "Context : {context}"),
        ('human', "Question: {question}")
    ]

)

while True:
    user_query = input("Enter your question => ")

    retrieved_docs = retriever.invoke(user_query)

    retrieved_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

    chain = prompt_template | model

    response = chain.invoke(

        {
        "question": user_query, 
        "context" : retrieved_text
        }

    )

    print(response.content)
