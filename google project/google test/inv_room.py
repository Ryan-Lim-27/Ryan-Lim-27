from googleapiclient.discovery import build
from google.oauth2 import service_account

class Room:
    def __init__ (self, scope, file, sp_id, cell) :
# If modifying these scopes, delete the file token.json.
        SCOPES = [scope]       #['https://www.googleapis.com/auth/spreadsheets']
        
        SERVICE_ACCOUNT_FILE = file   #'credentials1.json'
        
        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        self.SPREADSHEET_ID = sp_id              #'1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'

        self.service = build('sheets', 'v4', credentials=creds)

        self.range_ = cell       #'Sheet1!A1'  # TODO: Update placeholder value.
        
        

    def Data(self,status):
    # How the input data should be interpreted.
        self.value_input_option = 'USER_ENTERED'  # TODO: Update placeholder value.'USER_ENTERED'


        self.value_range_body = {
            "range":self.range_,           # same value stated in range_
            "majorDimension": "ROWS",      # values to be filled by "ROWS" or "COLUMNS"
            "values": [[str(status)],]                 # nested array. array in array 
        }
        #return value_range_body,value_input_option

    def api(self):
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        
        request = sheet.values().update(spreadsheetId=self.SPREADSHEET_ID, range=self.range_, 
                                        valueInputOption=self.value_input_option, body=self.value_range_body)
        respond = request.execute()

        return print(respond)