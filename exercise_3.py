# import libraries
import json
from pandas import read_excel
filename = 'MappingDocumentExercise.xlsx'

workbook_sheet = 'in'
# open workbook and read columns
df = read_excel(filename, sheet_name = workbook_sheet)
headers = df.columns[0].split(',')

# parse rows and build dictionary with column name as keys
json_feed = []
for i in range(1,df.shape[0]):
    values = df.iloc[i][0].split(',')
    row = {}
    row[headers[0]] = values[0]
    row[headers[1]] = values[1] 
    if(values[2]!=''):
        row[headers[2]] = values[2]

    # append all dictionaries to a single array
    json_feed.append(row)

# serializing json 
json_feed_object = json.dumps(json_feed, indent = 4)
  
# writing json object to file
with open("csv_to_json_feed.json", "w") as outfile:
    outfile.write(json_feed_object)
    outfile.close()