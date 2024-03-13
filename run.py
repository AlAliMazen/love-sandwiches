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


"""
following code is just for reference
sales = SHEET.worksheet('sales')
data = sales.get_all_values() # returns list of lists get_all_records() returns a list of dictionary

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
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: \n")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
# the two functions for updating sales and surplus worksheets are now removed and refactored


# refactoring the code is the process of restructuring the code to improve its readability 
def update_worksheet(data, worksheet):
    """
    update worksheet, add new row with the list data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update=SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet was updated successfully\n")

def calculate_surplus_data(sales_data):
    """
    surplus is when market needs more sandwiches to be made fresh and will be 
    thrown away if any sandwiches didn't got sold. Surplus is the result of 
    stock-sales .
     - positive result indicates waste 
     - negative result indicate extra made fresh when sold out

    """
    print("Calculating surplus data...\n")
    stock=SHEET.worksheet('stock').get_all_values()
    #pprint(stock)#this function is used to print the whole list in a table like
    stock_row=stock[-1]
    # now we need a way of subtracting two lists or rows of a list. in order to do this we need to use the zip function 
    surplus_data=[]
    for stock, sales in zip(stock_row,sales_data):
        surplus=int(stock)-sales
        surplus_data.append(surplus)
    
    return surplus_data

def get_last_5_entries_sales():
    """
    it should get only the 5 entries of each column in order to calculate the sales data which is a 
    result of average of the last 5 entries. 
    Collects columns of the data from sales worksheet, collecting the last 5 entries
    for each sandwiches and returns the data as a list of lists
    """
    sales=SHEET.worksheet('sales')
    #column=sales.col_values(3)
    #print(column)
    
    columns = []
    for ind in range(1,7):
        column= sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculate stock data...\n")
    new_stock_data = []
    for column in data:
        int_column=[int(val) for val in column]
        average=sum(int_column)/len(column)
        #adding 10% 
        stock_num=average*1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data








# it is best practice to wrap all calling function in a main function which in turn call other functions
def main():
    """
    Run all program function
    """
    data = get_sales_data()
    sales_data=[int(value) for value in data]
    update_worksheet(sales_data,"sales")
    new_surplus_data=calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data,"surplus")
    last_5_sales_entries=get_last_5_entries_sales()
    stock_data=calculate_stock_data(last_5_sales_entries)
    update_worksheet(stock_data,"stock")

print("Welcome to love Sandwiches Data automation")
main()