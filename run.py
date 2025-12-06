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

sales = SHEET.worksheet('Sales')

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

#def update_sales_worksheet(data):
#    """
#    Adding a new row to sales worksheet when updated
#    """
#    print("The sales worksheet is updating...\n")
#    sales_worksheet = SHEET.worksheet("Sheet1")
#    sales_worksheet.append_row(data)
#    print("You have successfully updated the sales worksheet!\n")

#def update_surplus_worksheet(data):
#    """
#    Adding a new row to surplus worksheet when updated
#    """
#    print("The surplus worksheet is updating...\n")
#    surplus_worksheet = SHEET.worksheet("Sheet2")
#   surplus_worksheet.append_row(data)
#    print("You have successfully updated the surplus worksheet!\n")

def update_worksheet(data, worksheet):
    """
    Recieves the list of data from user to be inserted into the worksheets.
    Updates the relevant worksheet with the integers provided.
    """
    print(f"The {worksheet} worksheet is updating...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"You have successfully updated the {worksheet} worksheet!\n")

def calculate_surplus_data(sales_row):
    """
    Comparing the sales with the stock already had to calculate a surplus for each item.
    The surplus is found by subtracting the sales figure from the stock figure.
    Positive surplus respresents the books that were not bought.
    Negative surplus represents the books that had to be ordered in for the customer.
    """
    print("Surplus data is being calculated...")
    stock = SHEET.worksheet("Stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def get_last_5_entries_sales():
    """
    This will collect the data from the last five entries of the sales worksheet,
    returning the data as a list
    """
    sales = SHEET.worksheet("Sales")
    
    columns = []
    for ind in range(1, 11):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

    columns = []
    for ind in range(10):
        print(ind)

def calculate_stock_data(data):
    """
    Calculating the stock average for each book and adding 10%
    """
    print("The system is calculating stock data...\n")
    new_stock_data = []
    
    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data
    
def main():
    """
    These are the main programme functions for the datasheet
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "Sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "Stock")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "Stock")
   
print("This is Heavenly Books Data Automation!\n")
#main()





