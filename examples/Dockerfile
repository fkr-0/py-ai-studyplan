# Session 08: package only the UI. Ollama runs separately.
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY chat_app.py .
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "chat_app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]
