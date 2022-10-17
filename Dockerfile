FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/deals-api

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/deals-api/entrypoint.sh
RUN chmod +x /usr/src/deals-api/entrypoint.sh

COPY . .
EXPOSE 8000

ENTRYPOINT ["/usr/src/deals-api/entrypoint.sh"]