from fastapi import FastAPI
from app.api.routes import router
app = FastAPI(
    
    title="Enterprise RAG Assistant",
    description="AI-powered enterprise knowledge assistant using RAG architecture",
    version="1.0.0"
)
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Assistant is running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }