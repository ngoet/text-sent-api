import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

import requests

import constants as c


@dataclass
class Scenario:
    title: str
    file_name: Optional[str] = None
    warning: Optional[str] = None
    failure: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    base_url: str = "http://127.0.0.1:8000"
    endpoint: str = c.ENDPOINT.FILE_BASED.SENTIMENT_FILE
    request_body: Optional[Union[str, dict]] = None

    @property
    def file_path(self) -> str:
        return os.path.join(os.getcwd(), "tests", "test_data", self.file_name)


def run_endpoint_test(scenario: Scenario) -> None:
    """
    Run an endpoint test.
    """

    url = f"{scenario.base_url}{scenario.endpoint}"

    if scenario.endpoint in get_class_attributes(c.ENDPOINT.FILE_BASED):
        r = requests.post(
            url=url,
            files={
                "file": (
                    scenario.file_name,
                    open(scenario.file_path, "rb"),
                    "multipart/form-data",
                )
            },
            headers=scenario.headers,
        )
    else:
        r = requests.post(
            url=url,
            headers=scenario.headers,
            json=scenario.request_body,
        )

    output = json.loads(r.content.decode("UTF-8"))

    if scenario.failure:
        assert output["error"] == scenario.failure

    else:
        assert r.status_code == 200

        if scenario.warning:
            assert output.get("warning", None) == scenario.warning

        Path("tmp_files").mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = f"tmp_files{scenario.endpoint}_{scenario.title.replace(' ','_')}_{timestamp}.json"

        with open(file_name, "w") as w:
            json.dump(output, w)


def generate_endpoint_test_scenario(
    title: str,
    endpoint: str,
    failure: Optional[str] = None,
    warning: Optional[str] = None,
    file_name: Optional[str] = None,
    request_body: Optional[Union[str, dict]] = None,
) -> Scenario:
    """
    Generate and endpoint tests scenario

    :param title: The title of the scenario
    :param file_name: The name of the file that is transformed using the endpoint
    :param endpoint: The name of the endpoint
    :param failure: The expected failure message (if applicable)
    :param warning: The expected warning message (if applicable)
    :param request_body: The request body associated with the payload
    :return: A Scenario object
    """
    local = os.environ.get("LOCAL", "True") == "True"
    assert int(bool(file_name)) + int(bool(request_body)) == 1, "One of file_name and request_body should be specified"
    prefix = "[local]" if local else "[FastAPI]"
    title = f"{prefix}{title}"

    scenario = Scenario(
        title=title,
        file_name=file_name,
        base_url="http://127.0.0.1:8000" if local else os.environ["BASE_URL"],
        endpoint=endpoint,
        warning=warning,
        request_body=request_body,
        failure=failure,
    )

    return scenario


def get_class_attributes(obj) -> List[str]:
    """
    Function to obtain the values of all attributes of a class.

    :param ClassVar obj: A tmp_files ingestion constants class
    :return: List[str] class_vals: A list containing the values of all
    attributes associated with the class.
    """
    class_objects = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    class_vals = [getattr(obj, i) for i in class_objects]

    return class_vals
