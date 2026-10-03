from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Echo Service API", version="1.0.0")

class EchoMessage(BaseModel):
    message: str

@app.get("/health", status_code=200)
def health_check():
    """Endpoint para Health Check de AWS ALB / ECS"""
    return {"status": "healthy"}

@app.post("/echo")
def echo(payload: EchoMessage):
    """Endpoint principal que regresa lo enviado"""
    return {"echo": payload.message}