from dotenv import load_dotenv
import os
import requests


load_dotenv()
BITLY       = os.getenv("BITLY")
BITLY_GROUP = os.getenv("BITLY_GROUP")

def bitly_shorten(url):
    if BITLY == None or BITLY_GROUP == None:
        return url
        
    data = {
      "group_guid": BITLY_GROUP,
      "domain": "bit.ly",
      "long_url": url
    }

    headers = {"Authorization": f"Bearer {BITLY}"}

    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=data, headers=headers)
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()['link']

    print(f'bitly_shorten: {response.status_code} || {response.text}')
    
    return 0


if __name__ == "__main__":
    print(bitly_shorten("https://www.amazon.com.br/As-margens-ditado-Elena-Ferrante/dp/6555603704"))
