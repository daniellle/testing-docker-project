# web/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install Flask and psycopg2 to connect to PostgreSQL
RUN pip install flask psycopg2

# Copy the Flask app code
COPY app.py .

# Run the Flask app
CMD ["python", "app.py"]
