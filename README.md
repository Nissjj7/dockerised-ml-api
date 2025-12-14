# Dockerised ML API #

## Overview

This project demonstrates how a machine learning model can be deployed as a RESTful API using Python, Flask, and Docker. The application exposes a prediction endpoint that loads a pre-trained model and returns inference results via HTTP requests. The entire system is containerised to ensure consistent and reproducible execution across environments.


## Problem Statement
Machine learning models are often developed in isolation but face challenges when moving to production, such as:
* Environment inconsistencies
* Manual dependency management
* Lack of standardised deployment interfaces
This project addresses these challenges by packaging a trained ML model into a containerised web service that can be deployed reliably across development, testing, and production environments.

## Solution Architecture
The solution follows a modular deployment architecture:
<**1. Model Training**> – A simple ML model is trained and persisted using pickle.
<**2. Inference Layer**> – A Flask API loads the trained model and exposes prediction endpoints.
<**3. Containerisation**> – Docker packages the application and its dependencies into a portable image.
<**4. Deployment Ready**> – The container can be deployed locally, on cloud platforms, or in CI/CD pipelines.


## Technologies Used
• Programming Language: Python
• Web Framework: Flask
• Machine Learning: Scikit-learn
• Containerisation: Docker
• Data Handling: NumPy, Pandas
• Version Control: Git, GitHub


## Project Structure
dockerised-ml-api/
├── app/
│   ├── app.py          # Flask API
│   └── model.py        # Model loading and prediction logic
├── model/
│   ├── train_model.py  # Model training script
│   └── trained_model.pkl
├── requirements.txt
├── Dockerfile
└── README.md

## API Endpoints
## Health Check
## GET /health
Response:
{
  "status": "API is running"
}

## Prediction Endpoint
## POST /predict
Request Body:
{
  "features": [25, 3]
}

Response:
{
  "prediction": 0
}


## Running the Application with Docker
## Build the Docker Image

docker build -t dockerised-ml-api .


## Run the Container
docker run -p 5000:5000 dockerised-ml-api

The API will be available at:
http://localhost:5000


## Logging and Error Handling
• Application-level logging is implemented for API requests and prediction flow.
• Input validation ensures robust handling of invalid requests.
• Clear HTTP status codes are returned for success and error scenarios.


## Future Enhancements
• Model versioning and registry integration
• Authentication and rate limiting
• 8CI/CD pipeline for automated builds
• Cloud deployment using Azure Container Apps or Kubernetes


## Author
### Nissiya Thomas
MSc Advanced Computer Science – University of Liverpool
