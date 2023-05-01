"""Settings for the MLOps course project."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base Settings used to configure the project."""

    MLFLOW_TRACKING_URI: str = "http://mlflow:5000"
    MLFLOW_EXPERIMENT_NAME: str = "mlops-course"
    DATA_PATH: str = "data/"


config = Settings()
