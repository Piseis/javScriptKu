from dotenv import load_dotenv
import os

load_dotenv()

def env( key ):
    return os.environ.get( key );