
from retrieval.retrieve import retrieve_documents


# func to take query->vector then search vector database for similar chunks
def test_query(query, domain_filter=None):

    print("\nQuery:", query)
  
    results = retrieve_documents(query,domain_filter)  

    for i, doc in enumerate(results):
        print(f"\nResults:{i+1}") #result number
        print("Metadata:", doc.metadata)
        print("Text Preview:", doc.page_content[:400]) # prints first 400 characters of the chunk


if __name__=="__main__":
    test_query("What are ethical risks of AI surveillance?")

    test_query("What are ethical risks of AI surveillance?", domain_filter="surveillance")
    