from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
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
    text_splitter = CharacterTextSplitter(
        chunk_size = 512,
        chunk_overlap  = 0,
        separator = ' '
    )

    chunks = []
    for text in docs:
        subset = text_splitter.create_documents([text])
        subset = text_splitter.split_documents(subset)
        chunks += subset
    
    return chunks

## vector db creation
chunks = get_chunks()
print(f"number of chunks {len(chunks)}")

print("creating chroma db ....")
persist_directory = 'chroma_db/'
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory=persist_directory
)

# print("quering question ....")
# question = "What is HELIS?"
# result = vectordb.similarity_search(question, k=3)





