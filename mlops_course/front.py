"""Simple Streamlit App.

This code is a simple Streamlit app that allows users to input their
personal information and get a prediction of their chances of surviving
the Titanic disaster. Here are the key components and their explanations:

- The app begins with a welcome message and a brief description of
    how it works.
- In the sidebar, there is an input form where users can select their
    sex, age, and fare.
- After filling in the input form, users can click the "Predict"
    button to make a prediction.
- When the button is clicked, the app creates an instance of the
    InputData class with the user input.
- It then sends a POST request to the API endpoint /predict with
    the input data as JSON.
- The response from the API is parsed into an instance of the
    OutputData class.
- Finally, the app displays the prediction results based on the
    received data.
- The app uses Streamlit to create a user-friendly interface and
    the requests library to communicate with the API.
"""
import requests
import streamlit as st

from mlops_course.schema import InputData, OutputData
from mlops_course.settings import config

API_URL = config.BACKEND_URI

st.title("🚢 Would I have survived?")
st.markdown(
    """
    Welcome to the **Titanic Survival Prediction App**! :wave:

    ### 🪧 Description

    Have you ever wondered whether you would have survived the Titanic
    disaster? With this app, you can input your personal information
    and find out your chances of survival. :thinking:

    ### 📜 How to use?

    Simply:

    - 👈 **Insert your passenger information here.**
    - 🖱️ **Click the button to make a prediction.**

    ### 🤔 How does it work?

    Using machine learning algorithms, this app predicts your likelihood of
    surviving based on factors such as your age, gender, ticket class,
    and whether you were traveling alone or with family members. :computer:
    """
)

# create an input form for the features
with st.sidebar:
    st.title("🙋 Passenger Features")
    # Define the user input form
    sex = st.selectbox("Sex", ["female", "male"])
    age = st.slider("Age", min_value=0, max_value=100, value=30)
    fare = st.slider("Fare", min_value=0, max_value=550, value=100)
    st.title("🔮 Predict")

# create a button to make the prediction
if st.sidebar.button("Predict", use_container_width=True):
    input_data = InputData(
        sex=sex,
        age=age,
        fare=fare,
    )

    # make a request to the API
    backend_endpoint = f"{API_URL}/predict"
    response = requests.post(
        url=backend_endpoint,
        json=input_data.dict(),
        timeout=5,
    )
    prediction_data = OutputData.parse_obj(response.json())

    # display the prediction results
    st.title("🔮 Prediction")
    if prediction_data.prediction < 0.5:
        st.error("🧟 You probably wouldn't have survived.")
    else:
        st.success("🎉 You probably would have survived.")
