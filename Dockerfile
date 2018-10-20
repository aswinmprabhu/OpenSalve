# Use the official python image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY temp_random_key

# Make port 8080 available to the world outside this container
EXPOSE 8080

# create root directory for our project in the container
RUN mkdir /music_service

# Set the working directory to /music_service
WORKDIR /api

# Copy the current directory contents into the container at /music_service
ADD . /api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Apply migrations
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

# Run Server
CMD ["python", "manage.py", "runserver", "8080"]
