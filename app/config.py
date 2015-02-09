import os
# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x0b\xe2\xca\xd6(q\x1d\xd8\xd8\xcb\xa1\x0b5\xbf\x08k!\xe4\x1f\xcd\xfeN`\xf0'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)