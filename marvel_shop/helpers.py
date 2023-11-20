import decimal
import requests
import requests_cache
import json
import time
import hashlib
import urllib.parse  




# setup our api cache location (this is going to make a temporary database storage for our api calls)

requests_cache.install_cache('image_cache', backend='sqlite')


def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"1"}

    headers = {
        "X-RapidAPI-Key": "0dfb94aa78msheb396cbe39e2fb9p12e051jsn0e705811824d",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if 'items' in data.keys():
        img_url = data['items'][1]['originalImageUrl']

    return img_url



# API_URL = 'https://gateway.marvel.com:443/v1/public/'


# def search(request):
#     data = request.json

#     type = json.get(data, 'type')

#     if type == None or type not in ['character', 'comic']:
#         # Return all character order by name
#         return 'A valid Type was not found, listing all characters', __list_all_characters()

#     filter = json.get_or_error(data, 'filter')
#     if type.lower() == 'character':
#         return 'Searching characters', search_character(filter)

#     return 'Searching comics', search_comic(filter)


# def search_character(name):
#     public_key, ts, hash = __get_api_auth()

#     response = requests.get(
#         f'{API_URL}characters?nameStartsWith={urllib.parse.quote(name)}&ts={ts}&apikey={public_key}&hash={hash}')
#     if response.status_code != 200:
#         raise Exception(response.json())

#     results = response.json()['data']['results']

#     characters = [
#         {"id": character['id'],
#          "name": character['name'],
#          "image": character['thumbnail']['path']+'.jpg',
#          "appearances":character['comics']['available']} for character in results]
#     return characters


# def search_comic(name):
#     public_key, ts, hash = __get_api_auth()

#     response = requests.get(
#         f'{API_URL}comics?titleStartsWith={urllib.parse.quote(name)}&ts={ts}&apikey={public_key}&hash={hash}')
#     if response.status_code != 200:
#         raise Exception(response.json())

#     results = response.json()['data']['results']

#     comics = [
#         {"id": comic['id'],
#          "tittle": comic['title'],
#          "image": comic['thumbnail']['path']+'.jpg',
#          "onsaleDate":comic['dates'][0]['date']} for comic in results]
#     return comics


# def search_comic_id(id):
#     public_key, ts, hash = __get_api_auth()

#     response = requests.get(
#         f'{API_URL}comics/{id}?ts={ts}&apikey={public_key}&hash={hash}')
#     if response.status_code != 200:
#         raise Exception(response.json())

#     results = response.json()['data']['results']

#     comics = [
#         {"id": comic['id'],
#          "tittle": comic['title'],
#          "image": comic['thumbnail']['path']+'.jpg',
#          "onsaleDate":comic['dates'][0]['date']} for comic in results]
#     return comics


# def __list_all_characters():
#     public_key, ts, hash = __get_api_auth()

#     response = requests.get(
#         f'{API_URL}characters?orderBy=name&ts={ts}&apikey={public_key}&hash={hash}')

#     if response.status_code != 200:
#         raise Exception(response.json())

#     results = response.json()['data']['results']

#     characters = [
#         {"id": character['id'],
#          "name": character['name'],
#          "image": character['thumbnail']['path']+'.jpg',
#          "appearances":character['comics']['available']} for character in results]
#     return characters


# def __get_api_auth():
#     public_key = __get_public_key()
#     ts = str(time.time())
#     hash = __get_hash(public_key, ts)

#     return public_key, ts, hash


# def __get_public_key():
#     public_key = config('PUBLIC_KEY')

#     if type(public_key) == None:
#         raise Exception("Public key not found.")

#     return public_key


# def __get_hash(public_key, timestamp):
#     # Assume public_key and timestamp ar not null due to current workflow
#     private_key = config('PRIVATE_KEY')
#     if type(private_key) == None:
#         raise Exception("Private key not found.")

#     str_enconded = (timestamp+private_key+public_key).encode()
#     api_key = hashlib.md5(str_enconded)
#     return api_key.hexdigest()




class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it 