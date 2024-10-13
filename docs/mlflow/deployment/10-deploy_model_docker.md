# Deploy a Model using Docker

Another way to deploy a model is using [**Docker**](https://www.docker.com/). Docker is a platform for developing, shipping, and running applications using containerization. It allows you to package your application and its dependencies into a container that can run on any environment.

!!! tip "Deploy a MLFlow model with Docker"

    You can deploy a MLFlow model with Docker using the following command:

    ```bash
    docker run \
        --net host \
        --env MLFLOW_TRACKING_URI=http://localhost:5000 \
        ghcr.io/mlflow/mlflow:v2.17.0 \
        mlflow models serve \
        --model-uri models:/<model_name>/<model_version> \
        --port 5001 \
        --env-manager local
    ```

    ![docker_06](../../assets/docker/docker_06.jpg)
