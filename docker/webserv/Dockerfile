FROM python:2.7.11

RUN pip install -U flask pymongo praw

ENV PYTHONPATH=/usr/share/
COPY web /usr/share/web
COPY db /usr/share/db
CMD python /usr/share/web/web.py
