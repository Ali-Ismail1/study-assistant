from fastapi import FastAPI , Form ,UploadFile,File ,HTTPException
from services.pdf_service import get_text
from storage.session_store import store_session_text,get_session_text
from fastapi.middleware.cors import CORSMiddleware
from services.ai_service import get_ai_summary , get_ai_quiz , get_ai_concepts 
import traceback
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app=FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (or specify your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_pdf_file (file : UploadFile = File(...)):
    try :
        pdf_text = await get_text(file)
        if not pdf_text.strip():
            raise HTTPException(status_code=400, detail="PDF contains no extractable text (it may be scanned/image-only).")
        session_id = store_session_text(pdf_text)
        return {"message": "file uploaded succesfully", "session_id": session_id}
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    

@app.post("/summary")
async def get_summary(session_id :str = Form(...)):
    text = get_session_text(session_id)
    if not text:
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        return get_ai_summary(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")

@app.post("/quiz")
async def get_quiz(session_id :str = Form(...)):
    text = get_session_text(session_id)
    if not text:
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        return get_ai_quiz(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")
@app.post("/concepts")
async def get_concepts(session_id :str = Form(...)):
    text = get_session_text(session_id)
    if not text:
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        return get_ai_concepts(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")
