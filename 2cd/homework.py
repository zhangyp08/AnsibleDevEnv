import requests
import unittest
import HTMLTestRunner

class TestInterface(unittest.TestCase):
    def testCase1(self):
        r = requests.get('http://api.apiopen.top/searchMusic')
        self.assertEqual(r.status_code, 200)

    def testCase2(self):
        r = requests.get('http://api.apiopen.top/musicBroadcasting')
        self.assertEqual(r.encoding, 'UTF-8')

    def testCase3(self):
        r = requests.get('http://api.apiopen.top/musicBroadcastingDetails?channelname=public_tuijian_spring')
        self.assertIn("漫步春天", r.text)

    def testCase4(self):
        r = requests.get('http://api.apiopen.top/musicDetails')
        self.assertEqual(r.status_code, 200)

    def testCase5(self):
        r = requests.get('http://api.apiopen.top/musicRankings')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestInterface("testCase1"))
    suit.addTest(TestInterface("testCase2"))
    suit.addTest(TestInterface("testCase3"))
    suit.addTest(TestInterface("testCase4"))
    suit.addTest(TestInterface("testCase5"))

    fp = open('result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'Test Report',
                                           description=u'This is result of test lesson2 - Python interface test')

    runner.run(suit)
    fp.close()
