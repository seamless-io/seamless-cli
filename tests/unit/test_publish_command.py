import responses
from click.testing import CliRunner

from core.constants import SEAMLESS_SERVICE_URL, SEAMLESS_SERVICE_PUBLISH_ROUTE
from core.seamless import publish


@responses.activate
def test_publish_command():
    response_str = "Running your code seamlessly"
    request_url = SEAMLESS_SERVICE_URL + SEAMLESS_SERVICE_PUBLISH_ROUTE
    responses.add(
        responses.POST, request_url, body=response_str)

    runner = CliRunner()
    result = runner.invoke(publish)

    # The right request was made
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == request_url
    assert responses.calls[0].response.text == response_str

    # The cli command printed the response text
    assert response_str in result.output
