import numpy as np
from app.db import retrieve_documents

# A function to query FAISS with user input and get relevant documents
def query_faiss(query: str):
    """
    Convert the query into an embedding and search in FAISS.
    (For demo, using a random embedding for the query, replace with actual embedding logic)
    """
    query_embedding = np.random.rand(768)  # Replace with actual embedding generation
    return retrieve_documents(query_embedding)
