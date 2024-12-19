FROM python:3.12.8-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["python3.12", "-B", "main.py"]