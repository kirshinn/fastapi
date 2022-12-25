FROM python:3.9
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir -r /src/requirements.txt
COPY . /src/
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]