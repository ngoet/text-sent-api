class ENDPOINT:
    class TEXT:
        SENTIMENT = "/sentiment_text"
        SENTIMENT_LONG = "/sentiment_text_long"


class API_METHOD_GROUPS:
    FILE_UPLOAD = "file_upload"
    TEXT = "text"


class EXAMPLES:
    class INPUT:
        POSITIVE = {"text": "I am feeling great today!"}

    class OUTPUT:
        POSITIVE = {
            "status": "success",
            "sentiment_score": 0.525,
            "error": None,
            "warning": None,
        }


class ERROR_MESSAGES:
    CONTACT_SUPPORT = "An unexpected error occurred. Please contact support."
    N_WORDS = "Maximum number of words exceeded for this endpoint (max = {} words; your text = {} words)"


class LIMITATIONS:
    BASIC = 200
    EXTENDED = 1500
