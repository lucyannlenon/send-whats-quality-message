import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "13DXXydj3SsclCLeXMasL33Mw8pJCks_NUE_z8bZjpAE"
SAMPLE_RANGE_NAME = "teste!"


def getGoogleData(line):
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  creds = getCredentials()

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'{SAMPLE_RANGE_NAME}{line}')
        .execute()
    )
    values = result.get("values", [])

    if not values:
      return None

    return values
  except HttpError as err:
    print(err)

def writeGoogleSheets(line,items):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = getCredentials()

    body = {
        'values': [items]
    }

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'{SAMPLE_RANGE_NAME}{line}', valueInputOption='RAW', body=body)
            .execute()
        )

        return None


    except HttpError as err:
        print(err)
    return

def getCredentials():
    creds = None
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          "google-client.json", SCOPES
      )
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(creds.to_json())
    return creds