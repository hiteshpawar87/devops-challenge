# DevOps Challenge – SimpleTimeService ⏱️

This repository contains a complete DevOps pipeline solution for deploying a minimal Python-based REST API ("SimpleTimeService") using containerization, CI/CD, Helm charts, and Open Policy Agent (OPA) enforcement.

---

## 📌 Project Goals

- Build a Python API that returns current server time and client IP
- Containerize the application using Docker
- Set up CI/CD using GitHub Actions
- Deploy to Kubernetes using Helm
- Enforce policies using OPA (e.g., prevent root containers)
- Follow DevOps best practices (non-root user, IaC, GitOps)

---

## 🧱 Folder Structure

devops-challenge/
├── app/ # Python app (SimpleTimeService)
│ ├── main.py
│ └── requirements.txt
│
├── .github/workflows/ # GitHub Actions CI/CD pipeline
│ └── ci.yml
│
├── Dockerfile # Dockerfile for the app
├── .dockerignore
├── .gitignore
│
├── helm/ # Helm chart to deploy app
│ └── simpletimeservice/
│ ├── Chart.yaml
│ ├── values.yaml
│ └── templates/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ingress.yaml
│
├── opa/ # OPA policy to enforce security
│ └── policy.rego
│
├── k8s/ # Optional raw manifests
│ └── namespace.yaml
│
└── README.md # You are here


---

## 🚀 SimpleTimeService API

A minimal Flask API that returns server time and client IP address.

### Example Response
```json
{
  "timestamp": "2025-08-07T10:30:00Z",
  "client_ip": "123.45.67.89"
}



🐳 Docker Usage
Build and run locally:

docker build -t simpletimeservice .
docker run -p 5000:5000 simpletimeservice
Pull from DockerHub:

docker pull hiteshpawar87/simpletimeservice:latest
docker run -p 5000:5000 hiteshpawar87/simpletimeservice


🔁 CI/CD Pipeline
GitHub Actions Workflow (.github/workflows/ci.yml) performs:

Python dependency installation
Unit tests (if any)
Docker image build & push to DockerHub

Secrets required:

DOCKER_USERNAME
DOCKER_PASSWORD

☸️ Kubernetes Deployment
Using Helm
helm upgrade --install simpletimeservice helm/simpletimeservice \
  --namespace devops-challenge --create-namespace

Direct K8s manifest
kubectl apply -f k8s/namespace.yaml
kubectl apply -f helm/simpletimeservice/templates/


🔐 OPA Policy
OPA policy (opa/policy.rego) ensures pods do not run as root. Integrate with Gatekeeper or OPA admission controller.

✅ Best Practices Followed
✅ Non-root Docker user
✅ Small Python image (based on python:3.10-slim)
✅ CI/CD via GitHub Actions
✅ Reusable Helm chart
✅ Policy-as-code with OPA


👤 Author
Hitesh Pawar
GitHub • Credly
AWS Certified DevOps Engineer – Professional


