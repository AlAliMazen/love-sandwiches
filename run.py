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

def get_sales_data():
    """
    Get sales figues input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six number, separated by commas.")
    print("Examples: 120,20,30,40,50,60\n")

    data_str=input("Enter your data here: ")

    #spit the data and put them into a list using split on string
    sales_data = data_str.split(",")

    #call a function to check if the length is exactly 6 and all can be converted into integers
    validate_data(sales_data)

def validate_data(values):
    """
    validate the values inside the list whether they are exactly 6 and can be converted into integers
    """
    try:
        if len(values) !=6:
            raise ValueError(
                 f'Exactly 6 figures required. You provided {len(values)}'
                )
    except ValueError as e:
        print(f'Invalid input: {e}, please try again')


get_sales_data()
