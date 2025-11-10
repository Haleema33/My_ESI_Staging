from fastapi import FastAPI

app = FastAPI(title="SBOM Service",
              root_path="/api/gateway/sbom")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "sbom"}

@app.get("/sbom-list")
def sbom_list():
    return {"sbom": ["package1", "package2"]}
