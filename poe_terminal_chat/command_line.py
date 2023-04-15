# entry point for terminal poe chat
import argparse
import sys
from argparse import ArgumentParser
from .poeterminal import Poe
from .utils import update_poe_env


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
    argparser.add_argument('input', type=str, help="question string", nargs="*")
    args = argparser.parse_args()
    if args.change:
        update_poe_env()
        print("Update Poe terminal chat successfully!")
    # as terminal entry
    if len(sys.argv) < 2:
        print("请至少问一个你想问的问题~")
    else:
        msg = ''.join(args.input)
        poe = Poe()
        poe.send_message(msg)
