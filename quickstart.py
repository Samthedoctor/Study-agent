import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Use the full access scope
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def create_event(service, summary, start_time, end_time, description=None):
    """Creates a single event on the user's primary calendar."""
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata', # Important to set your timezone
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }
    
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created successfully! View it here: {event.get('htmlLink')}")
    except HttpError as error:
        print(f"An error occurred: {error}")


def main():
    """Shows basic usage of the Google Calendar API."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # --- LET'S CREATE A TEST EVENT ---
        # This creates an event for tomorrow at 10:00 AM for one hour.
        # We will replace this with dynamic data from the AI later.
        
        summary = "Test Event for Study Planner"
        description = "This is a test to see if we can create events."
        
        # Get tomorrow's date
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        
        # Set start and end times
        start_time = datetime.datetime.combine(tomorrow, datetime.time(10, 0))
        end_time = start_time + datetime.timedelta(hours=1)
        
        # Call our new function to create the event
        create_event(service, summary, start_time, end_time, description)


    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()