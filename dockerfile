FROM python:3.7

RUN pip install  fastapi uvicorn

WORKDIR /app

COPY ./interview/app/ .
COPY ./interview/run.py .

EXPOSE 80

CMD ["python","run.py"]



