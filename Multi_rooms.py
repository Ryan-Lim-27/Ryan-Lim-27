from googleapiclient.discovery import build
from google.oauth2 import service_account

class Multi_rooms:
    def __init__ (self, scope, file, sp_id) :
# If modifying these scopes, delete the file token.json.
        SCOPES = [scope]       #['https://www.googleapis.com/auth/spreadsheets']
        
        SERVICE_ACCOUNT_FILE = file   #'credentials1.json'
        
        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        self.SPREADSHEET_ID = sp_id           

        self.service = build('sheets', 'v4', credentials=creds)
        
        

    def Data(self,rooms,status):
        
        x =0
        data={}
        for x in range(len(rooms)):
    
            data[x] = {
                "range": rooms[x],           # same value stated in range_
                "majorDimension": "COLUMNS",
                "values": [[str(status[x])],]

                },
        datas=[]
        for x in range(len(rooms)):
            datas += list(data[x])

        #return value_range_body,value_input_option
        self.batch_update_values_request_body = {
        # A list of updates to apply to the spreadsheet.
        # Requests will be applied in the order they are specified.
        # If any request is not valid, no requests will be applied.
        'value_input_option': "USER_ENTERED",  # TODO: Update placeholder value.
        'data' : datas,
        }

    def api(self):
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        
        request = sheet.values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=self.batch_update_values_request_body)
        respond = request.execute()

        return print(respond)


'''
# How the input data should be interpreted.
        self.value_input_option = type  # TODO: Update placeholder value.'USER_ENTERED'


        self.value_range_body = {
            "range":self.range_,           # same value stated in range_
            "majorDimension": "COLUMNS",      # values to be filled by "ROWS" or "COLUMNS"
            "values": [[str(status1)],[str(status2)],]                 # nested array. array in array 
        }
'''
