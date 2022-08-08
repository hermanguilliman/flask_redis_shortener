import os


def cast_bool(value: str) -> bool:
    if not value:
        return False
    return value.lower() in ("true", "t", "1", "yes")


class Config:
    FLASK_DEBUG: bool = cast_bool(os.environ.get('FLASK_DEBUG')) or True
    URL_LEN: int = os.environ.get('URL_LEN', 4)
    SITE_NAME = os.environ.get('SITE_NAME', 'Flask of Redis url shortener')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'flask_url_shortener'
    REDIS_URL = ""