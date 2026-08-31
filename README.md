# Study Assistant

An AI-powered tool that analyzes lecture PDFs and returns summaries, quiz questions, and key concepts to help students study more effectively.

## Live Demo
https://study-assistant-production-34ec.up.railway.app/
> **Note:** Hosted on Railway's free tier 

## Features
- Upload any lecture PDF
- Generate a concise summary
- Generate a 10-question quiz covering key topics
- Extract key concepts with detailed explanations

## Tech Stack
- **Backend:** FastAPI, Python
- **AI:** Google Gemini API
- **PDF Processing:** pypdf
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Ali-Ismail1/study-assistant.git
cd study-assistant
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the root directory and add your Gemini API key**
```
GEMINI_API_KEY=your_key_here
```

**5. Run the app**
```bash
uvicorn main:app --reload
```

**6. Open your browser at**
```
http://localhost:8000
```

## How to Use
1. Upload a lecture PDF using the file picker
2. Click **Summary** to get a concise overview of the content
3. Click **Quiz** to generate 10 practice questions
4. Click **Key Concepts** to get detailed explanations of the main topics

## Project Structure
```
study-assistant/
├── main.py                 # FastAPI app and routes
├── services/
│   ├── pdf_service.py      # PDF text extraction
│   └── ai_service.py       # Gemini API integration
├── models/
│   └── schemas.py          # Pydantic data models
├── static/
│   └── index.html          # Frontend
├── storage/
│   └── session_store.py    # Session management
├── .env                    # API keys — not committed
├── .gitignore
├── requirements.txt
└── README.md
```

## Author
Ali Ismail — Computer Engineering Student, Ain Shams University
