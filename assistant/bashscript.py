import os
import openai 

from . import const
from . import utils


def returnBashForGivenAction(text):
    prompt = "Give me precise bash script to do following action " + text + "  only return bash script"
    openai.organization = const.GPT3_ORG_ID
    openai.api_key = utils.get_gpt3_secret()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You should only return bash script"}, 
          {"role": "user", "content": prompt}]
    )
    return response.choices[0]["message"]["content"].strip()

if __name__ == "__main__":
    print("install xyz " + returnBashForGivenAction("install xyz"))
    print("Move all JPEG images to photos folder " + returnBashForGivenAction("Move all JPEG images to photos folder"))
    print("Organize my systems" + returnBashForGivenAction("Organize my desktop"))
