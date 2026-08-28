# DevOps Project 1 — Automated CI/CD Pipeline

![Deploy Status](https://github.com/endeedslap/devops-project-1/actions/workflows/deploy.yml/badge.svg)

## What This Project Does
A fully automated CI/CD pipeline that deploys a Python web application 
to AWS EC2 every time code is pushed to GitHub — no manual steps required.

## Live Demo
http://18.218.70.33:5000

## Tech Stack
| Tool | Purpose |
|---|---|
| Python Flask | Web application |
| Docker | Containerization |
| GitHub Actions | CI/CD automation |
| AWS EC2 | Cloud hosting |
| Ubuntu 22.04 | Server OS |

## How It Works
1. Developer pushes code to GitHub
2. GitHub Actions automatically triggers
3. Docker builds a container image
4. Image is shipped to AWS EC2
5. App restarts with new version live

## Pipeline Steps
- **Checkout** — pulls latest code
- **Build** — creates Docker image
- **Save** — compresses image file
- **Copy** — sends image to AWS server
- **Deploy** — stops old container, starts new one

## Skills Demonstrated
- CI/CD pipeline design and implementation
- Docker containerization
- Cloud deployment on AWS EC2
- Linux server administration
- GitHub Actions automation
- Security group configuration
- SSH key authentication

## How to Run Locally
```bash
git clone https://github.com/endeedslap/devops-project-1.git
cd devops-project-1
pip install -r requirements.txt
python app.py
```
Open browser → http://localhost:5000
