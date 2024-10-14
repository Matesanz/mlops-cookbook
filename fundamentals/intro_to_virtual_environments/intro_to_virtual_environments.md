# Introduction to Virtual Envs

A virtual environment is an isolated environment in which you can **work on Python projects without interfering with the system-wide Python installation** or other projects. This is an **essential practice** for managing dependencies and ensuring project-specific package versions. This is especially useful if you are working on multiple projects at the same time, or if you want to test out new packages without affecting your system. Here's how to create a virtual environment in Python, Some of the most common tools to create virtualenvs are:

- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [pyenv](https://github.com/pyenv/pyenv)
- [conda](https://docs.conda.io/en/latest/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

!!! question "Why Virtual Environments?"

    Creating a virtual environment is a crucial step when working on Python projects to manage dependencies and keep your development environment clean and isolated. It allows you to work on multiple projects with different dependencies without conflicts.

## Using `venv` Module


!!! info "Venv module is a Python built-in module"

    Starting from Python 3.3, a built-in module called `venv` can be used to create virtual environments.
    This method is recommended for Python 3.3 and later.

**1. Open a Terminal or Command Prompt**.

**2. Create a Virtual Environment**:

Navigate to the directory where you want to create the virtual environment using `cd`:

```bash
cd /path/to/your/project
```

Create the virtual environment using the `venv` module. Replace `<venv_name>` with your desired environment name:

```bash
python -m venv <venv_name>
```

**3. Activate the Virtual Environment**:


!!! note "Command changes depending on the OS"

    👇 Select your operating system

    === "On Windows"

        ```console
        <venv_name>\Scripts\activate
        ```

    === "On macOS and Linux"

        ```shell
        source <venv_name>/bin/activate
        ```

!!! tip "How to Deactivate the Virtual Environment"
   
    Simply run:

    ```bash
    deactivate
    ```

## Using Pyenv

Virtualenvs are a great way to isolate your Python project dependencies. They allow you to create an isolated environment for your project, which means that you can install packages without affecting the rest of your system. 

!!! info "How to install pyenv?"

    Open a terminal (``Ctrl+Shift+` `` or `Terminal > New Terminal`) and use the following command:

    ``` bash
    curl https://pyenv.run | bash
    ```

**1. Install the desired Python version**

```bash
pyenv install <python-version>
```

**2. Create a Virtualenv using Pyenv**

```bash
pyenv virtualenv <python-version> <virtualenv-name>
```

**3. Activate the Pyenv Virtualenv**

```bash
pyenv activate <virtualenv-name>
```

!!! tip "Activate the virtualenv automatically"

    You can activate the pyenv virtualenv automatically **every time you enter into the project folder** by using this command:

    ```bash
    pyenv local <virtualenv-name>
    ```

    This will create a `.python-version` file in the project structure.

!!! tip "How to deactivate the virtualenv"
    
    You can deactivate the virtualenv using 
    
    ```bash
    pyenv deactivate
    ```

## Using Conda

Conda is a popular package and environment management system that allows you to create isolated environments for different Python projects. In this tutorial, we'll walk you through the steps to create virtual environments using Conda.

!!! info "How to install conda?"

    Before you begin, make sure you have Conda installed on your system. If you don't have Conda installed, you can **download and install** Miniconda or Anaconda, which includes Conda, **from the [official Conda website](https://conda.io/en/latest/miniconda.html).**

**1. Open a Terminal or Command Prompt**

**2. Create a New Conda Environment**

To create a new Conda environment, use the `conda create` command. You can specify the Python version and additional packages during the environment creation. Replace `<env_name>` with your desired environment name and `<python_version>` with the Python version you want.

```bash
conda create --name <env_name> python=<python_version>
```

!!! example "Venv named 'myenv' with python 3.11"

    To create an environment named "myenv" with Python 3.11, you would run:

    ```bash
    conda create --name myenv python=3.11
    ```

**3. Activate the Conda Environment**

Once the environment is created, activate it using the `conda activate` command. Replace `<env_name>` with the name of the environment you want to activate.

```bash
conda activate <env_name>
```

!!! example "Activate the 'myenv' environment"

    ```bash
    conda activate myenv
    ```

You will notice that the prompt changes to indicate that your Conda environment is active.

!!! tip "How to deactivate the Conda Environment"

    To deactivate the Conda environment and return to the base environment, simply run:

    ```bash
    conda deactivate
    ```

!!! tip "List Conda Environments"

    To view a list of all the Conda environments on your system, use the following command:

    ```bash
    conda env list
    ```

!!! tip "Remove a Conda Environment"

    To remove a Conda environment, you can use the `conda env remove` command. Replace `<env_name>` with the name of the environment you want to remove.

    ```bash
    conda env remove --name <env_name>
    ```

    !!! example "remove the "myenv" environment"

        ```bash
        conda env remove --name myenv
        ```
