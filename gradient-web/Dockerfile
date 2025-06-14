FROM python:3.9-slim 
# Used a base image with Python 3.9

WORKDIR /app 
# Set the working directory in the container
# Copy the requirements file and install dependencies

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 
#Copying the source code into the container

EXPOSE 8080
 # Expose port 8080 for the application

CMD ["python", "app.py"]
