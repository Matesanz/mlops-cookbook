# What is MLFlow?

Remember that **you are a scientist** (of data), and as a good scientist, you should keep a record of all your experiments. Well, **imagine MLflow as a book where you can write down all your progress**.

![mlflow_workflow](https://mlflow.org/docs/latest/_images/mlflow-overview.png)

For example, imagine you are trying to develop a model that predicts the price of a house based on a series of parameters like the year of construction or the square footage. As a data scientist, your job is to research and experiment with different approaches to build an accurate model. This is very much like a writer working on their book.

![mlflow_frontend](../assets/mlflow_frontend.jpg)

This is the frontend of MLFlow. It is a web application that allows you to keep track of your experiments. You can see the different experiments you have run, the parameters you have used, the metrics you have measured, and the artifacts you have generated.

## How to install MLFlow?

It's really simple! 😃 You can install MLFlow using `pip` like any other python library (remember to do so inside a virtual environment)

!!! info "Install MLFlow"

    ```bash
    pip install mlflow
    ```

## How to launch MLFlow?

Once you have installed MLFlow, you can launch it with the following command:

!!! info "Launch MLFlow"

    This will launch a server in your local machine. You can access it by **going to [http://localhost:5000](http://localhost:5000) in your web browser**.

    ```bash
    mlflow server
    ```

    You will see the following output:

    ```bash
    [2024-02-21 23:29:52 +0100] [725738] [INFO] Starting gunicorn 21.2.0
    [2024-02-21 23:29:52 +0100] [725738] [INFO] Listening at: http://127.0.0.1:5000 (725738)
    [2024-02-21 23:29:52 +0100] [725738] [INFO] Using worker: sync
    [2024-02-21 23:29:52 +0100] [725739] [INFO] Booting worker with pid: 725739
    [2024-02-21 23:29:52 +0100] [725740] [INFO] Booting worker with pid: 725740
    [2024-02-21 23:29:53 +0100] [725741] [INFO] Booting worker with pid: 725741
    ```
