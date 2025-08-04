# Python 3.13 기반 이미지
FROM python:3.13-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 작업 디렉토리
WORKDIR /app

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 복사
COPY . /app/

# static 파일 모으기
RUN python manage.py collectstatic --noinput

# 컨테이너 실행 시 명령
CMD ["gunicorn", "simson.wsgi:application", "--bind", "0.0.0.0:8000"]