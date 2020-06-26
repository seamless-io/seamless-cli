from core.constants import PACKAGE_ENTRY_POINT
from tests.integration.conftest import execute_terminal_command


def test_init_command():
    output = execute_terminal_command([PACKAGE_ENTRY_POINT, "init"])
    assert "Initializing an example seamless project" in output


def test_run_command_works():
    pass  # TODO need operational service in order to finish this integration test


def test_publish_command_works():
    pass  # TODO need operational service in order to finish this integration test
