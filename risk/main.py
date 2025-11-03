from fastapi import FastAPI

app = FastAPI(title="Risk Service")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "risk"}

@app.get("/risk-score")
def risk_score():
    return {"risk": "sample risk score"}
