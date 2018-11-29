from testdata.getpath import GetTestReport

import xlsxwriter

ReportPath = GetTestReport()
print(ReportPath)
workbook = xlsxwriter.Workbook(ReportPath)
worksheet = workbook.add_worksheet()
worksheet.write("A1","Hello world")
workbook.close()