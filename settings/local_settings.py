DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test_db', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'crazyministr',
        'PASSWORD': '123',
        'HOST ': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

DEBUG = True
ALLOWED_HOSTS = ['*']
