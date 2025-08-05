import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "instance", "artgallery.db")}'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/artgallery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1009200290018'