# This is a Python script that is used to do a lot of things. It can be thought
# of as a manager script for this project. It is used to install requirements,
# run sorter, linter, start and build the project and more. It will be a
# constantly evolving script as the project evolves.

import logging as logger
import os
import subprocess
import sys

logger.basicConfig(stream=sys.stdout, level=logger.DEBUG)


def install_pip(package_name):
    # check if package is installed
    check_command = "pip3 show " + package_name
    try:
        output = subprocess.check_output(check_command, shell=True)
    except:
        logger.info(f"Installing {package_name}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "-q", "install", package_name]
        )


PACKAGES = ["black", "isort", "click", "inquirer", "pyyaml"]


def install_packages():
    install_pip(" ".join(PACKAGES))


import click
import inquirer


class Setup:
    def shell_run(self, command):
        output = subprocess.check_output(command, shell=True)
        return output.decode("utf-8")

    def start(self):
        if not os.path.exists(".venv"):
            self.shell_run("python3 -m venv .venv")
            logger.info("Virtual environment created.")
        self.git()

    def git(self):
        username = self.shell_run("git config --global user.name")
        if username == "":
            questions = [
                inquirer.Confirm(
                    "set_username",
                    message="Do you want to set git author name?",
                    default=True,
                ),
            ]
            answers = inquirer.prompt(questions)
            if answers["set_username"]:
                username = inquirer.text(
                    message="Enter git author name (not username): "
                )
                self.shell_run(f'git config --global user.name "{username}"')
            else:
                logger.warn("Git author name not set.")

        email = self.shell_run("git config --global user.email")
        if email == "":
            questions = [
                inquirer.Confirm(
                    "set_email",
                    message="Do you want to set git author email?",
                    default=True,
                ),
            ]
            answers = inquirer.prompt(questions)
            if answers["set_email"]:
                email = inquirer.text(message="Enter git author email: ")
                self.shell_run(f'git config --global user.email "{email}"')
            else:
                logger.warn("Git author email not set.")

        self.configure()

    def configure(self):
        configure_path = "bin/configure"
        script = """#!{}
alias commit="./commit.sh"
alias setup="python3 setup.py"
echo "Added aliases for commit and setup."
echo ""
echo "Run 'setup' to start the setup again. Run 'setup -h' for more options."
echo "Run 'commit' to commit changes. Run 'commit -h' for help."
""".format(
            os.environ["SHELL"]
        )
        with open(configure_path, "w") as f:
            f.write(script)

        configure_st = os.stat(configure_path)
        os.chmod(configure_path, configure_st.st_mode | 0o111)
        print(
            """Configuration script created.

You may want to configure aliases for commit and setup scripts.
To do so, run the configurator binary:

    source bin/configure

You may also want to activate the virtual environment, if you haven't already:

    source .venv/bin/activate
"""
        )


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@click.command(help="Start the setup.")
def start():
    Setup().start()


cli.add_command(start)


@click.command(help="Install requirements.")
def install():
    logger.info("Installing requirements...")
    install_packages()
    logger.info("Requirements installed.")


cli.add_command(install)


@click.command(help="Generate alias configuration script.")
def configure():
    Setup().configure()


cli.add_command(configure)


if __name__ == "__main__":
    cli()
