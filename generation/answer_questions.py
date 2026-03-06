from retrieval.retrieve import retrieve_documents
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def answer_questions(query):
    docs=retrieve_documents(query)
    if not docs:
        return "No relevant sources found",[]
    context = "\n\n".join(
        [f"[{i+1}]\n{doc.page_content}" for i, doc in enumerate(docs)]
    )
    prompt= ChatPromptTemplate.from_template("""
You are an academic AI research assistant.

Answer the user's question using ONLY the context provided.
                                             
If the context doesn't contain enough information, say so.
                                             
Cite sources using [1], [2], etc.

Prefer citing more than one source when relevant.
                                                                                          
Do NOT create a References or Sources section.    
                                                                                                                                
                                                                                        
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
    return response.content, docs

    

if __name__=="__main__":
    question= input("Ask a question: ")
    answer, docs= answer_questions(question)
    print("\nAnswer:\n")

    print("\nSources:\n")

    for i, doc in enumerate(docs):
        meta = doc.metadata
        print(f"[{i+1}] {meta.get['author','Unkown']} "
              f"({meta.get['year','NA']}) — "
              f"{meta.get['title','Unknown']}"
        )