import numpy as np
from app.models.document_model import Document

# A function that processes the document (e.g., embedding generation)
def ingest_document(title: str, content: str):
    """
    Ingest the document and generate its embedding.
    (For demo, generating a random embedding, replace with Chaitra's embedding logic)
    """
    embedding = np.random.rand(768)  # Replace with actual embedding generation
    doc_id = generate_doc_id()
    return doc_id, embedding

# A mock function to generate document IDs
def generate_doc_id():
    global doc_id_counter
    doc_id_counter += 1
    return doc_id_counter
