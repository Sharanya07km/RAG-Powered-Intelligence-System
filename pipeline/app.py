from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from embedding import DocumentEmbedder  # Ensure this is correctly defined
from ingest import ingest_document_to_api, save_embedding_to_faiss
from retrieval import retrieve_documents  # This import should work if retrieval.py is correct

app = FastAPI()

# Model for document ingestion
class Document(BaseModel):
    title: str
    content: str

# Route for ingesting documents
@app.post("/ingest/")
async def ingest(document: Document):
    try:
        # Call your ingestion function
        doc_id, embedding = ingest_document_to_api(document.title, document.content)
        
        # Save the embedding to FAISS
        save_embedding_to_faiss(doc_id, embedding)
        return {"message": "Document ingested and saved in FAISS", "doc_id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route for retrieving documents based on a query
@app.get("/retrieve/")
async def retrieve(query: str):
    try:
        # Call your retrieval function
        retrieved_docs = retrieve_documents(query)
        return {"retrieved_documents": retrieved_docs}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# app.py
def main():
    print("[INFO] Starting the application...")
    # Initialize app, routes, etc.
    print("[INFO] Application initialized successfully.")
    # Your application logic here

if __name__ == "__main__":
    main()
