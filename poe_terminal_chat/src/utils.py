import os
from dotenv import load_dotenv
import sys

def poe_env_file_path():
    return os.path.join(os.path.expanduser('~'), '.poe.env')

def update_poe_env():
    poe_token = input("> poe_token: ")
    proxy = input("> proxy: ")
    with open(poe_env_file_path(), 'w') as f:
        f.write(f'POE_TOKEN="{poe_token}"\nPOE_PROXY="{proxy}"')


def check_token():
    poe_file_path = poe_env_file_path()
    if os.access(poe_file_path, os.F_OK):
        load_dotenv(poe_file_path)
        poe_token = os.getenv('POE_TOKEN')
        if not poe_token:
            update_poe_env()
            return check_token()
        else:
            return poe_token
    else:
        poe_file = open(poe_file_path, 'w')
        poe_file.close()
        update_poe_env()
        load_dotenv(poe_file_path)
        return os.getenv('POE_TOKEN')
