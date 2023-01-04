import random
import string
import json
from flask import Flask, request, redirect

app = Flask(__name__)

url_dict = {}

def generate_random_string(length: int = 6) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))  

def save_url(long_url: str) -> None:
    short_url = generate_random_string()
    while short_url in url_dict:
        short_url = generate_random_string()
    url_dict[short_url] = long_url


@app.post('/shorten')
def shorten():
    data = json.loads(request.data)
    save_url(data['long_url'])

    return url_dict

@app.get('/<short_url>')
def goto(short_url):
    if short_url in url_dict:
        return redirect(f'http://{url_dict[short_url]}')
    else:
        return f"Invalid short url. {short_url}"

app.run(debug=True)