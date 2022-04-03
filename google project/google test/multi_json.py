import json
rooms = ("study!B2","living!B2","living!C2")
stat = (1,0,1)
#print (len(rooms))

x =0
data={}
for x in range(len(rooms)):
    
    data[x] = {
                "range": rooms[x],           # same value stated in range_
                "majorDimension": "COLUMNS",
                "values": [[str(stat[x])],]

            },

    #data = list(data)
datas=[]
for x in range(len(rooms)):
    datas += list(data[x])
#print (datas)

#range(0,3)


from Multi_rooms import Multi_rooms

SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
SERVICE_ACCOUNT_FILE = 'credentials1.json'
SPREADSHEET_ID = '1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'

s = Multi_rooms (SCOPE,SERVICE_ACCOUNT_FILE,SPREADSHEET_ID)
s.Data(rooms,stat)
s.api()
'''
'''