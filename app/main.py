from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.db import save_embedding_to_faiss, retrieve_documents
from app.services.ingestion_service import ingest_document
from app.services.retrieval_service import query_faiss

app = FastAPI()

# Model for document ingestion
class Document(BaseModel):
    title: str
    content: str

# Route for ingesting documents
@app.post("/ingest/")
async def ingest(document: Document):
    # Call the ingestion service
    doc_id, embedding = ingest_document(document.title, document.content)
    if not doc_id:
        raise HTTPException(status_code=400, detail="Failed to ingest document.")
    
    # Save embedding to FAISS
    save_embedding_to_faiss(doc_id, embedding)
    return {"message": "Document ingested and saved in FAISS", "doc_id": doc_id}

# Route for retrieving documents based on a query
@app.get("/retrieve/")
async def retrieve(query: str):
    # Perform vector search in FAISS
    retrieved_docs = query_faiss(query)
    if not retrieved_docs:
        raise HTTPException(status_code=404, detail="No documents found.")
    
    return {"retrieved_documents": retrieved_docs}
