import re

from textblob import TextBlob

import constants as c
from models.data_models import Response, StatusEnum


def analyze_sentiment(text: str) -> Response:
    """
    Analyze the sentiment of a text

    :param text: An input string
    :return: A polarity score
    """
    response = Response()
    try:
        analyzed_text = TextBlob(text)
        response.sentiment_score = analyzed_text.sentiment.polarity
        response.status = StatusEnum.success
    except:
        response.error = c.ERROR_MESSAGES.CONTACT_SUPPORT
        response.status = StatusEnum.unsuccessful

    return response


def check_text_length(text: str, n_words_permitted: int) -> Response:
    """
    Check that the text length is within the required params

    :param text: The text
    :param n_words_permitted: The number of allowed words
    :return: A Response object
    """
    response = Response()
    text_length = len(re.findall(r"\w+", text))
    if text_length > n_words_permitted:
        response.error = c.ERROR_MESSAGES.N_WORDS.format(n_words_permitted, text_length)
        response.status = StatusEnum.unsuccessful
    return response
