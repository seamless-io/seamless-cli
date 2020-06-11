import responses
from click.testing import CliRunner

from core.constants import SEAMLESS_SERVICE_URL
from core.seamless import run


@responses.activate
def test_run_command():
    response_str = "Running your code seamlessly"
    responses.add(
        responses.POST, SEAMLESS_SERVICE_URL, body=response_str)

    runner = CliRunner()
    result = runner.invoke(run)

    # The right request was made
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == SEAMLESS_SERVICE_URL
    assert responses.calls[0].response.text == response_str

    # The cli command printed the response text
    assert response_str in result.output
