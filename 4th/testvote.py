from TestRequest import TestPostRequest, TestGetRequest, TestDeleteRequest
import xlrd
from testdata.testdatademo import GetTestDataPath


test_data = xlrd.open_workbook(GetTestDataPath())



testurl = "http://127.0.0.1:8000"
header = {
    'content-type': "application/x-www-form-urlencoded"
}


def test_post_vote():
    try:
        table = test_data.sheets()[1]
        for i in range(3,5):
            choice = table.cell(3, 0).value  # get 4 row, 1 colume
            status = table.cell(3, 1).value
            expectresult = table.cell(3, 2).value

            hdata = {
                "choice": int(choice)
            }

            testcaseid = "1-1"
            testname = "test_vote_" + testcaseid
            testhope = str(int(status))
            fanhuitesthope = expectresult
            r = TestPostRequest(testurl+'/polls/1/vote/', hdata, header, testcaseid, testname, testhope,fanhuitesthope)
    except Exception as e:
        print(e)

def test_get_polls():
    try:
        table = test_data.sheets()[1]
        for i in range(13,14):
            status = table.cell(i, 0).value
            expectresult = table.cell(i, 1).value
            hdata = ""
            testcaseid = "1-2"
            testname = "test_polls_" + testcaseid
            testhope = str(int(status))
            fanhuitesthope = expectresult
            r = TestGetRequest(testurl+'/polls/1/', hdata, header, testcaseid, testname, testhope,fanhuitesthope,'status')
    except Exception as e:
        print(e)


def test_get_questions():
    try:
        hdata=''
        testcaseid = "1-3"
        testname = "test_questions_" + testcaseid
        testhope = "200"
        fanhuitesthope = "success"
        r = TestGetRequest(testurl + '/polls/',hdata, header, testcaseid, testname, testhope, fanhuitesthope, 'status')
    except Exception as e:
        print(e)


def get_login():
    try:
        table = test_data.sheets()[2]
        for i in range(3,5):
            key = table.cell(i, 0).value
            phone = table.cell(i, 1).value
            pwd = table.cell(i, 2).value
            status = table.cell(i, 3).value
            expectedresult = table.cell(i, 4).value

            hdata = {
                'key': key,
                'phone': phone,
                'passwd': pwd
            }

            header1 = {
                "content-type": "application/json;charset=utf-8"
            }

            testcaseid = "1-4"
            testname = "testdemo" + testcaseid
            testhope = status
            fanhuitesthope = expectedresult
            r = TestGetRequest('https://www.apiopen.top/login', hdata, header1, testcaseid, testname, testhope, fanhuitesthope, 'code')

    except Exception as e:
        print(e)

def test_vote_login():
    try:
        table = test_data.sheets()[3]
        for i in range(2,4):
            username = table.cell(i, 0).value
            password = table.cell(i, 1).value
            status = table.cell(i, 2).value
            expectedresult = table.cell(i, 3).value

            hdata = {
                'username': username,
                'password': password
            }

            testcaseid = "1-5"
            testname = "test_vote_login" + testcaseid
            testhope = status
            fanhuitesthope = expectedresult
            r = TestPostRequest('http://127.0.0.1:8000/polls/login/', hdata, header, testcaseid, testname, testhope, fanhuitesthope)

    except Exception as e:
        print(e)

def get_singlePoetry():
    try:
        table = test_data.sheets()[4]
        for i in range(3,4):
            status = table.cell(i, 0).value
            expectedresult = table.cell(i, 1).value

            hdata = ""

            header1 = {
                "content-type": "application/json;charset=utf-8"
            }

            testcaseid = "1-6"
            testname = "test_singlePoetry" + testcaseid
            testhope = status
            fanhuitesthope = expectedresult
            r = TestGetRequest('http://api.apiopen.top/singlePoetry', hdata, header1, testcaseid, testname, testhope, fanhuitesthope, 'code')

    except Exception as e:
        print(e)


def get_music():
    try:
        table = test_data.sheets()[4]
        for i in range(3,4):
            status = table.cell(i, 0).value
            expectedresult = table.cell(i, 1).value

            hdata = ""

            header1 = {
                "content-type": "application/json;charset=utf-8"
            }

            print(hdata)
            testcaseid = "1-7"
            testname = "test_music" + testcaseid
            testhope = status
            fanhuitesthope = expectedresult
            r = TestGetRequest('http://api.apiopen.top/searchMusic', hdata, header1, testcaseid, testname, testhope, fanhuitesthope, 'code')

    except Exception as e:
        print(e)

# test_post_vote()
# test_get_polls()
#test_get_questions()
# get_login()
# test_vote_login()
# get_singlePoetry()
# get_music()
