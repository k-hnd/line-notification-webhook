FROM python:3.6
ENV PORT 8080
WORKDIR /webhook
COPY . /webhook
RUN apt-get update -y && \
    apt-get install locales -y && \
    echo "ja_JP UTF-8" > /etc/locale.gen && \
    locale-gen && \
    pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", ":${PORT}", "--workers", "1", "--threads", "8", "app:webhook"]
