import re

def presence_check(name: str) -> bool:
    return bool(name)


def length_check(name: str) -> bool:
    return 2 < len(name) <= 20


def character_check(name: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z\-\s']+", name))