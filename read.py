from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# ID = ((URL spreadsheet - */d) - /edit*)
# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lRIDShBQU1oe7WOi6Q3FeuOCBvrAp02-A3_LhgwZ6Zs'
SAMPLE_RANGE_NAME = 'test!A1'

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Call the Sheets API

namecampos = [["numeros", "dfjdopjf", "Jkfdsapdsi"]]
registros=[["hola","adios", 5, 6.9, False, None],["hola","adios", 5, 6.9, False, None]]

request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="test!A1",valueInputOption="USER_ENTERED",body={"values":namecampos}).execute()
                                     
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="test!A:Z").execute()

values = result.get('values', [])
print(values)


