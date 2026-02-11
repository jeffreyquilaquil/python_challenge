FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libgirepository1.0-dev \
    gcc \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    gir1.2-gstreamer-1.0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install playsound==1.2.2

COPY . .

CMD ["python","app.py"]