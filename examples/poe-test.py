import os
from dotenv import load_dotenv
import poe;
from os import path



if __name__=="__main__":
    load_dotenv(path.join(os.path.expanduser('~'), '.poe.env'))
    key = os.getenv('POE_TOKEN')
    proxy = os.getenv('POE_PROXY')
    print(key)
    
