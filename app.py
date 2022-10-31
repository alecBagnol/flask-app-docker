import random

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#list of playstation games
images = [
    "https://www.listchallenges.com/f/items/8bbdbcba-1224-4b2e-84da-aa897bbafe9b.jpg",
    "https://www.listchallenges.com/f/items/4af31076-dc8d-4b52-b132-c27d140ff755.jpg",
    "https://www.listchallenges.com/f/items/ea0d2059-dfa7-47ca-ba9b-5483b749a798.jpg",
    "https://www.listchallenges.com/f/items/b03eb82d-b73a-4266-ac81-cb1861c8e3d4.jpg",
    "https://www.listchallenges.com/f/items/84897d0c-bb89-48e2-b526-905a805f4978.jpg",
    "https://www.listchallenges.com/f/items/86e9197e-654f-44e7-acf5-912fd2dfa03e.jpg",
    "https://www.listchallenges.com/f/items/4b6645f9-06f6-424b-9b6a-f4855a7c8143.jpg",
    "https://www.listchallenges.com/f/items/ff9804a4-c48f-469f-952b-f57e1d0eeb78.jpg",
    "https://www.listchallenges.com/f/items/30b442b3-998d-469f-a8af-fdca948f787c.jpg",
    "https://www.listchallenges.com/f/items/8a82fd09-5924-4659-9d42-9cb74a2ac1b0.jpg",
    "https://www.listchallenges.com/f/items/c4bdd03c-d242-4b6c-89c2-680a0da2197d.jpg",
    "https://www.listchallenges.com/f/items/c7542950-a648-49af-8807-ea83e6bd1fc1.jpg",
    "https://www.listchallenges.com/f/items/04f727d2-f935-454b-9672-3b8814ecf8ed.jpg",
    "https://www.listchallenges.com/f/items/f8d3dfda-b1cd-4406-959c-d9a77f841d47.jpg",
    "https://www.listchallenges.com/f/items/9b3b6213-e6a1-4b23-ab0b-f57eabf918a7.jpg",
    "https://www.listchallenges.com/f/items/3e77c0e8-71cf-4061-b6e1-58c8a39dd362.jpg"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
