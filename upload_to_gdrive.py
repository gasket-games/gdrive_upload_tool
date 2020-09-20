import pickle
import pprint
import os.path
import argparse
import datetime
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Requires a credentials.json file (make one here: https://console.developers.google.com/apis/credentials)
# Requires auth via web-browser to get a token which will be cached to a file (one-time)

parser = argparse.ArgumentParser()
parser.add_argument("source_path", help="local path to file you want to upload")
parser.add_argument("dest_path", help="destination folder on gdrive you want to upload to")
args = parser.parse_args()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    startTime = datetime.datetime.now()

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    print(f"Connecting to GDrive... {datetime.datetime.now() - startTime}")

    service = build('drive', 'v3', credentials=creds)

    filename = Path(args.source_path).name

    file_metadata = {'name': filename,
                     'parents': [ args.dest_path ]}
    media = MediaFileUpload(args.source_path,
                            resumable=True)

    print(f"About to upload {filename} ({args.source_path}) to {args.dest_path} {datetime.datetime.now() - startTime}")

    request = service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id',
                                     supportsAllDrives=True).execute()

    print(f"Upload requested {datetime.datetime.now() - startTime}")

    pprint.pprint(request)

    print(f"Upload complete {datetime.datetime.now() - startTime}")

if __name__ == '__main__':
    main()
