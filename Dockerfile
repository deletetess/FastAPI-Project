FROM python3.12-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["python3.12", "-B", "main.py"]