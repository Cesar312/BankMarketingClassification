FROM python:3.7.0
LABEL Banking Marketing Classification Model Cesar Martinez, Northwestern University
COPY ./SVC-model /usr/local/python/SVC-model/
COPY ./api/ /usr/local/python/api/
EXPOSE 5000
WORKDIR /usr/local/python/api/
RUN pip install -r requirements.txt
CMD python flaskAPI.py