"""
The cat_service module is responsible for getting cat images from the web
and storing them in the folder specified by the user.
"""
import os
import shutil

import requests


def get_cat(folder, name):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url)

    return response.raw


def save_image(folder: str, name: str, data):
    file_name = os.path.join(folder, name + ".jpg")

    with open(file_name, "wb") as fout:
        shutil.copyfileobj(data, fout)
