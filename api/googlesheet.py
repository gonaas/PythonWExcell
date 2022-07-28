from googleapiclient.discovery import build
from google.oauth2 import service_account
from constants import SERVICE_ACCOUNT_FILE, SCOPES

creds = None
creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()