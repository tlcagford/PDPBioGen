# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--reruns", action="store", default="2",
        help="Number of times to rerun failing tests."
    )

@pytest.fixture(scope="session", autouse=True)
def set_default_reruns(pytestconfig):
    # Default: rerun flaky tests twice
    pytestconfig.option.reruns = int(pytestconfig.getoption("--reruns"))
