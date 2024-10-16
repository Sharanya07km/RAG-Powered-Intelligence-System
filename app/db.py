import faiss
import numpy as np

# Initialize FAISS index (for demo purposes, using flat index)
dimension = 768  # Example dimension of embeddings (should match Chaitra's embeddings)
index = faiss.IndexFlatL2(dimension)

# Store document IDs and embeddings
doc_embeddings = {}
doc_id_counter = 1

def save_embedding_to_faiss(doc_id: int, embedding: np.ndarray):
    """
    Save the embedding to FAISS index.
    """
    global index
    # Add embedding to FAISS index
    index.add(np.array([embedding]))
    doc_embeddings[doc_id] = embedding

def retrieve_documents(embedding: np.ndarray, top_k: int = 5):
    """
    Perform vector search in FAISS to retrieve relevant documents.
    """
    global index
    # Search for the top K closest vectors
    distances, indices = index.search(np.array([embedding]), top_k)
    
    # Retrieve corresponding document IDs
    results = [doc_embeddings.get(idx, None) for idx in indices[0]]
    
    return results
