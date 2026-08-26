import uuid

def store_session_text (text:str):
    session_text = {}
    session_id = str(uuid.uuid4())
    session_text[session_id] = text
    return session_text
