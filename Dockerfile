FROM  python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $Port
CMD gunicorn --worked=4 --bind 0.0.0.0:$Port app:app
