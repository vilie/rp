FROM python:2.7.11

RUN pip install -U flask pymongo praw

ENV PYTHONPATH=/usr/share/
COPY bot /usr/share/bot
COPY db /usr/share/db
CMD python /usr/share/bot/bot.py
