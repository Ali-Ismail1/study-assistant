import uuid

session_store = {}

def store_session_text(text: str):
    session_id = str(uuid.uuid4())
    session_store[session_id] = text
    return session_id

def get_session_text(session_id: str):
    return session_store.get(session_id)