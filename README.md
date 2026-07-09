# Cloud Resource Inventory Manager | End-to-End CI/CD Pipeline

## Overview

This project is a cloud-native Flask application with a MySQL database. It demonstrates how a web application can be containerized using Docker, automatically built and pushed to Amazon ECR using GitHub Actions, and deployed on Kubernetes.

The application allows users to add and manage cloud resources through a simple web interface. All resource information is stored in a MySQL database running inside Kubernetes.

The main objective of this project was to gain hands-on experience with the complete DevOps workflow, including containerization, CI/CD, Kubernetes deployment, and troubleshooting real-world deployment issues.

---

## Technologies Used

- Python
- Flask
- MySQL
- Docker
- Kubernetes (Minikube)
- Git
- GitHub
- GitHub Actions
- AWS ECR
- Linux

---

## Project Architecture

```
                Developer
                    │
                    ▼
             GitHub Repository
                    │
                    ▼
            GitHub Actions (CI)
                    │
                    ▼
          Build Docker Image
                    │
                    ▼
            Push Image to AWS ECR
                    │
                    ▼
          Kubernetes Cluster (Minikube)
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Flask Deployment        MySQL Deployment
        │                       │
        ▼                       ▼
 Flask Service          MySQL Service
```

---

## Features

- Flask web application for managing cloud resources
- MySQL database integration
- Dockerized application
- Automated Docker image build using GitHub Actions
- Docker image pushed to Amazon ECR
- Kubernetes Deployments and Services
- ConfigMap for application configuration
- Kubernetes Secret for sensitive information
- MySQL deployed inside Kubernetes
- End-to-end CI/CD workflow

---

## Folder Structure

```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yml
│   ├── configmap.yml
│   ├── secret.yml
│   ├── mysql-deployment.yaml
│   └── mysql-service.yaml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
└── README.md
```

---

## Deployment Workflow

1. Developed the Flask application.
2. Containerized the application using Docker.
3. Configured GitHub Actions to build the Docker image automatically.
4. Pushed the Docker image to Amazon ECR.
5. Created Kubernetes Deployments and Services.
6. Configured ConfigMaps and Secrets.
7. Deployed both Flask and MySQL on Kubernetes.
8. Verified the application using Minikube.

---

## What I Learned

This project helped me gain practical experience with:

- Building Docker images
- Writing GitHub Actions workflows
- Using Amazon ECR as a private container registry
- Kubernetes Deployments
- Kubernetes Services
- ConfigMaps
- Secrets
- Deploying MySQL on Kubernetes
- Connecting Flask with MySQL
- Kubernetes networking
- Debugging Kubernetes applications

---

## Challenges I Solved

While working on this project, I encountered and resolved several real-world deployment issues:

- ImagePullBackOff
- ErrImagePull
- CrashLoopBackOff
- Expired Amazon ECR authentication token
- Kubernetes Secret configuration issues
- ConfigMap configuration errors
- MySQL connection failures
- Missing database tables
- Database schema mismatches
- Kubernetes Service configuration issues

Resolving these issues gave me practical experience in troubleshooting containerized applications running on Kubernetes.

⭐ If you found this project helpful, feel free to star this repository.


# Cloud Resource Inventory Manager | End-to-End CI/CD Pipeline

## Overview

This project is a cloud-native Flask application with a MySQL database. It demonstrates how a web application can be containerized using Docker, automatically built and pushed to Amazon ECR using GitHub Actions, and deployed on Kubernetes.

The application allows users to add and manage cloud resources through a simple web interface. All resource information is stored in a MySQL database running inside Kubernetes.

The main objective of this project was to gain hands-on experience with the complete DevOps workflow, including containerization, CI/CD, Kubernetes deployment, and troubleshooting real-world deployment issues.

---

## Technologies Used

- Python
- Flask
- MySQL
- Docker
- Kubernetes (Minikube)
- Git
- GitHub
- GitHub Actions
- AWS ECR
- Linux

---

## Project Architecture

```
                Developer
                    │
                    ▼
             GitHub Repository
                    │
                    ▼
            GitHub Actions (CI)
                    │
                    ▼
          Build Docker Image
                    │
                    ▼
            Push Image to AWS ECR
                    │
                    ▼
          Kubernetes Cluster (Minikube)
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Flask Deployment        MySQL Deployment
        │                       │
        ▼                       ▼
 Flask Service          MySQL Service
```

---

## Features

- Flask web application for managing cloud resources
- MySQL database integration
- Dockerized application
- Automated Docker image build using GitHub Actions
- Docker image pushed to Amazon ECR
- Kubernetes Deployments and Services
- ConfigMap for application configuration
- Kubernetes Secret for sensitive information
- MySQL deployed inside Kubernetes
- End-to-end CI/CD workflow

---

## Folder Structure

```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yml
│   ├── configmap.yml
│   ├── secret.yml
│   ├── mysql-deployment.yaml
│   └── mysql-service.yaml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
└── README.md
```

---

## Deployment Workflow

1. Developed the Flask application.
2. Containerized the application using Docker.
3. Configured GitHub Actions to build the Docker image automatically.
4. Pushed the Docker image to Amazon ECR.
5. Created Kubernetes Deployments and Services.
6. Configured ConfigMaps and Secrets.
7. Deployed both Flask and MySQL on Kubernetes.
8. Verified the application using Minikube.

---

## What I Learned

This project helped me gain practical experience with:

- Building Docker images
- Writing GitHub Actions workflows
- Using Amazon ECR as a private container registry
- Kubernetes Deployments
- Kubernetes Services
- ConfigMaps
- Secrets
- Deploying MySQL on Kubernetes
- Connecting Flask with MySQL
- Kubernetes networking
- Debugging Kubernetes applications

---

## Challenges I Solved

While working on this project, I encountered and resolved several real-world deployment issues:

- ImagePullBackOff
- ErrImagePull
- CrashLoopBackOff
- Expired Amazon ECR authentication token
- Kubernetes Secret configuration issues
- ConfigMap configuration errors
- MySQL connection failures
- Missing database tables
- Database schema mismatches
- Kubernetes Service configuration issues

Resolving these issues gave me practical experience in troubleshooting containerized applications running on Kubernetes.

⭐ If you found this project helpful, feel free to star this repository.
