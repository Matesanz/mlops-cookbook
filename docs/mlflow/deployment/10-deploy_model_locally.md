# Deploy Model Locally

We've already explained that deploying a model can be seen as setting up a restaurant (API) where you have a chef (your trained model) who can cook dishes (make predictions) for customers (incoming data). Now the question is ***"Where do you set up your restaurant (aka model)?"***. The quick answer is that **you will always deploy a model in a "computer" (server)**. It can be your computer (local deployment), a "cloud computer" (cloud server) or another "computer" inside your company (on-premise server).

In a professional environment you will normally deploy your model on the cloud or on-premise servers. However, for testing purposes, you can deploy your model locally on your computer. This is what we will do in this tutorial.

## Deploy a model using MLFLow

Mlflow provides a [simple way to **generate an API**](https://mlflow.org/docs/latest/cli.html#mlflow-models-serve) (the restaurant) using [Flask](https://flask.palletsprojects.com/en/3.0.x/) with a simple command:

!!! note "Command to deploy a model from MLFlow"
    ```shell
    mlflow models serve --model-uri models:/<model_name>/<model_stage>
    ```

!!! warning "Flask must be installed"

    Mlflow uses [Flask](https://github.com/pallets/flask) (a well known python library) to generate the API, so you need to have Flask installed. You can install Flask using **Pip** or **Poetry**:

    === "Using Pip"
        ```shell
        pip install flask
        ```

    === "Using Poetry"
        ```shell
        poetry add flask
        ```

## Model Deployment Configuration

You can change the default configurations of the API by using the [following options](https://mlflow.org/docs/latest/cli.html#cmdoption-mlflow-models-serve-m):

| Option             | Description                                                                                                                          | Default      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|
| -m, --model-uri    | Required URI to the model. A local path, a 'runs:/' URI, or a remote storage URI (e.g., an 's3://' URI). For more information about supported remote URIs for model artifacts, see [here](https://mlflow.org/docs/latest/tracking.html#artifact-stores). | -            |
| -p, --port         | The port to listen on.                                                                                             | 5000         |
| -h, --host         | The network address to listen on. Use 0.0.0.0 to bind to all addresses if you want to access the tracking server from other machines. | 127.0.0.1    |
| -t, --timeout      | Timeout in seconds to serve a request.                                                                               | 60           |
| -w, --workers      | Number of gunicorn worker processes to handle requests.                                                              | 1            |
| --env-manager      | If specified, create an environment for MLmodel using the specified environment manager. The following values are supported: - local: use the local environment - virtualenv: use virtualenv (and pyenv for Python version management) - conda: use conda If unspecified, default to virtualenv. | virtualenv   |
| --no-conda         | If specified, use local environment.                                                                                                | -            |
| --install-mlflow  | If specified and there is a conda or virtualenv environment to be activated, mlflow will be installed into the environment after it has been activated. The version of installed mlflow will be the same as the one used to invoke this command. | -            |
| --enable-mlserver | Enable serving with MLServer through the v2 inference protocol. You can use environment variables to configure MLServer. (See [here](https://mlserver.readthedocs.io/en/latest/reference/settings.html)) | -            |

**Let's see some examples 😎:**

!!! Example "Changing the port of the API"

    By default the **port** is set to the **5000**, we can change it to the **8888** by:

    ```shell
    mlflow models serve --model-uri models:/<model_name>/<model_stage> --port 8888
    ```

!!! Example "Change the timeout for serving requests"

    By default the **timeout** is set to **60 seconds**, we can change it to **10 seconds** by:

    ```shell
    mlflow models serve --model-uri models:/<model_name>/<model_stage> --timeout 10
    ```
