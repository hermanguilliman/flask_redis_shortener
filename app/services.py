from app import redis
from random import choices
from string import ascii_lowercase

def create_string(source_list, length: int) -> str:
    return ''.join(choices(source_list, k=length))

def _create_uniq_short_url(src, length: int) -> str:
    for a in range(5):
        short = ''.join(choices(src, k=length))
        if not redis.get(short):
            return short
    return "EASTER_EGG"

def get_short_url(full_url, length: int) -> str:
    short = _create_uniq_short_url(src=ascii_lowercase, length=length)
    redis.set(short, full_url)
    return short

def get_full_url(short_url) -> str:
    result = redis.get(short_url)
    if result:
        return result.decode("utf-8")
    else:
        return result


if __name__ == "__main__":
    pass
    

