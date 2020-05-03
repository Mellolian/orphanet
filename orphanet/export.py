import gspread
from google.oauth2.service_account import Credentials
import json

batch = []





scopes = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file(
    'bmlweb-e88f8b6ea0d8.json', scopes=scopes)
gc = gspread.authorize(credentials)
# Open a sheet from a spreadsheet in one go
wks = gc.open("Orphanet").sheet1

j = 1
with open('data.txt', 'r') as f:
    for line in f.readlines():
        batch.append(json.loads(line))
        if len(batch)> 950:
            wks.batch_update([{
            'range': f'A2:J{2+len(batch)}',
            'values': batch,
        }])
            wks = gc.open("Orphanet").get_worksheet(j)
            j += 1
            batch = []
    wks.batch_update([{
    'range': f'A2:J{2+len(batch)}',
    'values': batch,
}])
    
            