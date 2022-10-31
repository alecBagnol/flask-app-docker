#  base image alpine
FROM alpine:3.14

# install python3 and pip3 for alpine
RUN apk add --no-cache python3 py3-pip

# upgrade pip3
RUN pip3 install --upgrade pip

# install python packages needed for the app from requirements.txt
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# copy the app to the container
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Expose port 5000
EXPOSE 5000

# run the app
CMD ["python3", "/usr/src/app/app.py"]