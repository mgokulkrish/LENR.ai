from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

print("loading vector_db ....")

persist_directory = 'faiss_db/'
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = FAISS.load_local(persist_directory, embeddings)

print("quering question ....")
question = "What is HELIS?"
result = db.similarity_search(question)

for i in range(len(result)):
    print(f"document {i}")
    print(result[i].page_content)
    print(f"\n")

