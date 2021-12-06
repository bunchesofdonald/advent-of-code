FROM python:3.10
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /src/
WORKDIR /src/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY . .
