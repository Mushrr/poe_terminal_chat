import os
from dotenv import load_dotenv
import sys
import poe

def poe_env_file_path():
    return os.path.join(os.path.expanduser('~'), '.poe.env')

def update_poe_env():
    poe_token = input("> poe_token: ")
    proxy = input("> proxy: ")
    with open(poe_env_file_path(), 'w') as f:
        f.write(f'POE_TOKEN="{poe_token}"\nPOE_PROXY="{proxy}"')


def check_config(config_name: str = "POE_TOKEN"):
    poe_file_path = poe_env_file_path()
    if os.access(poe_file_path, os.F_OK):
        load_dotenv(poe_file_path)
        poe_token = os.getenv(config_name)
        if not poe_token:
            update_poe_env()
            return check_config(config_name)
        else:
            return poe_token
    else:
        poe_file = open(poe_file_path, 'w')
        poe_file.close()
        update_poe_env()
        load_dotenv(poe_file_path)
        return os.getenv(config_name)


def get_bot_names():
    client = poe.Client(check_config('POE_TOKEN'), check_config('POE_PROXY'))
    bot_objects = []
    for name, val in client.get_bots(download_next_data=False).items():
        bot_obj = {}
        _bot_obj = val["defaultBotObject"]
        bot_obj["name"] = name
        bot_obj["nick"] = _bot_obj["displayName"]
        bot_obj["description"] = _bot_obj["description"] 
        bot_objects.append(bot_obj)
    return bot_objects

def create_bot(client: poe.Client):
    def input_element(msg: str) -> str:
        return input(f"> {msg}:")
    name = input_element("name")
    nick = input_element("nick")
    description = input_element("description")
    base_model = input_element("base model (chinchilla, a2)")
    intro_message = input_element("intro message")
    prompt = input_element("prompt")
    try:
        client.create_bot(
                name,
                description=description,
                base_model=base_model,
                prompt=prompt,
                intro_message=intro_message
                )
        print("Create Bot successfully!")
    except:
        print("Create Bot failed!")
        exit(0)
