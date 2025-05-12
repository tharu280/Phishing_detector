from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()


model_name = "tharu280/phishing-detector"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()


label_map = {0: "Not Phishing", 1: "Phishing"}


class TextInput(BaseModel):
    text: str


def predict(text):
    inputs = tokenizer(text, return_tensors="pt",
                       padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
    return predicted_class_id


@app.post("/predict")
def classify_text(input: TextInput):
    class_id = predict(input.text)
    label = label_map[class_id]
    return {"class_id": class_id, "label": label}
