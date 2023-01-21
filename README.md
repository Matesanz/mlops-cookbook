# 👋 mlops-course

## 🪧 Description

Code for the MLOps Course: learning how to build, train, and deploy data models.

## 🗃️ Table of Contents

- [👋 mlops-course](#-mlops-course)
  - [🪧 Description](#-description)
  - [🗃️ Table of Contents](#️-table-of-contents)
  - [🚀 Basic Usage](#-basic-usage)
    - [📚 Documentation](#-documentation)
  - [📦 Installation](#-installation)
    - [🐍 Using Pip](#-using-pip)
    - [🌹 Using Poetry](#-using-poetry)
  - [🏗️ Development](#️-development)
    - [🐋 Devcontainer Environment](#-devcontainer-environment)
    - [🧑‍⚖️ Pre-Commit](#️-pre-commit)
    - [🌹 Poetry](#-poetry)
      - [📦 Installing Poetry](#-installing-poetry)
      - [ℹ️ Poetry Basic Usage](#ℹ️-poetry-basic-usage)
  - [🙋 Author](#-author)

## 🚀 Basic Usage

```python
import mlops_course
```

### 📚 Documentation

To launch documentation:

```bash
mkdocs serve
```

👉 Then go to http://localhost:8000

## 📦 Installation

### 🐍 Using Pip

```console
pip install .
```

### 🌹 Using Poetry

```console
poetry config virtualenvs.create false
poetry install
```

💡 To install poetry see: [installing poetry section](#-installing-poetry)

## 🏗️ Development

### 🐋 Devcontainer Environment

It is possible to have a **development environment** up an ready **[using Docker and vscode](https://code.visualstudio.com/docs/remote/containers)**:

![devcontainer_gif](https://microsoft.github.io/vscode-remote-release/images/remote-containers-readme.gif)

1. Install [remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in **VSCode**.
   1. Press `Ctrl+P`
   2. Paste `ext install ms-vscode-remote.remote-containers`
   3. Press `Enter`

2. Run the **docker** in development in **VSCode** *(wait, first time takes some time to run)* :

   ```console
   F1 > Open Folder in Container
   Select the desired folder (backend, frontend...)
   ```

It automatically searches for de `.devcontainer/devcontainer.json` file in the root folder.
To apply changes made to the [dockerfile](docker/Dockerfile) or the [devcontainer.json](.devcontainer/devcontainer.json):

   ```console
   F1 > Rebuild Container
   ```

👍 It will **install** automatically **`mlops_course`** in development mode and all the [pre-commit hooks](.pre-commit-config.yaml) along all the tools needed for a correct development: black, isort, pylint, mypy, pytest...

### 🧑‍⚖️ Pre-Commit

In order to **keep code and commits quality** we enforce the use of pre-commit by doing:

```console
pre-commit install
```

This will install a bunch of hooks that will check staged files (only the `*.py` staged files) to check that they stick to black, autopep8, isort and some other standards.

### 🌹 Poetry

#### 📦 Installing Poetry

This project uses Poetry as dependency manager. It needs to be installed in our computer to be used.
To install Poetry in Linux, macOS or Windows we need to execute the next line:

Option 1:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Option 2:

```bash
pip install poetry
```

To check if Poetry is working fine execute:

```bash
poetry --version
Poetry (version 1.2.0)
```

#### ℹ️ Poetry Basic Usage

To add a new dependency:

```bash
poetry add <package-name>
```

If you only want your dependency to be installed in development mode:

```bash
poetry add --dev <package-name>
```

Install added dependencies:

```bash
poetry install
```

## 🙋 Author

🙋 **Name**: Andrés Matesanz

📩 **Email**: Matesanz.Cuadrado@gmail.com
