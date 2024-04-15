FROM python:3.10

WORKDIR InternshipMeduzzen

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]