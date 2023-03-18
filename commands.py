import os
import openai 



def returnBashForGivenAction(text):
    prompt = "Give me precise bash script to do following action " + text
    openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
    openai.api_key =  os.getenv("OPENAI_API_KEY")
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
