import pytest
import requests

class TestHWex10:

    def test_length_phrase(self):
        phrase = input("Set the phrase less than 15 characters: ")

        assert len(phrase) <= 15, f"Input phrase length more than 15 symbols: {len(phrase)}"
        print(f"Input phrase length: {len(phrase)}")