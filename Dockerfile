# Use the official Python image as base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project to the working directory
COPY . .

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["python","snipbox_project/manage.py","runserver","0.0.0.0:8000"]
