FROM python:3.10-slim

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Copy the requirements file first (better caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy project
COPY ./core /app/

# Expose port
EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]