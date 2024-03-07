# Introduction to Docker - Part 2: Building Your Own Image

Welcome to the enhanced second part of our Docker introduction! In this section, we'll guide you through the process of building your own Docker image step by step using a simple example with a Python application. We'll use FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Step 1: Create a FastAPI Application

Create a file named `main.py` within the directory:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Docker! This is a FastAPI application."}
```

## Step 2: Create a Dockerfile

1. First create a file named: `Dockerfile`

    ```bash
    touch Dockerfile
    ```

2. **Define the Base Image**: Start by specifying the base image for your Dockerfile. We'll use an official Python image, specifically version 3.9-slim, to keep it lightweight. Inside the Dockerfile, add the following line:

    ```Dockerfile
    # Use an official Python image as the base image
    FROM python:3.9-slim
    ```

3. **Install FastAPI and Uvicorn**: Install the necessary Python packages for your FastAPI application. In this case, we need FastAPI itself and Uvicorn, which is the ASGI server FastAPI uses. Add the following line to the Dockerfile:

    ```Dockerfile
    # Install FastAPI and Uvicorn
    RUN pip install fastapi uvicorn
    ```

4. **Copy Application Code**: Copy the entire content of your local directory (where the Dockerfile is located) into the container's working directory. Add the following line to the Dockerfile:

    ```Dockerfile
    # Copy the application code to the container
    COPY main.py .
    ```

5. **Define the Command to Run the Application**: Specify the command to run your FastAPI application using Uvicorn. The `--host 0.0.0.0` makes it accessible from outside the container. The `--port 8000` makes the API available on port 8000. Add the following line to the Dockerfile:

    ```Dockerfile
    # Command to run the application using Uvicorn
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

6. **Save and Close the Dockerfile**: Save your changes and close the text editor.

## Step 3: Build the Docker Image

Open a terminal in the directory containing your Dockerfile and application code. Run the following command to build the Docker image:

```bash
docker build -t my-fastapi-app .
```

## Step 4: Run the Docker Container

Once the image is built, you can run a container based on it with the following command:

```bash
docker run -p 8000:8000 my-fastapi-app
```

!!! info "Remember run parameters"
    - `-p 8000:8000`: Maps port 8000 on the host to port 8000 on the container.
    - `my-fastapi-app`: The name of the Docker image to run.

Visit [http://localhost:8000](http://localhost:8000) in your web browser to interact with your FastAPI application.

Congratulations! You've successfully built a Docker image for a FastAPI application and run it in a container. Feel free to explore more features of FastAPI and Docker as you continue your learning journey.
