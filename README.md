# Texty
Text Editor

## Committing Changes

This repository uses a custom commit script `commit.sh` to commit changes. This script will automatically add all files in the repository, commit them, and push them to the remote repository.

    Usage: ./commit.sh files -m message -t type -b branch

    files           files to be committed
    -m              message: commit message
    -t              type: change type (optional)
    -b              branch: branch name (optional)
    -h, --help      display help message

**Note**: The `files` argument is required. If you do not specify any files, the script will produce an error. If you want to commit all files, use `"."` as the argument.

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

### Configuring `commit.sh`

You can open and edit the `commit.sh` script directly to add your own commands. These commands will be executed before the commit is made. For example, you can add a command to run a linter before committing.

**Note**: If any of the commands in the script fail, the script will exit and the commit will not be made.

In order to configure the script, you should add your commands inside the `commands()` function. The `commands()` function is called before the commit is made. You can add your commands inside the function.

    # User Defined Commands

    commands() {
        # Add your commands here
        
        # Example:
        # echo "Hello World"
    }
