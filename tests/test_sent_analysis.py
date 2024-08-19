import os
import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from utils import analyze_sentiment


class TestSentUtils(unittest.TestCase):
    def test_negative_sent(self) -> None:
        result = analyze_sentiment("I'm having a bad day.")
        self.assertEqual(
            result.json(),
            '{"status": "success", "sentiment_score": -0.6999999999999998, "error": null, "warning": null}',
        )

    def test_positive_sent(self) -> None:
        result = analyze_sentiment("I'm having a great day.")
        self.assertEqual(result.json(), '{"status": "success", "sentiment_score": 0.8, "error": null, "warning": null}')


if __name__ == "__main__":
    unittest.main()
