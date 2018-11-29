import unittest
import requests
import json


class testpools(unittest.TestCase):
    base_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Language': 'en-US'
    }
    def setUp(self):
        self.url = "http://127.0.0.1:8000/polls/"

    def test_get_question(self):  # get all vote questions
        result = requests.get(self.url)
        code = result.status_code
        text = result.text
        dicts = json.loads(text)
        self.assertEqual(code, 200)
        self.assertEqual(dicts['message'], 'success')
        self.assertEqual(dicts['data']['1'], "请选择你喜欢的游戏？")

    def test_get_choices(self):
        result = requests.get(self.url)
        code = result.status_code
        text = result.text
        dicts = json.loads(text)
        if code == 200:
            question_len = len(dicts['data']) + 1
            for item in range(1,question_len):
                url = self.url + "{}/".format(item)
                print(url)
                result = requests.get(url)
                text = result.text
                d = json.loads(text)
                self.assertEqual(d["status"], "200")
                self.assertEqual(d['message'], 'success')

    def test_set_votes(self):

        url = self.url + "1/vote/"
        d={"choice": "3"}
        result = requests.post(url, data=d)
        code = result.status_code
        text = result.text
        dicts = json.loads(text)
        self.assertEqual(dicts["status"], "200")
        self.assertEqual(dicts['message'], 'success')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
