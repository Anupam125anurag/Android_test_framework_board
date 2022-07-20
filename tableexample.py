
import os
import prettytable
from prettytable import ALL as ALL
items_table = prettytable.PrettyTable(hrules=ALL)
items_table.field_names = ["sl no", "Build", "Details"]

build_id=os.popen("adb shell getprop ro.build.id").read()
build_fingerprint=os.popen("adb shell getprop ro.product.build.fingerprint").read()
build_date=os.popen("adb shell getprop ro.product.build.date").read()
build_type=os.popen("adb shell getprop ro.product.build.type").read()

with open('Parser_Result.txt','r') as file:
    Str = file.read()


items = [
    {
        "sl no": "1",
        "Build": "BUILD ID",
        "Details":build_id
    },
    {
        "sl no": "2",
        "Build": "Build_Fingerprint",
        "Details":build_fingerprint
    },
    {
       "sl no": "3",
       "Build": "BUILD DATE",
       "Details":build_date
    },
    
    {
       "sl no": "4",
       "Build": "BUILD TYPE",
       "Details":build_type
    },

]

def format_details(Details, max_line_length):
    #accumulated line length
    ACC_length = 0
    words = Details.split(",")
    formatted_Details = ""
    for word in words:
        #if ACC_length + len(word) and a space is <= max_line_length 
        if ACC_length + (len(word) + 1) <= max_line_length:
            #append the word and a space
            formatted_Details = formatted_Details + word + " "
            #length = length + length of word + length of space
            ACC_length = ACC_length + len(word) + 1
        else:
            #append a line break, then the word and a space
            formatted_Details = formatted_Details + "\n" + word + " "
            #reset counter of length to the length of a word and a space
            ACC_length = len(word) + 1
    return formatted_Details

for item in items:
    item["Details"] = format_details(["Details"], 42)
    items_table.add_row([item["sl no"], item["Build"], item["Details"]])

print(items_table)
