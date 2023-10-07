# Description: This script is run after the devcontainer is built.
# It installs the packages defined in pyproject.toml and the local package.
# It also installs pre-commit hooks and starts mkdocs.

GREEN='\033[92m'
BLUE='\033[94m'
END='\033[0m'

# configure git
echo -e "${BLUE}🚀  Launching Devcontainer Post-Install Script${END}\n"
echo -e "${BLUE}🔧  Configuring Git...${END}\n"
git_config_file=".git_user_config"
if [ ! -f "$git_config_file" ]; then
    echo -e "${BLUE}ℹ️  It looks like this is the first time you run this script, please provide the following GIT information:${END}\n"
    read -p "Git user name: " git_name
    read -p "Git user email: " git_email
    echo ${git_name} > ${git_config_file}
    echo ${git_email} >> ${git_config_file}
fi
git_name=$(head -n 1 "$git_config_file")
git_email=$(sed -n '2p' "$git_config_file")
git config --global user.name "${git_name}"
git config --global user.email "${git_email}"
git config --global --add safe.directory $(pwd)
echo -e "${GREEN}✅  Git Configured!${END}\n"

# initialize pyenv
echo -e "${BLUE}🔧  Initializing Pyenv...${END}\n"
eval "$(pyenv init -)"
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# avoid creating virtualenvs in poetry
echo -e "${BLUE}🔧  Configuring Poetry...${END}\n"
poetry config virtualenvs.create false
echo 'poetry config virtualenvs.create false' >> ~/.bashrc

# install packages defined in pyproject.toml and the local package
echo -e "${BLUE}🔧  Installing python dependencies using Poetry..${END}\n"
if [ ! -f "poetry.lock" ]; then
    echo -e "${BLUE}ℹ️  No poetry.lock file found, resolving dependencies, this may take a while, please wait..${END}\n"
fi
poetry install --no-interaction --no-ansi --no-root
pip3 install -e . --no-deps 
echo -e "${GREEN}✅  Python dependencies installed!${END}\n"

# install pre-commit hooks and start mkdocs
echo -e "${GREEN}✅  Project correctly configured!${END}\n"
echo -e "${BLUE}🔧  Installing pre-commit hooks and starting mkdocs..${END}\n"
pre-commit install
