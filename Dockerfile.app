# Set the base image.
FROM python:3.10-slim

# Expose necessary ports.
# Uvicorn [REST-API]
EXPOSE 4200
EXPOSE 8001

# Set the working directory.
WORKDIR /app

# Copy necessary files from the host.
COPY ./src ./src
COPY ./requirements.txt ./requirements.txt
COPY ./data ./data
COPY ./notebooks ./notebooks
COPY ./bin/run_services.sh ./bin/run_services.sh

# Install application dependencies.
RUN pip install -r requirements.txt

# Make the bash script executable.
RUN chmod +x ./bin/run_services.sh

# Set up entrypoint to make the container executable.
ENTRYPOINT ["./bin/run_services.sh"]
