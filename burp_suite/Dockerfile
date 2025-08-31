FROM python:alpine3.21
WORKDIR /portal
COPY application ./
COPY requirements.txt ./
COPY run.py ./
RUN pip3 install -r requirements.txt

CMD [ "python3" "run.py" ]