from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

INDEX_PATH = "faiss_index"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    INDEX_PATH,
    embedding,
    allow_dangerous_deserialization=True
)