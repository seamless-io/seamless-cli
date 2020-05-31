from core.constants import PACKAGE_NAME
from tests.conftest import execute_terminal_command


def test_init_command():
    output = execute_terminal_command([PACKAGE_NAME, "init"])
    assert "Initializing an example seamless project" in output


def test_run_command_works():
    output = execute_terminal_command([PACKAGE_NAME, "run"])
    assert "Running your code seamlessly" in output


def test_publish_command_works():
    output = execute_terminal_command([PACKAGE_NAME, "publish"])
    assert "Publishing your code..." in output
    assert "Success!" in output

    output = execute_terminal_command([PACKAGE_NAME, "publish", "--schedule", "test_schedule"])
    assert "Publishing your code to run on schedule test_schedule..." in output
    assert "Success!" in output
