import re

"""
Validations to check against the user submitted name

Presence Check - checks that a name is entered
Length Check - checks that the name is a suitable length
Character Check - checks that only valid characters are used in the name.
"""

def presence_check(name: str) -> bool:
    return bool(name)


def length_check(name: str) -> bool:
    return 2 < len(name) <= 20


def character_check(name: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z\-\s']+", name))