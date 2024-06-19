# assignment
# My FastAPI with Firestore Integration and CI/CD 

This project demonstrates a FastAPI application that integrates with Google Firestore.

## Installation

1. Clone the repository:
2. Install dependencies:
   pip3 install -r requirements.txt

## Running the application
1. Running app locally:

   uvicorn main:app --host 0.0.0.0 --port 8000


3. Running app with Docker:
   
     docker build -t test:v2 .
   
     docker run -p 8000:8000 test:v2


