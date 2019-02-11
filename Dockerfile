FROM python:3

ADD fortunescrapper.py /

RUN pip install random

CMD [ "python", "./fortunescrapper.py" ]
