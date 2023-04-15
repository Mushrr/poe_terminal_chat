# main source file

import os
from .utils import update_poe_env, check_token
import poe

class Poe:
    def __init__(self):
        self.poe_token = check_token()
        self.poe_proxy = os.getenv('POE_PROXY')
        self.poe_client = poe.Client(self.poe_token, proxy=self.poe_proxy)
    def send_message(self, msg: str, module:str = "capybara"):
        for chunk in self.poe_client.send_message(module, msg, with_chat_break=True):
            print(chunk['text_new'], end="", flush=True)
