FROM python

# Устанавливаем перемменную окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочюю дерикторию
WORKDIR /code

# Копируем файл requirements в контейнер
COPY requirements.txt /code/

# Установка зависимости
RUN pip install -r requirements.txt

# Копируем код проекта
COPY . /code/
