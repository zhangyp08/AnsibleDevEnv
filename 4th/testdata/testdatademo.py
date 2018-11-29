import os
import xlrd

def GetTestDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testdata", "TestData.xls")

# print(GetTestDataPath())
#
#
# test_data = xlrd.open_workbook(GetTestDataPath())
#
# table = test_data.sheets()[1]
#
# choice = table.cell(3,0).value
#
# print(choice)