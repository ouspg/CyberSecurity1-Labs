FROM python:alpine3.10

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    python3-dev \
    make

WORKDIR /portal
COPY application ./application
COPY requirements.txt ./
COPY run.py ./
RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py" ]