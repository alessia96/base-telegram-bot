import os

from dotenv import load_dotenv
import logging
import openai


logger = logging.getLogger()
logger.setLevel('INFO')

load_dotenv()
DEFAULT_RESPONSE = os.environ.get('DEFAULT_RESPONSE', 'No response. Please try again later.')
MAX_HISTORY = os.environ.get('MAX_HISTORY', 15)
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')


