import os

from yet_another_ini import parse_from_file


def parse(filename):
    return parse_from_file(os.path.join("tests", "samples", filename))


def test_dict_header():
    assert (
        parse("dict_header.txt")
        == {
            "a": {
                "b": "c",
                "d": None
            }
        }
    )


def test_list_header():
    assert (
        parse("list_header.txt")
        == {
            "a": [
                "b",
                "c",
                "d"
            ]
        }
    )


def test_mixed_headers():
    assert (
        parse("mixed_headers.txt")
        == {
            "a": "b",
            "c": None,
            "dict": {
                "a": None,
                "b": "c"
            },
            "list": [
                "a",
                "b",
                "c"
            ]
        }
    )
