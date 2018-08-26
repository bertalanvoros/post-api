FROM python:2-jessie

RUN pip install requests
RUN pip install flask
RUN pip install flask-restful

EXPOSE 8080

CMD [ "python", "/opt/app/api.py"]
