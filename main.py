from fastapi import Body, FastAPI, File, UploadFile
from mangum import Mangum

import constants as c
from models.data_models import Payload, Response
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


handler = Mangum(app)
