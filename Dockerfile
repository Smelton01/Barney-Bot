FROM ubuntu:latest
COPY requirements.txt /tmp

COPY config.py /app/
COPY lines.txt /app/
COPY checkpoint/model-26000.pth /app/ 

RUN apt-get update && apt-get -y install python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
RUN pip3 install --no-cache-dir torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY simple_bot.py /app/
COPY rnn_bot.py /app/

WORKDIR /app
CMD ["python3", "simple_bot.py"]
