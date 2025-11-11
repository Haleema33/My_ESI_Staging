from fastapi import FastAPI

app = FastAPI(title="Auth Service",
              root_path="/api/gateway/auth")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "auth"}

@app.get("/auth-info")
def auth_score():
    return {"Auth": "auth service is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8084)