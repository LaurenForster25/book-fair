import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
      "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('ss.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)