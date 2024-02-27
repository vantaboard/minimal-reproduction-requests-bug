import requests_mock
import pytest

from python_requests_bug import fetch_example, fetch_example_with_bug


def test_404_bug(
    requests_mock: requests_mock.MockerCore,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    Test a 404 response with a bug on the boolean check.

    :param requests_mock: The fixture provided by the requests-mock library.
    """

    # Set up the mock response.
    requests_mock.get(
        "mock://example.com/",
        status_code=404,
    )

    fetch_example_with_bug()

    out, _ = capsys.readouterr()

    assert "Not Found" in out


def test_404(
    requests_mock: requests_mock.MockerCore,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    Test a 404 response without a bug on the boolean check.

    :param requests_mock: The fixture provided by the requests-mock library.
    """

    # Set up the mock response.
    requests_mock.get(
        "mock://example.com/",
        status_code=404,
    )

    fetch_example()

    out, _ = capsys.readouterr()

    assert "Not Found" in out
