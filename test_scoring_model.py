import unittest
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class test_verification(unittest.TestCase):

    def test_request(self):
        param =     [{"PIN_CODE": "1234567",
                    "UNICAL_CODE": 1234678901,
                    "APP_ID": "{AaBb123456789CcDddEefq1}"}]
        response = requests.post("http://127.0.0.1:8000/scoring", json=param)

        logger.info("Request data: %s", param)
        logger.info("Response status code: %s", response.status_code)
        logger.info("Response data: %s", response.json())

        self.assertEqual(response.status_code, 200)

        self.assertIn("score", response.json())

        score = response.json()["score"]
        self.assertTrue(0 <= score <= 100)
if __name__ == "__main__":
    unittest.main()