# Используем официальный базовый образ Python 3.12
FROM python:3.12-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# # Экспортируем переменные окружения
# ENV PYTHONUNBUFFERED=1


# Команда запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
