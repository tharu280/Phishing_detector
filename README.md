
# Phishing Link Detector API

This project is a **Phishing Link Detector** API built using a fine-tuned BERT model hosted on Hugging Face and served via FastAPI. It classifies text input as either **Phishing** or **Not Phishing**.

---

## Features

- Fine-tuned z BERT model for phishing detection.
- Easy-to-use REST API endpoint to classify URLs or text.
- Fast and efficient inference using Hugging Face Transformers and PyTorch.
- Simple JSON input/output interface.

---

## Model

The model is based on the **BERT** architecture and fine-tuned on a phishing detection dataset. It is publicly available on Hugging Face Hub:

- Model repo: [`tharu280/phishing-detector`](https://huggingface.co/tharu280/phishing-detector)

---

## API Usage

### Start the FastAPI server

```bash
uvicorn main:app --reload
```


### POST `/predict`

Classify whether the input text is phishing or not.

- **Request Body** (JSON):

  ```json
  {
    "text": "http://example.com/login"
  }
  ```

- **Response** (JSON):

  ```json
  {
    "class_id": 1,
    "label": "Phishing"
  }
  ```

---


## Requirements

- Python 3.8+
- FastAPI
- Transformers
- PyTorch
- Uvicorn (for running the server)

Install dependencies with:

```bash
pip install fastapi transformers torch uvicorn
```

---

## How to Use

1. Clone the repo or copy the code.
2. Install dependencies.
3. Run the FastAPI server with Uvicorn.
4. Use any HTTP client (Postman, curl) or build your frontend to send POST requests to `/predict`.

---

## Future Improvements

- Add URL preprocessing and validation.
- Expand dataset and retrain for better accuracy.
- Add batch predictions.
- Dockerize the app for easier deployment.
- Add a frontend UI for quick testing.

---

## License

MIT License.
