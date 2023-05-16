"""Defines the FastAPI app and the API endpoint for making predictions.

Imagine we have a special computer program called an API.
This program can do something really cool: it can predict things
for us based on some information we give it. Let's say we want to
use this program to predict if someone would have survived the Titanic
shipwreck.

To make this prediction, we need to give the program some information
about a person, like their age, sex, and fare they paid for their ticket.
This information helps the program understand different things that might
affect someone's chance of survival.

The program has a model inside it that has learned from a lot of data about
the Titanic shipwreck. This model is like a brain that can make predictions
based on what it has learned. It knows what things are important in determining
whether someone would have survived or not.

When we send our information to the program, it processes the information
and uses its model to make a prediction. The model thinks really hard and
gives us an answer: either "yes" or "no" to tell us if the person would
have survived.

So, this program works like a magic crystal ball that tells us what would have
happened to someone if they were on the Titanic. We just need to input their
information, and it gives us an answer. It's like asking a really smart
friend for their opinion!
"""
import mlflow
import numpy as np
from fastapi import FastAPI

from mlops_course.schema import InputData, OutputData
from mlops_course.settings import config

MLFLOW_URI = config.MLFLOW_TRACKING_URI
MODEL_NAME = config.MODEL_NAME
MODEL_URI = f"models:/{MODEL_NAME}/Production"

# connect to the MLflow tracking server and load the model
mlflow.set_tracking_uri(uri=MLFLOW_URI)
model = mlflow.pyfunc.load_model(model_uri=MODEL_URI)

# Define the FastAPI app
app = FastAPI()


# Define the API endpoint
@app.post("/predict")
def predict(input_data: InputData):
    """Make a prediction using the MLflow model."""
    # convert sex from "male" to 1 and "female" to 0
    sex = 0
    if input_data.sex == "male":
        sex = 1

    # Process the input data
    features = np.array(
        [
            sex,
            input_data.age,
            input_data.fare,
        ]
    ).reshape(1, -1)

    # Use the MLflow model to perform inference
    prediction = model.predict(features)

    # Return the inference results
    return OutputData(prediction=prediction[0])
