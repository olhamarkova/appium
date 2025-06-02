import re

def normalize(number: str) -> str:
    return re.sub(r"\D", "", number)