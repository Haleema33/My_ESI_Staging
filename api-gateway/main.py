from fastapi import FastAPI, Request, Response
import httpx
import os

app = FastAPI(
    title="API Gateway",
    root_path="/api/gateway",   # VERY important for Ingress routing
    docs_url="/docs",           # Default Swagger UI path
    redoc_url=None,
    openapi_url="/openapi.json"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "api-gateway"}

@app.get("/gateway")
def gateway_info():
    return {"message": "API Gateway running"}

# Environment variables for internal microservices
BILLING_URL = os.getenv("BILLING_URL", "http://billing.staging.svc.cluster.local")
RISK_URL = os.getenv("RISK_URL", "http://risk.staging.svc.cluster.local")
SBOM_URL = os.getenv("SBOM_URL", "http://sbom.staging.svc.cluster.local")
SCANNER_URL = os.getenv("SCANNER_URL", "http://scanner.staging.svc.cluster.local")

# Helper function to forward requests
async def forward_request(url: str, request: Request):
    async with httpx.AsyncClient() as client:
        method = request.method
        body = await request.body()
        headers = dict(request.headers)
        response = await client.request(method, url, content=body, headers=headers)
        
        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.headers.get("content-type")
        )
# Example route for billing
@app.api_route("/billing/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def billing_proxy(path: str, request: Request):
    url = f"{BILLING_URL}/{path}"
    return await forward_request(url, request)

# Example route for risk
@app.api_route("/risk/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def risk_proxy(path: str, request: Request):
    url = f"{RISK_URL}/{path}"
    return await forward_request(url, request)

# Example route for sbom
@app.api_route("/sbom/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def sbom_proxy(path: str, request: Request):
    url = f"{SBOM_URL}/{path}"
    return await forward_request(url, request)

# Example route for scanner
@app.api_route("/scanner/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def scanner_proxy(path: str, request: Request):
    url = f"{SCANNER_URL}/{path}"
    return await forward_request(url, request)
