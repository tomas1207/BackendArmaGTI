FROM python:3
RUN mkdir /project
WORKDIR /project
COPY . /project/
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh" , "./entrypoint.sh" ]