# Dependency Management with Poetry

[Poetry](https://python-poetry.org/) is an essential tool for Python developers as it **revolutionizes dependency management**, packaging, and project development. It simplifies the process of managing project dependencies by providing a declarative and intuitive approach. With Poetry: 

- Developers can easily **define and track their project's dependencies**, ensuring consistent and reproducible development environments across different machines. Additionally.
- Poetry simplifies packaging by automating the **creation of distributable packages**, making it easier to share and distribute projects with others.
- It also facilitates the **creation of virtual environments**, isolating project dependencies and avoiding conflicts. But, please better use specific virtual environment tools to create virtual-environments (pyenv, venv module, conda...)

Poetry's comprehensive features, combined with its user-friendly interface, streamline the development workflow and enhance the overall efficiency and maintainability of Python projects.

!!! question "Why Poetry if we have plain `requirements.txt`"

    While `requirements.txt` is a simple declaration of needed dependencies with Poetry you can pretty much trust that whatever combination it finds will work. It also allows you to install the local project as a python module using pip (but this is a more advanced topic).

!!! info "More About Poetry"
    You can find more info about Poetry in the [official documentation](https://python-poetry.org/).

## 1. Installing Poetry

Once we have our **development environment up and running**, we can start creating our project. We will use **Poetry** to manage our project's dependencies and packaging. Poetry provides a simple and intuitive interface for managing dependencies, packaging, and virtual environments. It also offers a comprehensive set of features, such as dependency resolution, dependency isolation, and dependency locking. Poetry's user-friendly interface and powerful features make it an indispensable tool for Python developers.

!!! info "How to install poetry?"

    Open a terminal and use onw of the following.

    === "Using pip"

        ``` bash
        pip install poetry==<version> # (1)
        ```

        1.  ℹ️ Remember to use a specific version (like `1.4.2`, `1.5.0` or `1.6.1`) by replacing `<version>` with the desired version.
    
    === "Using the official installer"

        ```bash
        curl -sSL https://install.python-poetry.org | python3 - --version <version> # (1)
        ```

        1.  ℹ️ Remember to use a specific version (like `1.4.2`, `1.5.0` or `1.6.1`) by replacing `<version>` with the desired version.

!!! warning "Avoid creating a virtualenv using Poetry"

    As we have seen before, by default Poetry creates a virtual environment for each project, but this is normally handled by other tools like `pyenv` or `conda`. So, if you are using Poetry. In order to **avoid Poetry creating a virtual environment**, you can use the `virtualenvs.create` config:

    ``` bash
    poetry config virtualenvs.create false
    ```

## 2. Creating a new project

To create a new project, we can use the `new` command:

``` bash
poetry new <project_name>
```

!!! info "The default poetry project structure"

    The `poetry new <project_name>` command will create a new project with the following structure:

    ``` bash
    <project_name>
    ├── pyproject.toml
    ├── README.md
    ├── <project_name>
    │   └── __init__.py
    └── tests
        └── __init__.py
    ```

!!! info "The default `pyproject.toml` file"

    The `pyproject.toml` file contains the project's metadata and dependencies and it will look like this:

    ``` toml
    [tool.poetry]
    name = "<project_name>"
    version = "0.1.0"
    description = ""
    authors = ["<author_name> <author_email>"]
    readme = "README.md"
    packages = [{include = "<project_name>"}]

    [tool.poetry.dependencies]
    python = "^<python_version>" # (1)

    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"
    ```

    1.  The `^` symbol in poetry indicates version is pinned to the major version. Remember: versions are given as `MAJOR`.`MINOR`.`PATCH`. So, if we had, for example `^3.11` as the python version, it means that this project is compatible with any 3.x python version (being `x` equal or greater than 11) but never 4.x versions.


### 3.2. Adding dependencies

To add a dependency, we can use the `add` command:

``` bash
poetry add <dependency>
```

!!! example "How to add a main dependency: `requests`"

    This will add the dependency to the `pyproject.toml` file and install it in the virtual environment. For example, to add the `requests` library, we can use the following command:

    ``` bash
    poetry add requests
    ```

    This will add the following lines to the `pyproject.toml` file:

    ``` toml
    [tool.poetry.dependencies]
    python = "^3.9"
    requests = "^2.25.1"
    ```

!!! info "Adding dependencies just for development"

    If we want to add a dependency just for development, we can use the `--group dev` flag. This will add the dependency to the `pyproject.toml` file under the `[tool.poetry.group.dev.dependencies]` section.

    ``` bash
    poetry add <dependency> --group dev
    ```

    !!! example ""How to add a development dependency: `pytest`"

        For example, to add the `pytest` library, we can use the following command:

        ``` bash
        poetry add pytest --group dev
        ```

        This will add the following lines to the `pyproject.toml` file:

        ``` toml
        [tool.poetry.dependencies]
        python = "^3.11"

        [tool.poetry.group.dev.dependencies]
        pytest = "^6.2.2"
        ```

### 3.3. Removing dependencies

To remove a dependency, we can use the `remove` command:

``` bash
poetry remove <dependency>
```
