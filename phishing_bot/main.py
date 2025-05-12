from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Path to your saved checkpoint
model_dir = "checkpoint-2630"

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir)
model.eval()  # Set model to evaluation mode

# Optional: Map predicted class IDs to human-readable labels
label_map = {0: "Not Phishing", 1: "Phishing"}


def predict(text):
    """Make a prediction on a single input text."""
    inputs = tokenizer(text, return_tensors="pt",
                       padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
    return predicted_class_id


if __name__ == "__main__":
    # Example phishing-style text
    text = "Dear user, your account has been compromised. Please verify your identity immediately by logging in here: http://secure-update-login.com/verify"

    prediction = predict(text)
    print(f"Predicted class ID: {prediction}")
    print(f"Predicted label: {label_map[prediction]}")
