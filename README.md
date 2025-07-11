
# SmartOps.AI – Full-Stack Automation Portal using Azure, Power Automate, and Python

This project demonstrates an AI-augmented automation platform using Microsoft Azure, Power Automate, and a Python backend with FastAPI and Azure Functions.

---

## 🔧 Tech Stack

- **Backend**: FastAPI (Python)
- **Automation**: Power Automate, Azure Logic Apps
- **ML Serving**: Azure Function using ONNX model
- **Cloud**: Azure App Services, Blob Storage, Cosmos DB
- **DevOps**: GitHub Actions, ARM/Bicep Templates

---

## 📁 Project Structure

```
SmartOps.AI/
├── backend/
│   └── api/
│       ├── main.py
│       ├── routes/
│       │   ├── tickets.py
│       │   └── onboarding.py
│       └── requirements.txt
├── functions/
│   └── ml_scorer/
│       ├── __init__.py
│       ├── function.json
│       ├── requirements.txt
│       └── model.onnx (you must generate this)
├── README.md
```

---

## 🚀 Setup Instructions

### 🔹 1. Backend API (FastAPI)
```bash
cd backend/api
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit `http://localhost:8000/docs` for Swagger UI.

---

### 🔹 2. Azure Function (ML Scorer)
```bash
cd functions/ml_scorer
pip install -r requirements.txt
# Start function locally
func start
```

*Note: Generate a dummy model using `generate_model.py` script provided earlier.*

---

### 🔹 3. Model Input Example
Send POST to `http://localhost:<function_port>/api/score`:
```json
{
  "text": "User cannot access email"
}
```

---

## 📦 Author

**Nikita Sinha**  
System Engineer (AI) | Indiana University  
Software Developer | Keelworks Foundation  
