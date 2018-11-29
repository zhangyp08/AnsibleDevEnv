from HTMLTestRunner import HTMLTestRunner
import unittest
import time

test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './' + now + 'result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title='Polls system interface test report',
                            description='Implementation Example with:'
                            )

    runner.run(discover)

    fp.close()