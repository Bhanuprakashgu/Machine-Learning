#Use python as base image
FROM python:3.19-slim

#Use workinf directory /app
WORKDIR /app

#Copy all the cotent of current directort to /app
COPY . /app

#Installing required packages
RUN pip install --no-cache-dir -r requirements.txt

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME World

#Run python program
CMD ["python","app.py"]