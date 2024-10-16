import requests
from sentence_transformers import SentenceTransformer

# Initialize the Sentence Transformer model (you can change this to another pre-trained model if needed)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to send document to Sharanya's API
def ingest_document_to_api(title: str, content: str):
    # Generate embeddings using sentence-transformers
    embedding = model.encode(content)

    # Prepare payload for Sharanya's API
    document = {
        "title": title,
        "content": content
    }

    # Call Sharanya's API for document ingestion
    response = requests.post("http://sharanya-api-url/ingest/", json=document)
    if response.status_code == 200:
        doc_id = response.json()["doc_id"]
        return doc_id, embedding
    else:
        raise Exception("Failed to ingest document")

# Save embeddings to Sharanya's FAISS API
def save_embedding_to_faiss(doc_id, embedding):
    # Convert the embedding (numpy array) to a list for JSON serialization
    payload = {
        "doc_id": doc_id,
        "embedding": embedding.tolist()  # Convert numpy array to list for JSON serialization
    }

    # Call Sharanya's API to save embedding in FAISS
    response = requests.post("http://sharanya-api-url/save_embedding/", json=payload)
    if response.status_code != 200:
        raise Exception("Failed to save embedding to FAISS")

# Example usage
try:
    title = "Sample Document"
    content = "This is the content of the sample document."
    
    # Ingest document to the API and get document ID and embedding
    doc_id, embedding = ingest_document_to_api(title, content)
    
    # Save embedding to FAISS
    save_embedding_to_faiss(doc_id, embedding)
    
    print(f"Document '{title}' successfully ingested and embedding saved!")
except Exception as e:
    print(f"Error: {e}")

# ingest.py
def ingest_data(embeddings):
    print("[INFO] Ingesting embeddings into storage...")
    # Code to send embeddings to Sharanya's API
    print("[INFO] Embeddings ingested successfully.")

if __name__ == "__main__":
    embeddings = []  # Load or create your embeddings
    ingest_data(embeddings)
