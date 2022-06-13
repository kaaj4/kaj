FROM python:latest
RUN mkdir /kaj
WORKDIR /kaj
COPY requirements.txt /kaj
RUN pip3 install -r requirements.txt
COPY . /kaj
CMD ["python3","-m","kaj"]
