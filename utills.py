import requests


def get_cat_picture(img_path):
    url = "https://cataas.com/cat"
    response = requests.get(url)
    with open(img_path,"wb") as my_file:
        my_file.write(response.content)

# get_cat_picture("../test/test.jpg")

