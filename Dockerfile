FROM python:3.9

WORKDIR /app

RUN pip install poetry fastapi "uvicorn[standard]"

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-dev

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
