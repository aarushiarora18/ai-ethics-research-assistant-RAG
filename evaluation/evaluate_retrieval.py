from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from evaluation.benchmark_queries import benchmark_queries

INDEX_PATH="faiss_index"
embedding= HuggingFaceEmbeddings(
    model_name= "sentence-transformers/all-MiniLM-L6-v2"
#    model_name="BAAI/bge-small-en-v1.5"
    )

vector_store= FAISS.load_local(
        INDEX_PATH,
        embedding,
        allow_dangerous_deserialization=True # trust local file and load it
    )
k=5
total_correct=0
total_result=0

for test in benchmark_queries:
    
    query=test["query"]
    expected_domain=test["expected_domain"]
    results= vector_store.similarity_search(query,k=k)

    print("\nQuery:", query)

    correct=0
    for doc in results:
        domain=doc.metadata.get("domain")
        print("Retrieved domain:", domain)
        if domain == expected_domain:
            correct+=1

    total_correct+= correct
    total_result+=k

precision_at_k = total_correct / total_result

print("\nPrecision@{}: {:.2f}".format(k, precision_at_k))



