class Config:
    THREADED = True
    SECRET_KEY = b"I\x97\xcf}\x1eN$a[$\xf2\xfdT\xf1C\xf5\xb4\xeb\x97)\x19\x0eY\xab"


class Development(Config):
    DEBUG = True


class Testing(Config):
    pass


config = {
    "dev": Development,
    "testing": Testing,
}
