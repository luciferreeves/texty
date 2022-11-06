# Texty

[![Texty Build](https://github.com/luciferreeves/texty/actions/workflows/texty.yaml/badge.svg)](https://github.com/luciferreeves/texty/actions/workflows/texty.yaml)

Text Editor

## Requirements

Before you start using, building or contributing, there are a few things you need to have installed and configured on your machine:

- [Git](https://git-scm.com/downloads)
- [Python 3.6+](https://www.python.org/downloads/)

## Quick Start

To get started immediately, you can run the `setup.py` script. This is a Python script that is used to do a lot of things. It can be thought of as a manager script for this project. It is used to install requirements, run the project, and more. To run the script, type the following command in your terminal:

    python3 setup.py start

This will run the script and allow you to configure aliases for the project using the file `bin/configure`. Once the script runs successfully, you can run the project by running the following command in your terminal to configure aliases for the project:

    source bin/configure

> **Note**: You need to run the `source bin/configure` command every time you open a new terminal window.

After running the above command, you can run setup script by running the `setup` command and the commit script by running the `commit` command. For more infomation on the commit script, see [Committing Changes](#committing-changes) section below.

If you need further help, you can pair `-h` or `--help` option with any of the commands to get help for that command. For example, to get help for the `setup` command, run the following command:

    setup -h

Similarly, to get help for the `commit` command, run the following command:

    commit --help

A virtual environment is created automatically when you run the `setup.py` script. If you ran the script successfully, you should go ahead and activate the virtual environment:
    
    source .venv/bin/activate

At this point, you are ready to start contributing to the project by making changes to the code and submitting pull requests.

## Contributing Guidelines

The project is open to contributions. All kinds of suggestions are welcome. I want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug (Go to [File a Bug](https://github.com/luciferreeves/texty/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D) for reporting a bug)
- Discussing the current state of the code (See [Discussions](https://github.com/luciferreeves/texty/discussions) Page)
- Submitting a fix (See [Pull Requests](https://github.com/luciferreeves/texty/pulls) Page)
- Proposing new features (See [Request a Feature](https://github.com/luciferreeves/texty/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D) for requesting a feature)
- Becoming a maintainer (See [Maintainers](#maintainers))

GitHub is being exclusively used to host code, to track issues and feature requests, as well as accept pull requests for this project. Following is a guideline for developing via GitHub:

### Making Changes

> You can skip this step if you ran the `setup.py` script successfully.

You should start by [forking this repository](https://github.com/luciferreeves/texty/fork) and then cloning it to your local machine. If you need help with this, you can follow [this guide](https://help.github.com/articles/fork-a-repo/). Once you have cloned the repository, you can start making changes.

> **Note**: You must be working in a virtual environment. If you don't know what that is, you can read more about it [here](https://docs.python.org/3/tutorial/venv.html). To create a virtual environment, run the following command:

    python -m venv .venv

This will create a virtual environment named `env`. This environment will be used to install the project's dependencies and will be ignored by Git. To activate the environment, run the following command:

    source .venv/bin/activate

This will activate the virtual environment. You can now install the project's dependencies by running the following command:
    
    python3 setup.py install

To configure aliases at this point, run the following command:

    python3 setup.py configure
    source bin/configure

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
- The `files` argument is required. If you do not specify any files, the script will produce an error. You can add multiple files by separating them with a space. If you want to commit all files, use `"."` as the argument.
- The `-m` flag is required. If you do not specify a message, the script will prompt you for one.
- The `-t` and `-b` flags are optional. If you do not specify a branch, the script will use the current branch. If you do not specify a type, the script will use the default type `feat`.
- Valid change types are `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, and `revert`. If you specify an invalid type, the script will ask if you want to use the default type `feat`.
- If a non-existent branch is specified, the script will ask if you want to create the branch, and if you do, it will create the branch and push it to the remote repository; otherwise, it will abort.

Then you can run the  command:

```bash
commit README.md -m "Update README.md" -t "docs" -b "main"
```

Before running the command, make sure you have `git` installed and configured and that you have the correct permissions to push to the remote repository. 
If you haven't configured aliases or run `setup.py` at this point, you can achieve the same by making the script executable first:

```bash
chmod +x commit.sh
```

Commit the changes:

```bash
./commit.sh README.md -m "Update README.md" -t "docs" -b "main"
```

#### Configuring `commit.sh`

You can open and edit the `commit.sh` script directly to add your own commands. These commands will be executed before the commit is made. For example, you can add a command to run a linter before committing.

> **Note**: If any of the commands in the script fail, the script will exit and the commit will not be made.

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

This is a list of the current maintainers of this project. This list is automatically generated from the [maintainers.yml](maintainers.yml) file. The maintainers are listed in the order of their addition to the file. If you ever added or modified any parts of this repository, please add your name to the file and open a pull request.

The maintainers in the `maintainers.yml` file are listed in the following format:
    
    - name: <name of the maintainer>
      github: <github username of the maintainer>
      email: <email of the maintainer> (optional)
      website: <website of the maintainer> (optional)

> **Note**: Please do not edit the `README.md` file directly. Instead, edit the `maintainers.yml` file and run the `commit.sh` script to generate the `README.md` file.

<!-- maintainers -->- [Bobby](luciferreeves) - [https://thatcomputerscientist.com](https://thatcomputerscientist.com)![Bobby](https://github.com/luciferreeves.png?size=40) 