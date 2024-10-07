from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import spacy
from extractor import EntityExtractor

app = FastAPI()

nlp = spacy.load("../chapter_08/pipelines/fashion_ner_with_base_entities")
extractor = EntityExtractor(nlp)

class TextToExtractEntities(BaseModel):
    record_id: str
    text: str

class TextsRequest(BaseModel):
    values: List[TextToExtractEntities]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/entities")
def extract_entities(body: TextsRequest):
    """Extract Named Entities from a batch of Records."""
    documents = []

    for item in body.values:
        documents.append({"record_id": item.record_id, "text": item.text})

    entities_result = extractor.extract_entities(documents)

    response = [
        {"record_id": er["record_id"], "data": {"entities": er["entities"]}}
        for er in entities_result
    ]

    return {"values": response}