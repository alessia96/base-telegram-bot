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


history = dict()


def process_message(text: str, username: str) -> str:

    if username not in history:
        messages = [{"role": "user", "content": text}]
        history[username] = messages
    else:
        history[username] += [{"role": "user", "content": text}]
        messages = history[username]

    response = get_openai_response(messages=messages)

    if response != DEFAULT_RESPONSE:
        history[username].append({"role": "assistant", "content": response})

    if len(history[username]) > MAX_HISTORY:
        history[username] = history[username][-MAX_HISTORY:]

    return response


def get_openai_response(messages: list) -> str:
    client = openai.OpenAI(api_key=OPENAI_APIKEY)

    try:
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful friend."
                }
            ] + messages
        )
    except (Exception,) as e:
        logger.error(e)
        return DEFAULT_RESPONSE
    if len(completion.choices) == 0:
        return DEFAULT_RESPONSE

    output = completion.choices[0].message
    return output