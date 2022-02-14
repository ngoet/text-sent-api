"""
    Local endpoint tests.

    Requires that the app is running locally (run `uvicorn main:app --reload`)
"""

import os

import pytest

from tests.endpoint_scenarios import SCENARIOS
from tests.endpoint_test_utils import run_endpoint_test

os.environ["LOCAL"] = "True"


@pytest.mark.parametrize("scenario", list(SCENARIOS.values()), ids=SCENARIOS.keys())
def test_eval(scenario):
    run_endpoint_test(scenario)
