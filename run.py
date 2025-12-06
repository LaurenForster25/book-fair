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

def update_surplus_worksheet(data):
    """
    Adding a new row to surplus worksheet when updated
    """
    print("The surplus worksheet is updating...\n")
    surplus_worksheet = SHEET.worksheet("Sheet2")
    surplus_worksheet.append_row(data)
    print("You have successfully updated the surplus worksheet!\n")

def calculate_surplus_data(sales_row):
    """
    Comparing the sales with the stock already had to calculate a surplus for each item.
    The surplus is found by subtracting the sales figure from the stock figure.
    Positive surplus respresents the books that were not bought.
    Negative surplus represents the books that had to be ordered in for the customer.
    """
    print("Surplus data is being calculated...")
    stock = SHEET.worksheet("Sheet3").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data
    
    
def main():
    """
    These are the main programme functions for the datasheet
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
   
print("This is Heavenly Books Data Automation!\n")
main()