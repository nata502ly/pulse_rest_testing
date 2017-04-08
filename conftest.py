import pytest

from fixtures.pulse_rest_client import PulseRestAPI


@pytest.fixture()
def app():
    return PulseRestAPI(resource="books")
