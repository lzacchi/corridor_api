FROM python:3.10

RUN mkdir /app

COPY /app /app

COPY pyproject.toml /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry install --no-dev
RUN export FLASK_APP=app/app.py

ENTRYPOINT [ "poetry" ]
CMD [ "run", "python", "app.py" ]
