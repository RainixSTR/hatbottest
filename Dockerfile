FROM python:3.8
COPY /app /app
RUN pip install requests pyTelegramBotAPI beautifulsoup4
CMD python app/main.py