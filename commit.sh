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

# Get arguments passed to this script
files=$1
message=$2
type=$3
branch=$4

# Check if the branch name is specified
if [ "$branch" != "" ]; then
    # Check if the branch name is valid
    if [ $(git branch | grep -c "$branch") -eq 0 ]; then
        echo "Branch $branch does not exist"
        exit 1
    fi
fi

# Check if the change type is specified
if [ "$type" != "" ]; then
    # Check if the change type is valid
    if [ $(echo $type | grep -c "feat\|fix\|docs\|style\|refactor\|perf\|test\|chore\|revert") -eq 0 ]; then
        echo "Invalid change type $type"
        exit 1
    fi
fi

# Check if the commit message is specified, if not, prompt the user
if [ "$message" = "" ]; then
    echo "Enter commit message (required):"
    read message
fi


# Check if files are specified, if not, prompt the user
if [ "$files" = "" ]; then
    echo "Enter files to be committed (space separated) or '.' for all files (required):"
    read files
fi


# Generate requirements.txt file, delete it if it already exists
if [ -f requirements.txt ]; then
    rm requirements.txt
fi
pip3 freeze > requirements.txt


# Add files to be committed
git add $files
git add requirements.txt

# Modify the message in the following format: <type>: <message>
if [ "$type" != "" ]; then
    message="$type: $message"
fi

# Commit the changes
git commit -m "$message"

# Push the changes to the remote branch
if [ "$branch" != "" ]; then
    git push origin $branch
else
    git push origin $branch
fi

