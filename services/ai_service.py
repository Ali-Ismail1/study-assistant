from google import genai
import os 
import dotenv
from dotenv import load_dotenv
load_dotenv(os.path.join(os.getcwd(), ".env"))

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

client = genai.Client(api_key = api_key)

def get_ai_summary(pdf_text : str ):
    final_prompt = f'Provide a detailed summary for the following text ( summary must be shorter than original text length): \n {pdf_text}'
    try:
        ai_result = client.models.generate_content(
            model = "gemini-3.6-flash", 
            contents = final_prompt
            )
        return {"summary": ai_result.text}
    except Exception as e:
        raise ValueError(f"Gemini API error: {str(e)}")
def get_ai_quiz(pdf_text : str ):
    final_prompt = f'Generate a 10 question quiz covering the key ropics in the following text , the questions may be mcq , article , true or false etc ... : \n {pdf_text}'
    try:
        ai_result = client.models.generate_content(
            model = "gemini-3.6-flash", 
            contents = final_prompt
            )
        return {"quiz": ai_result.text}
    except Exception as e:
        raise ValueError(f"Gemini API error: {str(e)}")
def get_ai_concepts (pdf_text : str ):
    final_prompt = f'state the key concepts and Provide an explanation for each from  the following text  with refrence to samples from the text during explanation of key concepts : \n {pdf_text}'
    try:
        ai_result = client.models.generate_content(
            model = "gemini-3.6-flash", 
            contents = final_prompt
            )
        return {"key_concepts": ai_result.text}
    except Exception as e:
        raise ValueError(f"Gemini API error: {str(e)}")


