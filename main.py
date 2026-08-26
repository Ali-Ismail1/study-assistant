from fastapi import FastAPI , Form ,UploadFile,File ,HTTPException
from services.pdf_service import get_text
from storage.session_store import store_session_text
from services.ai_service import get_ai_summary , get_ai_quiz , get_ai_concepts 
app=FastAPI()
session_texts = {}
current_session_id = ""
current_session_text = ""

@app.get("/")
def read_root():
    return {"message": "Study Assistant API is running!"}

@app.post("/upload")
async def upload_pdf_file (file : UploadFile = File(...)):
    file_bytes = await file.read()
    try :
        pdf_text = get_text(file_bytes)
        current_session_dict = store_session_text(pdf_text)
        current_session_id = current_session_dict.key 
        current_session_text = current_session_dict.value
        session_texts[current_session_id] = current_session_text
        return {"message": "file uploaded succesfully"}
    except Exception as e :
        raise  HTTPException(status_code =400 , detail="Unsupported File Format ")
    

@app.post("/summary")
async def get_summary():
    return get_ai_summary(session_texts[current_session_id])

@app.post("/quiz")
async def get_quiz():
    return get_ai_quiz(session_texts[current_session_id])

@app.post("/concepts")
async def get_concepts():
    return get_ai_concepts(session_texts[current_session_id])