# Python'ning yengil versiyasini tanlaymiz
FROM python:3.10-slim

# Keraksiz .pyc fayllar yaratilishining oldini olish va loglarni to'g'ridan-to'g'ri ko'rsatish
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ishchi papkani belgilash
WORKDIR /app

# PostgreSQL va boshqa kutubxonalar uchun kerakli tizim paketlarini o'rnatish
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Talablarni o'rnatish (Gunicorn ham qo'shilgan deb faraz qilamiz)
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Barcha kodlarni nusxalash
COPY . /app/

CMD ["gunicorn", "book.wsgi:application", "--bind", "0.0.0.0:8000"]