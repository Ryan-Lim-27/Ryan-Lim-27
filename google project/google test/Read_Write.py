
from googleapiclient.discovery import build
from google.oauth2 import service_account



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = 'credentials1.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SPREADSHEET_ID = '1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'
RANGE_NAME = 'Sheet2!B5:E9'
service = build('sheets', 'v4', credentials=creds)

range_ = RANGE_NAME  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'USER_ENTERED'  # TODO: Update placeholder value.

cars = [["Ford", "Volvo", "BMW",100],["Ford", "Volvo", "BMW",200],]
 
value_range_body = {
    "range":RANGE_NAME,           # same value stated in range_
    "majorDimension": "ROWS",      # values to be filled by "ROWS" or "COLUMNS"
    "values": cars                 # nested array. array in array 
    #[
    #["hi","this","is","a","test"],["hello"]
  #]

}

# Call the Sheets API
sheet = service.spreadsheets()

request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range_, valueInputOption=value_input_option, body=value_range_body)
respond = request.execute()

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
values = result.get('values', [])

print(values)

