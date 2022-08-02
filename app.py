from flask import Flask, render_template
import random

app = Flask(__name__)
# list of cat images

images = [
    "https://image.freepik.com/free-photo/gray-kitty-with-monochrome-wall-her_23-2148955126.jpg",
    "https://image.freepik.com/free-photo/cute-kitten-bed_1303-9321.jpg",
    "https://image.freepik.com/free-photo/selective-focus-black-white-adorable-cat-with-its-tongue-out_181624-35744.jpg",
    "https://image.freepik.com/free-photo/closeup-cute-bengal-cat-lying-bed_181624-35234.jpg",
    "https://image.freepik.com/free-photo/orange-grumpy-cat-grey_181624-19364.jpg",
    "https://image.freepik.com/free-photo/gold-bengal-cat-white-space_155003-12732.jpg",
    "https://image.freepik.com/free-photo/gold-bengal-cat-black-space_155003-12730.jpg"
]
@app.route('/')

def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
