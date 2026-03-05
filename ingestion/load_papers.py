import os
import json
from langchain_community.document_loaders import PyPDFLoader  # loads PDF files and extracts text page by page
from langchain_text_splitters import RecursiveCharacterTextSplitter # splits text into smaller chunks
from langchain_core.documents import Document # stores text and context

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")
PAPERS_PATH= os.path.join(DATA_PATH,"papers")
META_DATA_PATH= os.path.join(DATA_PATH,"corpus_metadata.json")

#func to load metadta
def load_metadata():
    with open(META_DATA_PATH,"r",encoding='utf-8') as f:
        return json.load(f)
    
#func to orchestrate ingestion
def load_documents():
    metadata_list= load_metadata()
    all_documents=[] #empty list

    #loop through each metadata entry
    for meta in metadata_list:
        file_path= os.path.join(PAPERS_PATH, meta['filename'])
        if not os.path.exists(file_path):
            print(f"file not found - {meta['filename']}")
            continue


    #opens PDF reads page by page and converts each page to document object containing page_text(gets embedded) and metadata
        loader=PyPDFLoader(file_path)
        pages=loader.load()

        for page in pages:
            enriched_doc= Document(
                page_content=page.page_content,
                metadata={
                    "source_id": meta["id"],
                    "title": meta["title"],
                    "author": meta["author"],
                    "year": meta["year"],
                    "domain": meta["domain"],
                    "type": meta["type"]
                }

            )
            all_documents.append(enriched_doc)

    return all_documents

#splitting pages now
def split_documents(documents):
    splitter= RecursiveCharacterTextSplitter(
        chunk_size= 600,
        chunk_overlap=100 #so we don't lose context

    )
    return splitter.split_documents(documents)

if __name__=="__main__":
    
    docs=load_documents()
    chunks= split_documents(docs)

    print(f"Loaded {len(docs)} pages")
    print(f'Created {len(chunks)} chunks')

    #print metadsat to confirm
    if chunks:
        print('\n Sample chunk metadata')
        print(chunks[0].metadata)
    else:
        print("no chunks created.")
    # print(len(set([c.metadata["source_id"] for c in chunks])))


