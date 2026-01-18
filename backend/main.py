from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Simple CI/CD Demo API")

# In this setup, frontend calls same-origin (/api/...),
# so CORS isn't strictly required, but it's common to show it.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

APP_VERSION = os.getenv("APP_VERSION", "dev")

@app.get("/health")
def health():
    return {"status": "ok", "version": APP_VERSION}

@app.get("/hello")
def hello():
    return {
        "message": "Hello from the backend API!",
        "version": APP_VERSION
    }
