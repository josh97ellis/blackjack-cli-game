FROM python:3.11.2

ADD src/blackjack.py .

RUN pip install PyYAML==6.0

CMD ["python", "./blackjack.py"]