from fastapi import Body, FastAPI, File, UploadFile
from mangum import Mangum

import constants as c
from models.data_models import Payload, Response, StatusEnum
from utils import analyze_sentiment, check_text_length

app = FastAPI(title="TextSentimentAPI")


@app.post(
    c.ENDPOINT.TEXT.SENTIMENT,
    name="Sentiment analysis for a text",
    description="",
    responses={
        200: {
            "description": "Analyze the sentiment of a text",
            "content": {"application/json": c.EXAMPLES.OUTPUT.POSITIVE},
        },
    },
    tags=[c.API_METHOD_GROUPS.TEXT],
    response_model=Response,
)
async def sentiment(payload: Payload = Body(..., example=c.EXAMPLES.INPUT.POSITIVE)) -> Response:
    """
    Analyze the sentiment of a text

    :param payload: Input (should be a valid JSON)
    :return: A Response object
    """
    response = check_text_length(text=payload.text, n_words_permitted=c.LIMITATIONS.BASIC)
    if not response.error:
        response = analyze_sentiment(payload.text)

    return response


@app.post(
    c.ENDPOINT.TEXT.SENTIMENT_LONG,
    name="Sentiment analysis for a long text",
    description="",
    responses={
        200: {
            "description": "Analyze the sentiment of a long text",
            "content": {"application/json": c.EXAMPLES.OUTPUT.POSITIVE},
        },
    },
    tags=[c.API_METHOD_GROUPS.TEXT],
    response_model=Response,
)
async def sentiment_long(payload: Payload = Body(..., example=c.EXAMPLES.INPUT.POSITIVE)) -> Response:
    """
    Analyze the sentiment of a long text

    :param payload: Input (should be a valid JSON)
    :return: A Response object
    """
    response = check_text_length(text=payload.text, n_words_permitted=c.LIMITATIONS.EXTENDED)
    if not response.error:
        response = analyze_sentiment(payload.text)

    return response


@app.post(
    c.ENDPOINT.FILE_BASED.SENTIMENT_FILE,
    name="Sentiment analysis for .doc, .docx and .txt files",
    description="",
    responses={
        200: {
            "description": "Analyze the sentiment of text in a .txt file",
            "content": {"application/json": c.EXAMPLES.OUTPUT.POSITIVE},
        },
    },
    tags=[c.API_METHOD_GROUPS.FILE_UPLOAD],
    response_model=Response,
)
async def sentiment_file(file: UploadFile = File(...)) -> Response:
    """
    Analyze the sentiment of a text

    :param file: Input file containing raw text
    :return: A Response object
    """
    extension = file.filename.split(".")[-1]
    if extension in c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS:
        contents = await file.read()
        contents = contents.decode("utf-8")
        response = check_text_length(text=contents, n_words_permitted=c.LIMITATIONS.BASIC)
        if not response.error:
            response = analyze_sentiment(contents)
    else:
        response = Response()
        response.status = StatusEnum.unsuccessful
        response.error = c.ERROR_MESSAGES.EXTENSION.format(
            extension, ", ".join(c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS)
        )

    return response


@app.post(
    c.ENDPOINT.FILE_BASED.SENTIMENT_FILE_LONG,
    name="Sentiment analysis for .doc, .docx and .txt files",
    description="",
    responses={
        200: {
            "description": "Analyze the sentiment of text in a .txt file",
            "content": {"application/json": c.EXAMPLES.OUTPUT.POSITIVE},
        },
    },
    tags=[c.API_METHOD_GROUPS.FILE_UPLOAD],
    response_model=Response,
)
async def sentiment_file_long(file: UploadFile = File(...)) -> Response:
    """
    Analyze the sentiment of a long text

    :param file: Input file containing raw text
    :return: A Response object
    """
    extension = file.filename.split(".")[-1]
    if extension in c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS:
        contents = await file.read()
        contents = contents.decode("utf-8")
        response = check_text_length(text=contents, n_words_permitted=c.LIMITATIONS.EXTENDED)
        if not response.error:
            response = analyze_sentiment(contents)
    else:
        response = Response()
        response.status = StatusEnum.unsuccessful
        response.error = c.ERROR_MESSAGES.EXTENSION.format(
            extension, ", ".join(c.ENDPOINT.FILE_BASED.SUPPORTED_EXTENSIONS)
        )

    return response


handler = Mangum(app)
