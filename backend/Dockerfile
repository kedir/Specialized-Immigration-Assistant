FROM python:3.10.12

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
    python3-dev \
    apt-utils \
    python-dev \
    build-essential \   
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -U pip


COPY app/requirements.txt /app
RUN pip install --no-cache-dir -U -r  ./app/requirements.txt

COPY app/ /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]