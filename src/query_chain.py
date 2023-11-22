from langchain.vectorstores import Chroma, FAISS
from langchain.embeddings import HuggingFaceEmbeddings

print("loading vector_db ....")

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = "faiss"

if db == "faiss":
    persist_directory = 'faiss_db/'
    db = FAISS.load_local(persist_directory, embeddings=embedding)
elif db == "chroma":
    db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)
else:
    raise ValueError(f"Cannot recognize database - {db}")

print("quering question ....")
question = "What is HELIS?"
result = db.similarity_search(question, k=3)

for i in range(len(result)):
    print(f"document {i}")
    print(result[i].page_content)
    print(f"\n")