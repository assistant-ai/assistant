from google.oauth2.credentials import Credentials
from google.cloud import secretmanager_v1

import base64
import os

GPT3_SECRET_FILE_NAME="openai.secret"
GPT3_SECRET_ID="projects/951968178545/secrets/gpt3-secret/versions/1"

gpt3_secret=None

def get_secret(secret_file_name: str, secret_id: str) -> str:    
    if os.path.exists(secret_file_name):
        with open(secret_file_name, "r") as f:
            secret = f.readlines()[0]
            return secret
    
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager_v1.AccessSecretVersionRequest(
        name=secret_id,
    )

    # Make the request
    response = client.access_secret_version(request=request)
    secret = response.payload.data.decode("UTF-8")
    # Save the decoded secret data to a file:
    with open(secret_file_name, "w") as f:
        f.write(secret)
    return secret

def get_gpt3_secret():
    global gpt3_secret
    if gpt3_secret:
        return gpt3_secret
    gpt3_secret = get_secret(GPT3_SECRET_FILE_NAME, GPT3_SECRET_ID)
    return gpt3_secret


if __name__ == "__main__":
    save_config_json()
