FROM python:3.7-buster

WORKDIR /root

COPY training.py /root/training.py
COPY requirements.txt /root/requirements.txt

RUN pip install -r /root/requirements.txt --no-cache-dir

ENTRYPOINT ["python", "training.py"]
