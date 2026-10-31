import os
from dotenv import load_dotenv

load_dotenv(".env")

PROVIDER = os.getenv("PROVIDER","Ollama")
MODEL = os.getenv("DRAFT-PILOT_LLM_MODEL","gemini-3.5-flash-lite")
API_KEY = os.getenv("GOOGLE_GENAI_API_KEY","")
DB_URI = os.getenv("DB_URI", "")


if PROVIDER == "google_genai" and os.getenv("GOOGLE_GENAI_API_KEY", "") == "":
    raise SystemExit("PROVIDER is google_genai but GOOGLE_API_KEY is empty. " \
    "Add it to your .env file.")