FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3-venv
WORKDIR /app
COPY . /app
RUN python3 -m venv library_creator
RUN . library_creator/bin/activate && \
  pip install -r requirements.txt
CMD ["python3", "index2.py"]
