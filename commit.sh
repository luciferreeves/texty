# This script is used to process certain files or run certain commands
# before a commit is made.  You should use this script instead of
# using the any of the git commands directly.

# This script is called with the following arguments:
# $1 - files to be committed (space separated) or '.' if all files
# $2 - commit message preceded by a '-m' 
# $3 - change type (optional) - valid values are 'feat', 'fix', 
#       'docs', 'style', 'refactor', 'perf', 'test', 'chore' or 
#       'revert'. If not specified, 'feat' is assumed. Must be
#       specified preceded by a '-t' flag.
# $4 - branch name (optional) - if not specified, the current branch
#       is assumed. Must be specified preceded by a '-b' flag.

# This script should return 0 if the commit should proceed or 1 if
# the commit should be aborted.

# Get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD)


# Help function

helpFuntion() {
    echo "Usage: $0 files -m message -t type -b branch"
    echo files "\t files to be committed (space separated) or '.' if all files"
    echo -m "\t message: commit message"
    echo -t "\t type: change type (optional) - valid values are 'feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'chore' or 'revert'. If not specified, 'feat' is assumed."
    echo -b "\t branch: branch name (optional) - if not specified, the current branch is assumed."
    echo -h, --help "\t display this help message"
    exit $1
}


# User Defined Commands
commands() {
    # Add commands here
    # Example:
    # echo "Hello World"

    # Generate Requirements.txt, delete the old one if it exists
    if [ -f requirements.txt ]
    then
        rm requirements.txt
    fi
    pip3 freeze > requirements.txt
}

# Default values for optional arguments
type="feat"
branch=$(git rev-parse --abbrev-ref HEAD)

# Commit function
commit() {
    # Run User Defined Commands
    commands
    # Check if the branch is the current branch
    if [ "$branch" == "$(git rev-parse --abbrev-ref HEAD)" ]
    then
        # If the branch is the current branch, commit the files
        git commit $1 -m "$2"
        echo $1
        echo $2
        # git push origin $branch
    else
        # If the branch is not the current branch, checkout the branch and commit the files
        git checkout $3
        git commit $1 -m "$2"
        git push origin $3
    fi
}

# Check if the number of arguments is less than 2
if [ $# -le 1 ] 
then
    # Check if the first argument is -h or --help
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]
    then
        helpFuntion 0
    else
        echo "Error: Not enough arguments"
        helpFuntion 1
    fi
fi

# Check if number of arguments is greater than 7
if [ $# -gt 7 ]
then
    echo "Error: Too many arguments"
    helpFuntion 1
fi

# Parse the arguments
while [ "$1" != "" ]; do
    case $1 in
        -m | --message )    shift
                            message=$1
                            ;;
        -t | --type )       shift
                            type=$1
                            ;;
        -b | --branch )     shift
                            branch=$1
                            ;;
        -h | --help )       helpFuntion 0
                            ;;
        * )                 files="$files $1"
    esac
    shift
done

# Check if the message is empty
if [ -z "$message" ]
then
    # If the message is empty, prompt the user for a message
    read -p "Enter commit message: " message
fi

# Add type to the message
message="$type: $message"

# Check if the branch exists
if [ -z "$(git branch --list $branch)" ]
then
    # If the branch does not exist, prompt if the user wants to create it
    read -p "Branch $branch does not exist. Do you want to create it? (y/n): " createBranch
    if [[ $createBranch =~ ^[Yy]$ ]] || [[ $createBranch =~ ^[Yy][Ee][Ss]$ ]]
    then
        git checkout -b $branch
    else
        echo "Commit aborted"
        exit 1
    fi
fi

# Check if type is valid
if [[ $type =~ ^(feat|fix|docs|style|refactor|perf|test|chore|revert)$ ]]
then
    # If type is valid, run commit function
    commit $files $message $branch
else
    # If type is invalid, prompt the to use the default type
    read -p "Invalid type. Do you want to use the default type "feat"? (y/n): " useDefaultType
    if [[ $useDefaultType =~ ^[Yy]$ ]] || [[ $useDefaultType =~ ^[Yy][Ee][Ss]$ ]]
    then
        commit $files $message $branch
    else
        echo "Commit aborted"
        exit 1
    fi
fi

