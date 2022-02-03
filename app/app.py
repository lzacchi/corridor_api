from typing import Any
from markupsafe import escape  # preventhtml injection

from flask import Flask
import requests
import requests_cache
import json

api_corridor = Flask(__name__)

requests_cache.install_cache("trains_cache", expire_after=300)


def get_trains_info() -> Any:
    url = "https://tsimobile.viarail.ca/data/allData.json"

    with requests.Session() as session:
        response = session.get(url)
        trains_info = response.json()

    return trains_info


@app.route("/")
def display_trains_info() -> Any:
    trains_info = get_trains_info()
    return trains_info


@app.route("/<train_number>")
def display_train(train_number: str) -> Any:
    train_info = get_trains_info()

    return train_info[escape(train_number)]


if __name__ == "__main__":
    api_corridor.run(port=5000)
