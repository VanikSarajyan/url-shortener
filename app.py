import random
import string
import json
from flask import Flask, request, redirect, make_response

app = Flask(__name__)

url_dict = {}

def generate_random_string(length: int = 6) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))  

def save_url(long_url: str) -> str:
    short_url = generate_random_string()
    while short_url in url_dict:
        short_url = generate_random_string()
    url_dict[short_url] = long_url

    return short_url


@app.route('/shorten', methods=['POST'])
def shorten():
    data = json.loads(request.data)
    short_url = save_url(data['long_url'])

    return short_url

@app.route('/<short_url>')
def goto(short_url):
    if short_url in url_dict:
        return redirect(f'{url_dict[short_url]}')
    else:
        return f"Invalid short url. {short_url}"

app.run(debug=True)