from pydantic import BaseModel

# Model representing the structure of a document
class Document(BaseModel):
    title: str
    content: str
