from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'^z\xd1\x8d\xe5f\xb9\xfa\xa2J\x99\xc0\x81\xf2\xd3\xf5'
