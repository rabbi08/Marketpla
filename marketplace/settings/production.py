from settings.staging import *


# fmt: off
# Allowed hosts for the site
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["duingud.com"]

)
# fmt: on

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str("DJANGO_SITE_URL", default="https://duingud.com")


EMAIL_HOST = env.str("DJANGO_EMAIL_HOST", default="smtp.sparkpostmail.com")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=587)
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER", default="TODO")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD", default="TODO (api key)")

# Enable S3 storage
DEFAULT_FILE_STORAGE = "marketplace.storages.MediaStorage"
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", default="")
AWS_STORAGE_BUCKET_NAME = env.str(
    "DJANGO_AWS_STORAGE_BUCKET_NAME", default="marketplace-production"
)
AWS_ACCESS_KEY_ID = env.str("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("DJANGO_AWS_SECRET_ACCESS_KEY")
