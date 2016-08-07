import xlrd

book = xlrd.open_workbook ('../data/SOWC 2014 Stat Tables_Table 9.xlsx')
for sheet in book.sheets():
    print sheet.name

sheet = book.sheet_by_name('Table 9 ')
print "Number of rows is ", sheet.nrows

for i in range(sheet.nrows):
    print sheet.row_values(i)