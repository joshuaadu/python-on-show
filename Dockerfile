FROM python:3.11-alpine AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN pip install pipenv
COPY Pipfile* ./
RUN PIP_USER=1 pipenv install --system --deploy --ignore-pipfile

FROM python:3.11-alpine

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
COPY --chown=myapp:user --from=base ${PYROOT}/ ${PYROOT}/

RUN mkdir -p /usr/src/app /usr/src/fake_database
WORKDIR /usr/src

COPY --chown=myapp:user app ./app
COPY --chown=myapp:user fake_database ./fake_database
USER user

CMD ls -la app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]