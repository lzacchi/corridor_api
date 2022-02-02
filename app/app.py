from typing import Any
from flask import Flask
from markupsafe import escape  # preventhtml injection

import urllib.request, json

app = Flask(__name__)


def get_train_info() -> Any:
    with urllib.request.urlopen(
        "https://tsimobile.viarail.ca/data/allData.json"
    ) as url:
        train_info = json.loads(url.read().decode())

    return train_info


@app.route("/train-info")
def display_train_info() -> Any:
    train_info = get_train_info()
    return train_info


@app.route("/train-info/<train_number>")
def display_train(train_number: str) -> Any:
    train_info = get_train_info()

    return train_info[train_number]
