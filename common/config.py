import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('diag.ini')

    def sections(self):
        return self.config.sections()

    def config(self):
        return self.config
