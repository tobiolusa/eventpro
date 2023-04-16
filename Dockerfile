FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /event_pro
WORKDIR /event_pro
ADD . /event_pro
RUN pip install -r requirements.txt