"""Define the input and output data schema for the model.

Imagine we have a special code that helps us organize information
in a very neat and structured way. This code is like a set of rules
that tells us how to describe different kinds of information.

In this code, we have two sets of rules. The first set of rules is
for describing the information we give to a computer program.
It tells us that the information should have three parts: "sex"
(which can only be either "female" or "male"), "age" (which
can be any number), and "fare" (which can also be any number).

The second set of rules is for describing the information that the
computer program gives us back. It says that the program will give
us one thing called "prediction," and that thing will be a number.

So, these rules help us make sure that the information we give to
the program and the information we get back from the program are
organized and easy to understand. It's like having a special
language that we use to communicate with the program.
"""

from typing import Literal

from pydantic import BaseModel


# Define the input data schema using Pydantic BaseModel
class InputData(BaseModel):
    """Data model for the input data to the model."""

    sex: Literal["female", "male"]
    age: float
    fare: float


# Define the output data schema using Pydantic BaseModel
class OutputData(BaseModel):
    """Data model for the output data from the model."""

    prediction: float
