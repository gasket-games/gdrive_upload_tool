Use GSuite and want a command line tool to upload files to Google Drive? `upload_to_gdrive.py` can do the trick.

Usage:
`python upload_to_gdrive.py "local_file_path" "destination_gdrive_location_code"`
* _local_file_path_ is the complete path to the file on your computer you want to upload. For example: `C:\Stuff\thing.zip` for Windows.
* _destination_gdrive_location_code_ is that text you see at the end of the URL when you are within a GDrive folder. For example: `https://drive.google.com/drive/folders/1234SomethingOnlyTheComputerUnderstands` <- the part after `/folders/`.

Heavily based on https://developers.google.com/drive/api/v3/quickstart/python (you'll want to follow the instructions there for creating your app id and installing prerequisites)
