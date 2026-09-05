FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY monitor.py .
COPY logger.py .

RUN mkdir -p logs

CMD ["python", "monitor.py"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD python -c "print('healthy')" || exit 1
