FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN pip3 install firebase-admin
COPY assignment-d43d0-firebase-adminsdk-63mo0-76ceb5b9ea.json .env
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]