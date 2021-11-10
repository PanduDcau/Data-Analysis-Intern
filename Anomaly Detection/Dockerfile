FROM python:3.8
#ENV CONTAINER_HOME=/var/www
#
#ADD . $CONTAINER_HOME
#WORKDIR $CONTAINER_HOME
#
#RUN pip install -r $CONTAINER_HOME/requirements.txt
#
#EXPOSE 5000
#
#ENTRYPOINT["python"]
#CMD["app.py"]

COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install  -r requirements.txt
CMD python app.py