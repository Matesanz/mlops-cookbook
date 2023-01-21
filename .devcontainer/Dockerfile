# VSCode Base Image
ARG PYTHON_VERSION="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${PYTHON_VERSION}

# Install Poetry
# Install Poetry
ARG POETRY="1.2.2"
RUN pip install poetry==${POETRY}

# Install python dependencies using poetry
COPY pyproject.toml /
RUN cd / && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root
