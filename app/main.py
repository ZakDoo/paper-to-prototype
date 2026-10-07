from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.routes import analyze

WEB_DIR = Path(__file__).resolve().parents[1] / "web"

app = FastAPI(
    title="Paper To Prototype API",
    version="1.0.0",
)

app.include_router(analyze.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def index():
    return FileResponse(WEB_DIR / "index.html")
