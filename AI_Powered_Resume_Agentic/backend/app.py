from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ai.enhancer import enhance_resume

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manual entry endpoint
@app.post("/enhance")
async def enhance(data: dict):
    improved = enhance_resume(data)
    return {"enhanced": improved}


# Upload resume endpoint
@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()

    # temporary simple text extraction
    text = content.decode("utf-8", errors="ignore")

    improved = enhance_resume(text)
    return {"enhanced": improved}
