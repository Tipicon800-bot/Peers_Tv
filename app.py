from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Мой сайт на Render!"

@app.route('/update')
def update_playlist():
    # Ваша логика обновления токенов, сохранения в stats.json и т.д.
    data = {"status": "updated", "tokens": 42}
    with open("stats.json", "w") as f:
        json.dump(data, f)
    return data

if __name__ == '__main__':
    app.run(debug=True)
