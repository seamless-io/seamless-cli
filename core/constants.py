PACKAGE_NAME = "seamless_cli"
PACKAGE_ENTRY_POINT = "seamless"
ARCHIVE_FOR_SENDING_NAME = "seamless_package.tar.gz"
ARCHIVE_SIZE_LIMIT = 10 * 1024 * 1024  # 10 MB
SEAMLESS_SERVICE_URL = "http://localhost:8000/run"  # TODO change to real URL
EXCLUDE_FOLDERS_AND_FILES = ['.git', '__pycache__', '.pytest_cache']
