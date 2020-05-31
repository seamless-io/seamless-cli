from subprocess import PIPE, run
import pytest

collect_ignore = ["setup.py"]

from core.constants import PACKAGE_NAME


def execute_terminal_command(command):
    result = run(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return result.stdout.decode("utf-8")


@pytest.fixture(autouse=True, scope="session")
def install_the_package():
    execute_terminal_command(["pip", "install", "--editable", "."])
    yield
    # o = execute_terminal_command(["pip", "uninstall", "-y", PACKAGE_NAME])
