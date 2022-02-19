"""
    Integration tests
    =================
    Please verify that your IP address is whitelisted in your deployed API Gateway REST API to run these tests.
"""

import os

import pytest

from tests.endpoint_scenarios import SCENARIOS
from tests.endpoint_test_utils import run_endpoint_test  # run_endpoint_test

os.environ["LOCAL"] = "False"
os.environ["BASE_URL"] = ""  # Add if you want to run integration tests (!)


@pytest.mark.parametrize("scenario", list(SCENARIOS.values()), ids=SCENARIOS.keys())
def test_eval(scenario):
    run_endpoint_test(scenario)
