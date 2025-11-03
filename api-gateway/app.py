from fastapi import FastAPI

app = FastAPI(title="API Gateway")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "api-gateway"}

@app.get("/gateway")
def gateway_info():
    return {"message": "API Gateway running"}
