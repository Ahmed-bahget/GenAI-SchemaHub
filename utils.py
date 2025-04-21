from gradio_client import Client
import json
import requests
import time
import random

client = Client("alanchen1115/gemini_api")

def generate_text(prompt):
    def check(prompt, attempt=1):
        try:
            result = client.predict(prompt=prompt, api_name="/predict")

            if result == "429 Resource has been exhausted (e.g. check quota).":
                if attempt <= 3: 
                    wait_time = 5  
                    print(f"Rate limited. Retrying attempt {attempt} in {wait_time} seconds...")
                    time.sleep(wait_time)
                    return check(prompt, attempt + 1)
                elif attempt <= 5:
                    wait_time = 60 
                    print(f"Extended wait due to persistent rate limiting. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    return check(prompt, attempt + 1)
                else:
                    print("Maximum retry attempts reached. Quota exhausted.")
                    return None
            else:
                return result

        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            return None

    return check(prompt)

api_keys = [
    'AIzaSyDAqHqVO9fRiESqLeQjslNh53ZiV36rgqI',
    'AIzaSyCUiG8Cm9TdIKasE4Ruasd0ZmLPgjSZ-nY',
    'AIzaSyCEdWSR9ATLuiEvO412pCnEhfxdLQxjIkc'
]
cx = '7266ebe81ea1a4367'


def get_google_custom_search_url(api_key, image_name):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': image_name,
        'searchType': 'image',
        'num': 1
    }
    return f'{base_url}?{requests.compat.urlencode(params)}'

def search_image(image_name):

    random.shuffle(api_keys)  
    for api_key in api_keys:
        try:
            url = get_google_custom_search_url(api_key, image_name)
            response = requests.get(url)

            if response.ok:
                data = response.json()
                items = data.get('items', [])
                if items:
                    return items[0]['link']
                else:
                    print(f"No image found for: {image_name} with key: {api_key}")
            else:
                print(f"Error with API key {api_key}: {response.status_code}, {response.reason}")
                if response.status_code == 429:  
                    print(f"Quota exceeded for API key {api_key}. Moving to next key.")
                else:
                    return None 
        except Exception as e:
            print(f"Exception occurred with API key {api_key}: {str(e)}")

    print("All API keys failed or have been exhausted. Could not retrieve image link.")
    return None

