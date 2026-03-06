import streamlit as st
from generation.answer_questions import answer_questions

st.title("AI Ethics Research Assistant")

query=st.text_input("Ask a question about AI ethics")
if query:
    answer,docs= answer_questions(query)
    st.subheader("Answer:")
    st.write(answer)

    st.subheader("Sources:")

    for i, doc in enumerate(docs):

        meta=doc.metadata
        st.write(
            f"[{i+1}] {meta.get('author','Unkown')} "
            f"({meta.get('year','NA')}) - ",
            f"{meta.get('title','unknown')}"
        )
