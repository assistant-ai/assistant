import os
import openai 



def isAction(text):
    prompt = "Determine if following text requires an action, only return True or False " + text
    openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
    openai.api_key =  os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": " Determine if following text requires an action  You should only retrun True or False"},
          {"role": "user", "content": prompt}]
    )
    return response.choices[0]["message"]["content"].strip()

if __name__ == "__main__":
    print("install xyz " + isAction("install xyz"))
    print("Move all JPEG images to photos folder " + isAction("Move all JPEG images to photos folder"))
    print("Organize my desktop " + isAction("Organize my desktop"))
    print("How are you R2D2 " + isAction("How are you R2D2")) 
