import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = '-p1-R-bU_0o1JN-_-nj-5KYq_26U--'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
