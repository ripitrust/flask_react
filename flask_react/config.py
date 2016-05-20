import os


class Config(object):

    def __init__(self, name=None, path=None):

        self.name = name
        self.path = os.path.abspath(path)
