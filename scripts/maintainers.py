# This file is used to generate the list of maintainers from the maintainers.yml
# file. It is used to make sure that all the maintainers are listed in the
# README.md file.

import yaml


def main():
    # Load the maintainers.yml file
    with open("maintainers.yml", "r") as f:
        maintainers = yaml.safe_load(f)

    # Load the README.md file
    with open("README.md", "r") as f:
        readme = f.read()

    # Generate the list of maintainers
    maintainers_list = ""
    maintainer_images = ""
    for maintainer in maintainers:
        if not maintainer["name"] or not maintainer["github"]:
            # Skip maintainers without a name or github username
            continue

        # Generate the markdown for the maintainer
        maintainers_list += "- [{}]({})".format(
            maintainer["name"], maintainer["github"]
        )
        if maintainer["email"]:
            maintainers_list += "<{}>".format(maintainer["email"])

        if maintainer["website"]:
            maintainers_list += " - [{}]({})".format(
                maintainer["website"], maintainer["website"]
            )

        # Move to next line
        maintainers_list += "\r"

        # Generate the markdown for the maintainer's image
        image_url = "https://github.com/{}.png?size=40".format(maintainer["github"])
        maintainer_images += "![{}]({}) ".format(maintainer["name"], image_url)

    # Remove everything below "<!-- maintainers -->" in the README.md file
    readme = readme.split("<!-- maintainers -->")[0]

    # Add the list of maintainers to the README.md file
    readme += "<!-- maintainers -->\r" + maintainers_list + "\r" + maintainer_images

    # Save the README.md file
    with open("README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
