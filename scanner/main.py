from fastapi import FastAPI

app = FastAPI(title="Scanner Service")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "scanner"}

@app.get("/scan")
def scan_info():
    return {"scan": "scan results will go here"}
