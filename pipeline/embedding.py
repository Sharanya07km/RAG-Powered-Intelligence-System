from transformers import AutoModel, AutoTokenizer
import torch

class DocumentEmbedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    
    def embed(self, text: str):
        # Tokenize input text
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            # Get the embeddings from the transformer model
            embeddings = self.model(**inputs).last_hidden_state.mean(dim=1)
        return embeddings.squeeze().numpy()

# Example usage
embedder = DocumentEmbedder()
embedding = embedder.embed("This is a sample document content")

# embedding.py
# embedding.py
from sentence_transformers import SentenceTransformer

def create_embeddings(documents):
    print("[INFO] Starting document embedding...")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(documents)
    print(f"[INFO] Successfully embedded {len(documents)} documents.")
    return embeddings

if __name__ == "__main__":
    documents = ["Example text 1", "Example text 2", "Example text 3"]
    embeddings = create_embeddings(documents)
    print("[INFO] Embeddings created:", embeddings)

