# Model Deployment

Model deployment is the process of **making your model available for use by other people or systems**. When you serve a model, it's like putting it to work so that it can make predictions or classifications on new, incoming data.

!!! quote "What does "deploying a model" mean?"

    Model deployment is the process of **making your model available for use by other people or systems**. When you serve a model, it's like putting it to work so that it can make predictions or classifications on new, incoming data.

## Model Deployment Workflow

Let's break it down using a **simple analogy**.

Deploying a model (also called "serving a model") is a bit like setting up a **restaurant** (API) where you have a **chef** (your trained model) who can cook **dishes** (make predictions) for **customers** (users) based on their **orders** (incoming data).

!!! tip "Comparing Serving a Model with a Chef in a Restaurant"

    👇 Click to compare

    === "Regular Model Serving"

        ![model_deployment_mlflow](../../assets/model_deployment_01.jpg)

    === "Model Deployment as if it were a restaurant"

        ![model_deployment_restaurant](../../assets/model_deployment_02.jpg)

Here's how it works:

1. **Training the Chef (Model)**: First, you train your chef by creating and fine-tuning your machine learning model using data. It's like teaching the chef how to cook your special recipes.

2. **Opening the Restaurant (Deployment)**: Once your chef is ready, you need a restaurant (a server or service) to serve the dishes (predictions). In MLflow, you can use the Model Registry to manage different versions of your chef's recipes (models) and choose which one to serve.

3. **Taking Orders (Incoming Data)**: People come to your restaurant and place orders (send data). For example, they might ask, "Is this email spam?" Your restaurant receives these orders (data) and sends them to your chef (model) to make predictions.

4. **Chef Makes Predictions (Model Serving)**: The chef (model) follows the recipe (model instructions) and prepares the dish (provides predictions) based on the order (incoming data).

5. **Serving the Dish (Sending Predictions)**: The chef serves the cooked dish (predictions) to the customers (applications or users) who requested it.

MLflow helps you manage and keep track of the chef's recipes (model versions) and ensures that everything runs smoothly in your "restaurant" by managing model deployments, making it easier to serve your machine learning models to applications and users in real time.