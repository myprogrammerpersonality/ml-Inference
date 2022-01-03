FROM python:3.9-slim-bullseye

COPY ./requirements.txt ./requirements.txt
COPY ./serve.py ./serve.py
COPY ./model.joblib ./model.joblib

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080  
CMD ["python3", "serve.py"]
