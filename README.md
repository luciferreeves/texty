# Texty
Text Editor


## Contributing Guidelines

The project is open to contributions. All kinds of suggestions are welcome. I want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug (Go to [File a Bug](https://github.com/luciferreeves/texty/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D) for reporting a bug)
- Discussing the current state of the code (See [Discussions](https://github.com/luciferreeves/texty/discussions) Page)
- Submitting a fix (See [Pull Requests](https://github.com/luciferreeves/texty/pulls) Page)
- Proposing new features (See [Request a Feature](https://github.com/luciferreeves/texty/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D) for requesting a feature)
- Becoming a maintainer (See [Maintainers](

GitHub is being exclusively used to host code, to track issues and feature requests, as well as accept pull requests for this project. Following is a guideline for developing via GitHub:

### Requirements

Before you start contributing, there are a few things you need to have installed and configured on your machine:

- [Git](https://git-scm.com/downloads)
- [Python 3.6+](https://www.python.org/downloads/)

### Making Changes

You should start by [forking this repository](https://github.com/luciferreeves/texty/fork) and then cloning it to your local machine. If you need help with this, you can follow [this guide](https://help.github.com/articles/fork-a-repo/). Once you have cloned the repository, you can start making changes.

**Note**: You must be working in a virtual environment. If you don't know what that is, you can read more about it [here](https://docs.python.org/3/tutorial/venv.html). To create a virtual environment, run the following command:

    python -m venv env

This will create a virtual environment named `env`. This environment will be used to install the project's dependencies and will be ignored by Git. To activate the environment, run the following command:

    source env/bin/activate

This will activate the virtual environment. You can now install the project's dependencies by running the following command:
    
    pip install -r requirements.txt

This will install all the dependencies required to run the project. You can now start making changes.

### Committing Changes

This repository uses a custom commit script `commit.sh` to commit changes. This script will automatically add all files in the repository, commit them, and push them to the remote repository. You should use this script instead of using the any of the git commands directly.

> **Note**: This script immediately pushes the changes to the remote repository. If you don't want to push the changes yet, you can use regular git commands, but you should still use the script to commit the final changes.

    Usage: ./commit.sh files -m message -t type -b branch

    files           files to be committed
    -m              message: commit message
    -t              type: change type (optional)
    -b              branch: branch name (optional)
    -h, --help      display help message

**Note**: The `files` argument is required. If you do not specify any files, the script will produce an error. You can add multiple files by separating them with a space. If you want to commit all files, use `"."` as the argument.

**Note**: The `-m` flag is required. If you do not specify a message, the script will prompt you for one.

**Note**: The `-t` and `-b` flags are optional. If you do not specify a branch, the script will use the current branch. If you do not specify a type, the script will use the default type `feat`.

**Note**: Valid change types are `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, and `revert`. If you specify an invalid type, the script will ask if you want to use the default type `feat`.

**Note**: If a non-existent branch is specified, the script will ask if you want to create the branch, and if you do, it will create the branch and push it to the remote repository; otherwise, it will abort.

Before running the script, make sure you have `git` installed and configured and that you have the correct permissions to push to the remote repository. Then you can start by making the script executable first:

```bash
chmod +x commit.sh
```

Then you can run the script:

```bash
./commit.sh README.md -m "Update README.md" -t "docs" -b "main"
```

#### Configuring `commit.sh`

You can open and edit the `commit.sh` script directly to add your own commands. These commands will be executed before the commit is made. For example, you can add a command to run a linter before committing.

**Note**: If any of the commands in the script fail, the script will exit and the commit will not be made.

In order to configure the script, you should add your commands inside the `commands()` function. The `commands()` function is called before the commit is made. You can add your commands inside the function.

    # User Defined Commands

    commands() {
        # Add your commands here
        
        # Example:
        # echo "Hello World"
    }

### Submitting Changes

Once you have made your changes, you can submit them by [creating a pull request](https://github.com/luciferreeves/texty/pulls). If you need help with this, you can follow [this guide](https://help.github.com/articles/creating-a-pull-request/) to learn how to create a pull request. Once you have created a pull request, it will be reviewed and merged if it is approved.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Maintainers

<!-- maintainers -->- [Bobby](luciferreeves) - [https://thatcomputerscientist.com](https://thatcomputerscientist.com)![Bobby](https://github.com/luciferreeves.png?size=40) 