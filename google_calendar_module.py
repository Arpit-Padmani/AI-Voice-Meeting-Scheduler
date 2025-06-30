import datetime
import os.path
# import json
import pytz
import dateparser

from IPython.core.formatters import JSONFormatter
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


class GoogleCalendarAPI:
    def __init__(self):
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                self.creds = flow.run_local_server(port=8080, redirect_uri_trailing_slash=False)

            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

        self.service = build("calendar", "v3", credentials=self.creds)

    def insertEventToGooleCelender(self, meeting_info):

        timezone = 'Asia/Kolkata'
        start_dt = datetime.datetime.strptime(meeting_info['datetime'], "%Y-%m-%d %H:%M:%S")
        start_dt = pytz.timezone(timezone).localize(start_dt)
        end_dt = start_dt + datetime.timedelta(hours=12)

        start_iso = start_dt.isoformat()
        end_iso = end_dt.isoformat()  # Add 1 hour

        event = {
            'summary': meeting_info['title'],
            'start': {
                'dateTime': start_iso,
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end_iso,
                'timeZone': 'America/Los_Angeles',
            }
        }
        event_result = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
        # print("Event created: (event_result.get('htmlLink'))  # Placeholder",meeting_info['intent'])

    def getAllEvenets(self):
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        print("Getting the upcoming 10 events")
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])


if __name__ == "__main__":
    try:
        calendar = GoogleCalendarAPI()
        # Example usage:
        # calendar.insertEventToGooleCelender(meeting_info)
        calendar.getAllEvenets()
    except HttpError as error:
        print(f"An error occurred: {error}")
