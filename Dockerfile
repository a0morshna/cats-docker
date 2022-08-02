# our base image
FROM python:3.7

COPY . /templates

WORKDIR /templates

RUN pip install Flask

# tell the port number the container should expose
EXPOSE 5000

ENTRYPOINT ["python"]

# run the application
CMD ["app.py"]
