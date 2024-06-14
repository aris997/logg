from datetime import datetime


def now(str_format: str = "%Y-%m-%d %H-%M-%S") -> str:
    """Just return a string with YY-mm-dd HH-MM-SS, I use it a lot 
    and so here we are."""
    return datetime.now().strftime(format=str_format)