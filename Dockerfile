FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8051

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]