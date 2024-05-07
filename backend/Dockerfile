FROM python:3.12

RUN mkdir /usr/src/pytrade

COPY main.py /usr/src/pytrade

COPY requirements.txt /usr/src/pytrade

WORKDIR /usr/src/pytrade

RUN pip install -r requirements.txt

CMD ["python", ".main.py"]