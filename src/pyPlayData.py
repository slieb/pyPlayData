import csv
import json
import xlrd
import pprint

# Opening a CSV file
csvfile = open('../data/data-text.csv', 'rb')
reader = csv.DictReader(csvfile)

for row in reader:
    print row

# Opening a JSON file
json_data = open('../data/data-text.json').read()
data = json.loads(json_data)

for item in data:
    print item

# Opening an EXCEL file
book = xlrd.open_workbook('../data/SOWC 2014 Stat Tables_Table 9.xlsx')
for sheet in book.sheets():
    print sheet.name

sheet = book.sheet_by_name('Table 9 ')
print "Number of rows is ", sheet.nrows

count = 0
data = {}
for i in xrange(14, sheet.nrows):
    row = sheet.row_values(i)
    country = row[1]

    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marraige': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }
    if country == 'Zimbabwe':
        break

print data['Afghanistan']

print "Pretty Print:"
pprint.pprint(data)
