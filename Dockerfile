# 1. Use an official, lightweight Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependencies file to the working directory
COPY requirements.txt .

# 4. Install the Python packages inside the container environment
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your local source code into the container
COPY . .

# 6. Inform Docker that the container listens on ports 8501 and 8000
EXPOSE 8501 8000

# 7. Default command (can be overridden by docker-compose)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]