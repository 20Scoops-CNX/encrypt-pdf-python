FROM python:3.7.3-alpine3.8

ARG PORT=9000
ENV PORT $PORT

COPY /src/requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]

CMD ["src/app.py"]