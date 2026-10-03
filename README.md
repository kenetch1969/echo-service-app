# Echo Service DevOps

A simple echo service with complete DevOps pipeline.

## Structure

- `app/` - Python application source code
- `docker/` - Docker container definition
- `terraform/` - AWS infrastructure as code
- `.github/workflows/` - CI/CD pipelines

## Quick Start

```bash
# Run locally
cd app && pip install -r requirements.txt && python main.py

# Build Docker image
docker build -t echo-service -f docker/Dockerfile .

# Deploy infrastructure
cd terraform && terraform init && terraform apply
```