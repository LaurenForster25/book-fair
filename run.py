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

def get_sales_data():
    """
    Retrieving sales figures from user input 
    """
    while True:
        print("Please enter the sales data from the last book fair")
        print("The data should be 10 numbers, separated by commas, see example below:")
        print("10, 11, 12, 13, 14, 15, 16, 17, 18, 19\n")
        
        data_str = input("Enter your sales here: ")
        
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("The data you have entered is valid!")
            break

    return sales_data

def validate_data(values):
    """
    2 functions in validate_data: Converts string values to integers + 
    check that all values of data can be converted to integers
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"10 values are required for successful data entry, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again!\n") 
        return False

    return True

def update_sales_worksheet(data):
    """
    Adding a new row to sales worksheet when updated
    """
    print("The sales worksheet is updating...\n")
    sales_worksheet = SHEET.worksheet("Sheet1")
    sales_worksheet.append_row(data)
    print("You have successfully updated the sales worksheet!\n")

def main():
    """
    These are the main programme functions for the datasheet
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)

print("This is Heavenly Books Data Automation!")
main()