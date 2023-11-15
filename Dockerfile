FROM python:3.11
COPY MerakiAPI.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "MerakiAPI.py"]
