def analyze_pdf(pdf_file: bytes) -> dict:
    """Stub response so the webpage can render before the pipeline exists."""
    _ = pdf_file
    return {
        "research_question": (
            "How can a research paper be turned into a concrete "
            "prototype plan with method, dataset, and baseline "
            "details extracted automatically?"
        ),
        "method": (
            "Parse the PDF into sections, then run sequential LLM "
            "extractors for research question, method, dataset, "
            "and experiments/baselines."
        ),
        "dataset": "not stated in the paper",
        "baseline": "not stated in the paper",
        "implementation_plan": [
            "Serve the upload page and accept a PDF at POST /analyze/.",
            "Extract text with PyMuPDF and split common paper headings.",
            "Call Groq extractors one section at a time, then build the plan.",
            "Deploy the Docker image on a free host with GROQ_API_KEY set.",
        ],
    }
