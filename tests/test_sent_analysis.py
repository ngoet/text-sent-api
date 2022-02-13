from utils import analyze_sentiment


def test_negative_sent() -> None:
    result = analyze_sentiment("I'm having a bad day.")
    assert (
        result.json() == '{"status": "success", "sentiment_score": -0.6999999999999998, "error": null, "warning": null}'
    )


def test_positive_sent() -> None:
    result = analyze_sentiment("I'm having a great day.")
    assert result.json() == '{"status": "success", "sentiment_score": 0.8, "error": null, "warning": null}'
