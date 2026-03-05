from retrieval.retrieve import retrieve_documents
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


def answer_questions(query):
    docs=retrieve_documents(query)
    if not docs:
        print("No relevant sources found")
        return
    context= "\n\n".join([doc.page_content for doc in docs])
    prompt= ChatPromptTemplate.from_template("""
    You are an academic AI research assistant.

    Answer the user's question using ONLY the context provided.

    Cite sources using (Author, Year).

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    
        
    )
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )
    chain= prompt | model

    response = chain.invoke({
        "context": context,
        "question": query
    })

    print("\nAnswer:\n")
    print(response.content)

    print("\nSources:\n")

    for doc in docs:
        meta = doc.metadata
        print(f"{meta['author']} ({meta['year']}) — {meta['title']}")


if __name__=="__main__":
    question= input("Ask a question: ")
    answer_questions(question)