FROM python:3.11-alpine

RUN pip install pipenv
RUN mkdir -p /usr/src/app/app
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock main.py ./
#COPY app ./app
COPY fake_database .

#RUN pipenv install --system

CMD ls -la fake_database

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]