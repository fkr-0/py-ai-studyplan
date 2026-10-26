FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt
COPY chat_app.py chat_logic.py /app/
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "chat_app.py", "--server.address=0.0.0.0", "--server.port=8501", "--browser.gatherUsageStats=false"]
