from googleapiclient.discovery import build
from google.oauth2 import service_account


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = 'credentials1.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SPREADSHEET_ID = '1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'

service = build('sheets', 'v4', credentials=creds)
range_ = 'Sheet1!A15' #pointer
value_input_option = 'USER_ENTERED' 

# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.


ValuesRange = {
    "range":range_,                                                                     # same value stated in range_
    "majorDimension": "COLUMNS",                                                        # values to be filled by "ROWS" or "COLUMNS"
    "values": [["hi","this","is","a","test"],["hello","and","Goodbye"]]                 # nested array. array in array 
}

value_range_body = ValuesRange                                                          # Same request format as Read_Write

request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=range_, valueInputOption=value_input_option, 
                                                        insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()
print(response)