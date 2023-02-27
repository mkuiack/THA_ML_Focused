FROM python:3.9.6

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./src .
COPY ./data /usr/data

EXPOSE 8000

CMD [ "python3", "app.py"]
