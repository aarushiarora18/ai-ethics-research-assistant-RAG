from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from retrieval.vector_store import vector_store, INDEX_PATH



def retrieve_documents(query, domain_filter=None, k=10, max_results=3):
    
    
    results = vector_store.similarity_search(query, k=k) #retrieve 10 results first

    
    if domain_filter:
        print("applying domain filter", domain_filter)
       
        results = [
            doc for doc in results
            if doc.metadata.get("domain") == domain_filter
        ]
    # diversity filter
    unique_results=[]
    seen_sources=set()
    for doc in results:
        source_id = doc.metadata.get("source_id")

        if source_id not in seen_sources:
            unique_results.append(doc)
            seen_sources.add(source_id)

        if len(unique_results) == 3:
            break

    results = unique_results   #keep only top 3
    return unique_results
