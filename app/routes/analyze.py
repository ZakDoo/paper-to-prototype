from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.analyze_service import analyze_pdf

MAX_PDF_BYTES = 10 * 1024 * 1024

router = APIRouter(
    prefix="/analyze",
    tags=["analyze"],
)


@router.post("/")
async def analyze(pdf_file: UploadFile = File(...)):
    filename = (pdf_file.filename or "").lower()
    content_type = (pdf_file.content_type or "").lower()
    is_pdf = filename.endswith(".pdf") or content_type == "application/pdf"
    if not is_pdf:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    data = await pdf_file.read()
    if not data:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty.",
        )
    if len(data) > MAX_PDF_BYTES:
        raise HTTPException(
            status_code=400,
            detail="File is larger than 10 MB.",
        )

    return analyze_pdf(data)
