# 🧩 MyESI — Microservices Staging Environment

The MyESI Staging Environment hosts multiple microservices working together to deliver a modular, scalable system architecture. This environment is deployed on Kubernetes and uses Docker images stored in GitHub Container Registry (GHCR).

---

## 🌐 Accessing the Services

All services are available under the same domain:

https://staging.myesi.local

Each service exposes interactive Swagger docs at the URLs below.

| Service | Swagger Docs URL | Description |
|---|---|---|
| 🌀 API Gateway | https://staging.myesi.local/api/gateway/docs | Main routing layer handling requests between services |
| 💳 Billing Service | https://staging.myesi.local/api/billing/docs | Handles payments and invoice management |
| 🧠 Risk Analysis Service | https://staging.myesi.local/api/risk/docs | Performs risk computations for uploaded artifacts |
| 🧾 SBOM Service | https://staging.myesi.local/api/sbom/docs | Generates and manages Software Bill of Materials |
| 🔍 Scanner Service | https://staging.myesi.local/api/scanner/docs | Scans dependencies for vulnerabilities |
| 🔐 Auth Service | https://staging.myesi.local/api/auth/docs | Handles user authentication and JWT management |

---

## 🗄️ Database Architecture

Two PostgreSQL databases are configured for this staging setup:

| Database | Purpose | Used By |
|---|---|---|
| 🧾 postgres-billing | Dedicated for Billing microservice | billing |
| 🧩 postgres-shared | Shared among all other microservices | auth, risk, sbom, scanner, api-gateway |

Database credentials are stored securely using Kubernetes Secrets and are accessed via the `DATABASE_URL` environment variable in each service’s deployment.

---

## ⚙️ Deployment Overview

Each microservice runs as a Kubernetes `Deployment` and exposes a `ClusterIP` `Service` under the `staging` namespace. An NGINX Ingress controller routes external requests to the appropriate service using domain-based paths.

Example commands:

```bash
# View running pods
kubectl get pods -n staging

# View service endpoints
kubectl get svc -n staging
```

To restart a deployment so it pulls a new image:

```bash
kubectl rollout restart deployment <service-name> -n staging

# Example:
kubectl rollout restart deployment api-gateway -n staging
```

Check rollout status:

```bash
kubectl rollout status deployment <service-name> -n staging
```

If `imagePullSecrets` were recently updated:

```bash
kubectl patch deployment <service-name> -n staging -p '{"spec":{"template":{"spec":{"imagePullSecrets":[{"name":"ghcr-login"}]}}}}'
```

---

## 🧰 Updating Docker Images (GHCR)

When you make code changes, build and push a new image to GHCR:

```bash
# Login to GHCR
docker login ghcr.io -u <your-github-username> -p <your-personal-access-token>

# Build and push updated image
docker build -t ghcr.io/<org>/<service>:latest ./<service>
docker push ghcr.io/<org>/<service>:latest
```

Then restart the corresponding deployment in Kubernetes (example above) so the new image is pulled.

---

## 🧩 Environment Variables

Each service uses environment variables defined in Kubernetes manifests. Common variables:

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `JWT_SECRET` | Secret key for authentication |
| `STRIPE_SECRET_KEY` | Used for payment gateway integration |
| `SERVICE_PORT` | Internal service port |
| `BILLING_URL`, `RISK_URL`, etc. | Service interconnections for API Gateway |

Secrets and sensitive values should be stored in Kubernetes `Secrets` (not committed to source control).

---

## 🚀 Accessing Swagger Docs

All services expose interactive Swagger documentation for API testing and exploration. Open any of the following in a browser:

- https://staging.myesi.local/api/gateway/docs
- https://staging.myesi.local/api/gateway/billing/docs
- https://staging.myesi.local/api/gateway/risk/docs
- https://staging.myesi.local/api/gateway/sbom/docs
- https://staging.myesi.local/api/gateway/scanner/docs
- https://staging.myesi.local/api/gateway/auth/docs

You can also view gateway-level aggregated docs or nested docs, for example:

https://staging.myesi.local/api/gateway/docs#/scanner/docs

---

## 🧩 Health Checks

Check service status via health endpoints, for example:

```bash
curl https://staging.myesi.local/api/gateway/health
```

Expected response:

```json
{"status": "ok", "service": "api-gateway"}
```

Each microservice should expose a similar `/health` endpoint that returns a small JSON payload indicating status.

---

## 📦 Directory Structure (Simplified)

```
MyESI_Staging/
├── api-gateway/
├── auth/
├── billing/
├── risk/
├── sbom/
├── scanner/
├── manifests/
```

- `manifests/` contains Kubernetes Deployment, Service, Ingress, and Secret manifests for the staging environment.
- Each service folder contains source code and a Dockerfile for building the service image.

---

## 🧩 Summary

- ✅ MyESI is fully containerized and deployed on Kubernetes  
- ✅ Each service is independently scalable and reachable via staging URLs  
- ✅ Two PostgreSQL databases (billing + shared) support a modular design  
- ✅ Swagger docs available for all endpoints

---
