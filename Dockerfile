FROM python:3.12-slim

# set the working directory in the container
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglib2.0-0 \
    git

COPY requirements.txt .

# install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the whole applications
COPY . .

# expose the port the app runs on
EXPOSE 8000

# command to run the application
CMD ["uvicorn", "segment_image_endpoint:app", "--host", "0.0.0.0", "--port", "8000"]
