FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /api

COPY requirements.txt /api

WORKDIR /api

RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /api

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]