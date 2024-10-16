FROM python:3.11
ENV LANG C.UTF-8

# Install dependencies
RUN apt-get update -y
RUN apt-get -y update && apt-get -y autoremove
RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "bot.py"]