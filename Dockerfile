FROM python:3.7-alpine
COPY requirements.txt /tmp

COPY Barney_bot/config.py /bots/
COPY Barney_bot/simple_bot.py /bots/
COPY keys.py /bots

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "simple_bot.py"]