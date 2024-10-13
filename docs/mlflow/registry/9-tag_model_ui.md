# Tag a Model using the UI

When you register a model it automatically tagged with a version number (1, 2, 3,...). However you may want to add **special tags**, called **"Aliases"** to your model **like "testing", "production"**... This way you can easily know which model of your lineage is the one used in which environment.

## Step 1: Open the model details

Inside the "Models" tab click on the model name you want to tag.

![model_details](https://mlflow.org/docs/latest/_images/oss_registry_4_model.png)

## Step 2: Add an Alias to the model

Click on the pencil icon (✏️) to edit the model aliases.

![add_alias](https://mlflow.org/docs/latest/_images/oss_registry_4b_model_alias.png)

!!! question "Why is tagging a model useful?"

    By tagging your models you always have a same model name for a given environment despite its version (1, 2, 3...). This way you can have new versions of your model and always know which one is the one used in production, testing, etc.
