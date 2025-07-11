from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./python-sample.py")
document = loader.load()

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=1000,
    chunk_overlap=0
)

document_chunks = splitter.split_documents(document)

print(len(document_chunks))

for i in document_chunks:
    print(i.page_content)
    print('='*40)