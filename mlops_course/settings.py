"""Settings for the MLOps course project."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base Settings used to configure the project."""

    MLFLOW_URI: str = "http://mlflow:5000"


config = Settings()
