"""
Author:     David Walshe
Date:       30 July 2022
"""

from pathlib import Path
from argparse import ArgumentParser, Namespace

import yaml

BASE_DIR = Path(__file__).parent
ROLES_DIR = BASE_DIR / "roles"


def parse_args() -> Namespace:
    """Parse command line arguments."""
    parser = ArgumentParser()
    parser.add_argument("--role-name", type=str, required=True, help="The name of the role to create.")
    parser.add_argument("--vars", action="store_true", help="Create a 'vars' folder.")
    parser.add_argument("--template", action="store_true", help="Create a 'templates' folder.")
    return parser.parse_args()


def cli():
    """CLI entry point."""
    args = parse_args()

    role_path = ROLES_DIR / args.role_name
    if role_path.exists():
        raise FileExistsError(f"Role '{args.role_name}' already exists.")

    role_path.mkdir()
    print(f"Role '{args.role_name}' created.")

    folders = {
        "tasks": True,
        "vars": args.vars,
        "templates": args.template,
    }
    for folder, make in folders.items():
        if make:
            folder_path = role_path / folder
            folder_path.mkdir()
            print(f"'{folder}' folder created.")
            main_yml_file = folder_path / "main.yml"
            main_yml_file.touch()
            print(f"'{main_yml_file}' created.")


if __name__ == "__main__":
    cli()
