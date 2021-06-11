FROM python:3.9.1

RUN mkdir /project
WORKDIR /project
COPY . /project/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "/bin/bash" , "./entrypoint.sh" ]