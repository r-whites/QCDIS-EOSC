FROM python:3.6.1-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV FLASK_APP "app.py"
CMD ["flask", "run"]