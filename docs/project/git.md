# Version Control using GIT

GIT is a powerful version control system that helps you track changes in your code and collaborate with others. This tutorial is aimed at beginners and will cover the basics of GIT.

!!! note "How to install GIT"

    Before you can use GIT, you need to install it on your computer. Visit the official [GIT website](https://git-scm.com/) and download the installer for your operating system. Follow the installation instructions for your platform.

!!! note "Configuring GIT"

    After installing GIT, you need to configure your name and email address. Open a terminal or command prompt and run the following commands, replacing "Your Name" and "your.email@example.com" with your actual name and email:

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email your.email@example.com
    ```

## The Basic GIT Workflow

Develop a new feature aside from the project:

1. **Create** a branch
2. **Making changes**
3. **Staging** changes
4. **Commit** changes
5. **Push** changes from local repository to remote repository

Integrate the new feature into the project.

6. Create a **Pull Request** (Github) or **Merge Request** (Gitlab) remotely
7. **Merge Changes** remotely
8. **Remove Branch** remotely
9.  Pull Changes from remote repository to local repository
10. Remove Branch locally

![GIT Schema](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*iL2J8k4ygQlg3xriKGimbQ.png)

## Creating a GIT Repository

A GIT repository is a place where you can store your project's code. Navigate to the directory where your project is located in the terminal and run the following command to initialize a new GIT repository:

!!! note "Start A Repository"
    ```bash
    git init
    ```

## Adding Files to the Repository

Before you can track changes, you need to add your project's files to the repository. You can add individual files or all files in the directory using the following commands:

!!! note "Start tracking a file in our repository"

    === "Add a single file"

        ```bash
        git add <filename>
        ```

    === "Add all files"

        ```bash
        git add .
        ```

## Making Commits

A commit is a snapshot of the changes you've made. To commit your changes, use the following command:

!!! note "Commit changes"
    ```bash
    git commit -m "Your commit message"
    ```

    Make sure to replace "Your commit message" with a brief description of what you've changed.

## Working with Branches

Branches allow you to work on different features or parts of your project independently. 

![git branch schema](https://wac-cdn.atlassian.com/dam/jcr:a905ddfd-973a-452a-a4ae-f1dd65430027/01%20Git%20branch.svg?cdnVersion=1288)

!!! note "Create a new branch"
    ```bash
    git branch <new-branch-name>
    ```

!!! note "Switch to a branch"

    ```bash
    git checkout <new-branch-name>
    ```

!!! note "Create and Switch to a new branch in one command"

    ```bash
    git checkout -b <new-branch-name>
    ```

## Merging Branches

When you're done with a branch, you can merge it into the main branch (usually "master" or "main").

!!! note "How to merge a feature branch into the main branch"

    1. Switch to the main branch

        ```bash
        git checkout main
        ```

    2. Merge the other branch into the main branch

        ```bash
        git merge new-branch-name
        ```

## Sharing Your Code

You can share your GIT repository with others using platforms like [GitHub](https://github.com/) or [GitLab](https://gitlab.com/). Create an account on one of these platforms and follow their instructions for creating a new repository and pushing your code.

**Step 10: Fetching, Pulling and Pushing Changes**

!!! note "How to fetch changes"

    Fetching checks if there is any change available in the remote repository

    ```bash
    git fetch
    ```

!!! note "From a remote repository -> Local repository"

    ```bash
    git pull
    ```

!!! note "From local repository -> remote repository"

    ```bash
    git push
    ```

That's it! You now have a basic understanding of GIT. Remember that GIT is a powerful tool with many features and commands, so this tutorial is just the beginning. As you become more comfortable with GIT, you can explore advanced topics such as resolving conflicts, branching strategies, and more.
