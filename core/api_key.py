import os
from pathlib import Path

API_KEY_LENGTH = 32
HOME = str(Path.home())
CREDS_FOLDER = f"{HOME}/.seamless"
CREDS_FILE = f"{CREDS_FOLDER}/credentials"


class CredentialsException(Exception):
    pass


def get_api_key():
    if not os.path.exists(CREDS_FILE):
        raise CredentialsException("Cannot find credentials")
    with open(CREDS_FILE, 'r') as creds:
        api_key = creds.read()
    if not is_api_key_valid(api_key):
        raise CredentialsException("Credentials file does not contain a valid API KEY")
    return api_key


def set_api_key(api_key):
    Path(CREDS_FOLDER).mkdir(parents=True, exist_ok=True)
    with open(CREDS_FILE, 'w+') as f:
        f.write(api_key)


def is_api_key_valid(api_key):
    if len(api_key) != API_KEY_LENGTH:
        return False
    elif not api_key.isalnum():
        return False
    else:
        return True
