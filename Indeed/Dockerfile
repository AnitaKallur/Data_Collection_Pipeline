
# specify image:tag
FROM python:latest

# Run a bash command
RUN mkdir/mydirectory

# Set the current working directory
WORKDIR /mydirectory

# Copy data from docker context
COPY main.py .

# When we run container this is the command we run
ENTRYPOINT ["python3, main.py"]
