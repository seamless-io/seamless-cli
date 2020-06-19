PACKAGE_NAME = "seamless_cli"
PACKAGE_ENTRY_POINT = "seamless"
ARCHIVE_FOR_SENDING_NAME = "seamless_package.tar.gz"
ARCHIVE_SIZE_LIMIT = 10 * 1024 * 1024  # 10 MB
SEAMLESS_SERVICE_URL = "http://core-prod-env.eba-ckbd3sw2.us-east-1.elasticbeanstalk.com/run"
# SEAMLESS_SERVICE_URL = "http://localhost:5000/run"
EXCLUDE_FOLDERS_AND_FILES = ['.git', '__pycache__', '.pytest_cache']
