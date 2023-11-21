from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import pickle

# Chunking the data
# Chunking.
def get_dataset():
    with open('data.pkl', 'rb') as file:
        docs = pickle.load(file)
    return docs

def get_chunks():
    docs = get_dataset()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)

    chunks = []
    for text in docs:
        subset = text_splitter.create_documents([text])
        subset = text_splitter.split_documents(subset)
        chunks += subset
    
    return chunks

## vector db creation
chunks = get_chunks()
print(f"number of chunks {len(chunks)}")

print("creating FAISS db ....")

persist_directory = 'faiss_db/'

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

vectordb.save_local(persist_directory)

print(f"Successfully saved embeddings in FAISS")
