from .base import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
