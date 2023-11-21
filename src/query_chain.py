from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("loading vector_db ....")
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

print("quering question ....")
question = "What is HELIS?"
result = db.similarity_search(question, k=3)

for i in range(3):
    print(f"document {i}")
    print(result[i].page_content)
    print("")