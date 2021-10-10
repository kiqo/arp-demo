FROM python:3.7

WORKDIR /project

COPY ./arpdemo /project/arpdemo
COPY setup.cfg .
COPY setup.py .
COPY pyproject.toml .

RUN pip install --no-cache-dir .

CMD ["uvicorn", "arpdemo.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "arpdemo.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
