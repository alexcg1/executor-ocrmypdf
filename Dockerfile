FROM jinaai/jina:latest

RUN apt-get update &&\
    apt-get install -y tesseract-ocr tesseract-ocr-eng

# install requirements before copying the workspace
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# setup the workspace
COPY . /workspace
WORKDIR /workspace

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
