# Register a Model using the UI

The simplest way to register a model is by **using the MLflow Web Interface**. This is useful when you want to manually register a model. The instrucions shown here are were taken from the [official documentation](https://mlflow.org/docs/latest/model-registry.html#ui-workflow).

## Step 1: Open the model details

By clicking on the model name in the desired run in the **Experiments** page, you can see the model details.

![model_details](https://mlflow.org/docs/latest/_images/oss_registry_1_register.png)

## Setp 2: Register the model

You can click on the **Register Model** blue button to register the model.

![register_model](https://mlflow.org/docs/latest/_images/oss_registry_2_dialog.png)

!!! info "Create a new model"

    If you want to create a new lineage of a model, you can click on the **"Create New Version"** button. When a new model is registered a **new version is created**. The first version of a model is always version 1.
