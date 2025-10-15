### DevOps Basic Flask Project
# Overview
A basic Flask project demonstrating core DevOps concepts: containerization with Docker, orchestration using Kubernetes, integration with AWS ECR for images, and automated CI/CD deployment. The project follows best practices for monitoring, scaling, and IaC management.github​
**Features**
	• Simple Flask web application—serves as a template for microservices
	• Dockerized for easy container management
	• Kubernetes manifests/Helm charts for deployment
	• AWS ECR integration for storing Docker images
	• Basic monitoring/alerting setup

**Architecture**

User → Flask App (Docker) →[Kubernetes → AWS ECR (CI/CD) → Monitoring

# Project Structure

/ (root)
├── app/            # Flask app code
├── k8s/            # Kubernetes manifests
├── helm-chart/     # Helm deployment templates
├── Dockerfile
├── requirements.txt
├── .github/
└── README.md


**Prerequisites**
	• Docker (vXX+)
	• Python 3.8+
	• kubectl
	• AWS CLI configured for ECR access
	• Helm (for templated deployments)
# Getting Started
	1. Clone the repository:
	bash
	git clone https://github.com/SREEKANTH257/DevOps-basic-flask-project.git
	cd DevOps-basic-flask-project
	2. Install dependencies:
	bash
	pip install -r requirements.txt
	3. Run locally:
	bash
	python main.py
	flask run

The app will run locally at http://localhost:5000/.
	
# Docker Usage
	• **Build the image**:
	bash
	docker build -t flask-devops-app .
	• Run the container:
	bash
	docker run -p 5000:5000 flask-devops-app
	**Kubernetes Deployment**
	• Apply manifests:
	bash
	kubectl apply -f k8s/
	• Helm install:
	bash
	helm install flask-app ./helm-chart/
# CI/CD Pipeline
	• The project includes a sample GitHub Actions workflow for continuous integration and automated Docker image deployment to AWS ECR.
	• Configurations are found in .github/workflows/.
**Monitoring & Logging**
	• Integrated with Prometheus and Grafana for metrics collection and alerting.
	• Logs can be accessed via Kubernetes dashboard or kubectl logs.

# Acknowledgements
I was inspired by the daily tasks and hands-on experiences I gained in my previous roles, where I worked extensively with Flask, Docker, Kubernetes, and AWS. These technologies were integral to my day-to-day responsibilities, and I used them to build and deploy scalable applications. By leveraging these tools, I was able to showcase my expertise in modern DevOps best practices and cloud-native development.

# Contributing
Pull requests and contributions are welcome—please open an issue to discuss changes or major features in advance.>
