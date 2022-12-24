FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY . /app/
CMD ["uvicorn", "server:app", " --host=0.0.0.0", " --reload"]