import pytest
from app.app import get_trains_info, display_train, display_trains_info

"""List of train numbers operating in the corridor"""
ROUTE_NUMBERS = [
    6,
    14,
    15,
    24,
    28,
    35,
    37,
    38,
    42,
    51,
    52,
    53,
    54,
    59,
    60,
    62,
    63,
    64,
    67,
    68,
    69,
    72,
    73,
    75,
    76,
    84,
    87,
    690,
    693,
]


def test_get_info() -> None:
    data = get_trains_info()

    assert data is not None


def test_display_train() -> None:
    for train in ROUTE_NUMBERS:
        data = display_train(str(train))

    assert data is not None


def test_display_trains_info() -> None:
    data = display_trains_info

    assert data is not None
