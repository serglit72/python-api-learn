
import pytest


def test_short_phrase():
    phrase = input("Set a phrase: ")
    length = len(phrase)

    assert length < 15, f"The given phrase has more then 15 characters"

