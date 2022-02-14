import constants as c
from tests.endpoint_test_utils import generate_endpoint_test_scenario

SCENARIOS = {
    "sc1": generate_endpoint_test_scenario(
        title="Positive - success",
        file_name="positive.txt",
        endpoint=c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    ),
    "sc2": generate_endpoint_test_scenario(
        title="Negative - success",
        file_name="negative.txt",
        endpoint=c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    ),
    "sc3": generate_endpoint_test_scenario(
        title="Positive - failed extension (.docx)",
        file_name="positive.docx",
        failure=c.ERROR_MESSAGES.EXTENSION.format("docx", ",".join(c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS)),
        endpoint=c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    ),
    "sc4": generate_endpoint_test_scenario(
        title="Positive - failed extension (.xls)",
        file_name="positive.xls",
        failure=c.ERROR_MESSAGES.EXTENSION.format("xls", ",".join(c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS)),
        endpoint=c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    ),
    "sc5": generate_endpoint_test_scenario(
        title="No extension - failed extension (.no_extension)",
        file_name="no_extension",
        failure=c.ERROR_MESSAGES.EXTENSION.format("no_extension", ",".join(c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS)),
        endpoint=c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    ),
}
