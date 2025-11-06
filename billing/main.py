from fastapi import FastAPI

app = FastAPI(title="Billing Service")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "billing"}

@app.get("/billing-info")
def get_billing_info():
    # Replace this with real billing logic later
    return {"billing": "sample data"}

@app.get("/")
def home():
    return {"message": "Billing microservice is up and running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)