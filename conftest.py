import pytest
from fixtures.pulse_rest_client import PulseRestAPI


@pytest.fixture(scope="session")
def app():
    return PulseRestAPI(resource="books")

