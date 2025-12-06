import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
      "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('ss.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('book-fair')

sales = SHEET.worksheet('Sheet1')

data = sales.get_all_values()

#print(data)

def get_sales_data():
    """
    Retrieveing sales figures from user input 
    """
    print("Please enter the sales data from the last book fair")
    print("The data should be 10 numbers, separated by commas, see example below:")
    print("10, 11, 12, 13, 14, 15, 16, 17, 18, 19\n")

    data_str = input("Enter your sales here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)
    #print(f"The data provided is {data_str}")

def validate_data(values):
    """
    2 function in validate_date: Converts string values to integers + 
    check that all values of data can be converted to integers
    """
    print(values)

get_sales_data()