from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'credentials1.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SPREADSHEET_ID = '1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'

service = build('sheets', 'v4', credentials=creds)



batch_update_values_request_body = {
    # A list of updates to apply to the spreadsheet.
    # Requests will be applied in the order they are specified.
    # If any request is not valid, no requests will be applied.
    'value_input_option': "USER_ENTERED",  # TODO: Update placeholder value.
    'data' : [
        {
            "range": 'living!B2:C2',           # same value stated in range_
            "majorDimension": "COLUMNS",
            "values": [["1"],["1"],]

        },
        {
            "range": 'Ryan Room!B2',           # same value stated in range_
            "majorDimension": "COLUMNS",
            "values": [["1"],]

        },
        
],

    # TODO: Add desired entries to the request body.
}

request = service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=batch_update_values_request_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
print(response)

