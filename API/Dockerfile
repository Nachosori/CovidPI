FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ADD ./ /miapi

WORKDIR /miapi

RUN pip install -r requirements.txt

ENV PORT=8090

CMD uvicorn main:app --host 0.0.0.0 --port=${PORT}