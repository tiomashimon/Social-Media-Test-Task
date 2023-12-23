import requests
import json
from datetime import datetime
import random
import os


path = os.getcwd()

def load_config():
    with open(path + '/bot_config.json', 'r') as file:
        config = json.load(file)
    return config

def create_user(username, password):
    url = 'http://127.0.0.1:8000/api/user/'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    print(response)

def create_post(title, content, created_by):
    url = 'http://127.0.0.1:8000/api/post/'
    data = {'title': title, 'content': content, 'created_by': created_by}
    response = requests.post(url, data=data)

def create_like_unlike(user_id, post_id):
    url = 'http://127.0.0.1:8000/api/post/like-unlike/'
    data = {'user': user_id, 'post': post_id}
    response = requests.put(url, data=data)

def save_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def get_and_save_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        save_data_to_json(data, filename)
        print(f"Data from {url} saved to {filename}.")
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}, Response: {response.text}")

def create_daily_likes():
    url = 'http://127.0.0.1:8000/api/post/daily-likes/'
    data = {'date': datetime.now().strftime('%Y-%m-%d')}
    response = requests.post(url, data=data)

def create_random_posts_and_likes(user_id, max_posts, max_likes):
    for _ in range(random.randint(1, max_posts + 1)):
        create_post(f"Random Post by {user_id}", f"Random Post Content for {user_id}", user_id)

    for _ in range(random.randint(1, max_likes + 1)):
        post_id = random.randint(1, max_posts + 1)
        create_like_unlike(user_id, post_id)

if __name__ == "__main__":
    config = load_config()

    create_daily_likes()

    for i in range(1, config.get('number_of_users') + 1):
        username = f"example_user{i}"
        password = f"example_password{i}"
        create_user(username, password)

        create_random_posts_and_likes(i, config.get('max_posts_per_user', 50), config.get('max_likes_per_user', 50))

    get_and_save_data('http://127.0.0.1:8000/api/post/', 'posts_data.json')
    get_and_save_data('http://127.0.0.1:8000/api/user/', 'users_data.json')
