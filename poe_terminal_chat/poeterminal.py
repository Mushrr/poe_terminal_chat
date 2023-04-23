# main source file

import os
from .utils import update_poe_env, check_config
import poe

class Poe:
    def __init__(self, bot: str = "capybara"):
        self.poe_token = check_config()
        self.poe_proxy = os.getenv('POE_PROXY')
        self.poe_client = poe.Client(self.poe_token, proxy=self.poe_proxy)
        self.message_queue = []
        self.bot_name = bot;
    def single_chat(self, msg: str, with_chat_break=True):
        for chunk in self.poe_client.send_message(self.bot_name, msg, with_chat_break=with_chat_break):
            print(chunk['text_new'], end="", flush=True)

    def continus_chat(self):
        while True:
            question = ""
            print('🍄> ', end='')
            while True:
                tmp = input("")
                tmp = tmp.strip()
                if tmp == '':
                    break
                question += tmp
            if question == "":
                break
            print("\n😊> ", end='')
            try:
                self.single_chat(question, with_chat_break=False)
            except:
                print("好像网络出了点问题，重新发一下吧~🙌", end='', flush=True)
            print("\n")
        print(f"Hope this journey with {self.bot_name} can help you!")
        return
