#01 - Get lightweight Python image
FROM python:3.11-alpine

#02 - Define working directory
WORKDIR /app

#03 - Copy project files
COPY requirements.txt .

#04 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#05 Copy script
COPY app.py .

#06 Specify entry point
ENTRYPOINT ["python", "app.py"]