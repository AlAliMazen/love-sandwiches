# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values() # returns list of lists get_all_records() returns a list of dictionary


"""
following code is just for reference

for r in data:
    print(r)

if("egg salad" in data[0]):
    print("Egg salad found")
else:
    print("Not found")

print(len(data))

print(data[2][2])

for r in range(len(data)):
    for c in range(len(data[r])):
        print(f'Row: {r} Col{c} : {data[r][c]}')
"""
