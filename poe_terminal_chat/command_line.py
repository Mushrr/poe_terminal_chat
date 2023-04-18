# entry point for terminal poe chat
import argparse
import sys
from argparse import ArgumentParser
from .poeterminal import Poe
from .utils import create_bot, get_bot_names, update_poe_env


def main():
    poe_terminal_usage = '''
        use like this
        poechat your question
        if you want change config
        poechat --change'''
    argparser = ArgumentParser(description=poe_terminal_usage) 
    argparser.add_argument(
            '-c', 
            '--change', 
            help='change poe terminal chat config file',
            action='store_true'
            )
    argparser.add_argument(
            '-b',
            '--botnames',
            help="show current bot names",
            action="store_true"
            )
    argparser.add_argument(
            '--bot',
            help="select a bot to communicate with",
            )
    argparser.add_argument(
            '-a',
            '--addbot',
            help='create a new bot',
            action='store_true'
            )
    argparser.add_argument('input', type=str, help="question string", nargs="*")
    args = argparser.parse_args()
    if args.change:
        update_poe_env()
        print("Update Poe terminal chat successfully!")
    # as terminal entry
    if args.botnames:
        bot_objs = get_bot_names()
        print('\n'.join([f'Name: {bot["name"]}, Description: {bot["description"]}' for bot in bot_objs]))
        exit(0)
    if args.bot:
        poe_bot = Poe(bot=args.bot)
        poe_bot.continus_chat()
        exit(0)
    if args.addbot:
        poe_bot = Poe()
        create_bot(poe_bot.poe_client)
        exit(0)
    if len(sys.argv) < 2:
        print("请至少问一个你想问的问题~")
        exit(0)
    else:
        msg = ''.join(args.input)
        poe = Poe()
        poe.single_chat(msg)
