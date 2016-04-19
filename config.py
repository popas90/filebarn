WTF_CSRF_ENABLED = True
SECRET_KEY = 'h@rd-t0-gue55-k3y'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir, 'db')

# TODO use the debug database for now
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'debug.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(dbdir, 'repository/')
SQLALCHEMY_TRACK_MODIFICATIONS = True
