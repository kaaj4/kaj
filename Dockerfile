FROM python:latest
RUN mkdir /iqthon
WORKDIR /iqthon
COPY requirements.txt /iqthon
RUN pip3 install -r requirements.txt
COPY . /iqthon
CMD ["python3","-m","iqthon"]
