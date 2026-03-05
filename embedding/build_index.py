from ingestion.load_papers import split_documents, load_documents
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS # to store

INDEX_PATH= "faiss_index" # creates a folder which contains vectors, metadata and index files

def build_vector_index():
    print("loading and splitting documents")
    docs= load_documents()
    chunks= split_documents(docs)
    print(f"total chunks: {len(chunks)}")
    print("loading embedding model..")
    
    # creating a tool "embeddings": texts -> vectors
    embeddings= HuggingFaceEmbeddings(
        model_name= "sentence-transformers/all-MiniLM-L6-v2" #converts sentences into 384 dimensional vectors
 #       model_name="BAAI/bge-small-en-v1.5"
    )

    print("creating FAISS vector store..")
    vector_store= FAISS.from_documents(chunks,embeddings) # for each chunk there is a vector, which is mapped and kept here
    print("saving FAISS index locally..")
    vector_store.save_local(INDEX_PATH) #folder we created
    print("index built and saved")

if __name__=="__main__":
    build_vector_index()