# VSCode Base Image
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11
ARG DEBIAN_FRONTEND=noninteractive

# Python and poetry installation
ARG USER=vscode
USER $USER
ARG HOME="/home/$USER"

# Add pyenv to PATH
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

# Install pyenv and poetry
ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.6.1
RUN echo "done 0" \
    && curl https://pyenv.run | bash \
    && echo "done 1" \
    && pyenv install ${PYTHON_VERSION} \
    && echo "done 2" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "done 3" \
    && curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION} \
    && poetry config virtualenvs.in-project false
