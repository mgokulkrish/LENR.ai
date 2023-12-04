from langchain.vectorstores import Chroma, FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import pickle

db = "faiss"
chunk_size = 512
chunk_overlap = 20

# Chunking the data
# Chunking.
def get_dataset():
    with open('data.pkl', 'rb') as file:
        docs = pickle.load(file)
    return docs

def get_chunks(size, overlap):
    docs = get_dataset()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = []
    for text in docs:
        subset = text_splitter.create_documents([text])
        chunks += subset

    return chunks

## vector db creation
chunks = get_chunks(chunk_size, chunk_overlap)
print(f"number of chunks {len(chunks)}")


def save_vector_db(db):
    if db == "chroma":
        print("creating chroma db ....")
        persist_directory = 'chroma_db/'
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embedding,
            persist_directory=persist_directory
        )
    elif db == "faiss":
        print("creating FAISS db ....")
        persist_directory = 'faiss_db/'
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings
        )
        vectordb.save_local(persist_directory)
    else:
        raise ValueError(f"Cannot identify database - {db}")

    print(f"Successfully saved embeddings in {db}")

save_vector_db(db)
