import schedule
import time
import datetime
import pytz
from plyer import notification
from google_calendar_module import GoogleCalendarAPI
from text_to_speech import speak_text

def task_reminder(event_title, event_time):
    speak_text(f"Reminder: Your event '{event_title}' is scheduled at {event_time.strftime('%I:%M %p')}")
    notification.notify(
        title="Reminder: Upcoming Event",
        message=f"{event_title} at {event_time.strftime('%I:%M %p')}",
        # ap='icon.ico',
        timeout=10
    )

def schedule_google_events():
    calendar = GoogleCalendarAPI()
    events = calendar.getAllEvenets()
    now = datetime.datetime.now(pytz.utc)

    for event in events:
        title = event.get('summary', 'No Title')
        start = event.get('start', {}).get('dateTime')

        if not start:
            continue  # Skip events without start datetime

        event_time = datetime.datetime.fromisoformat(start)

        if event_time.tzinfo is None:
            event_time = pytz.utc.localize(event_time)

        # Schedule 10 minutes before event
        reminder_time = event_time - datetime.timedelta(minutes=10)
        local_time = reminder_time.astimezone()  # Convert to local timezone

        # Format for schedule (HH:MM)
        reminder_str = local_time.strftime("%H:%M")

        if reminder_time > now:
            print(f"✅ Scheduled reminder for '{title}' at {reminder_str}")
            schedule.every().day.at(reminder_str).do(task_reminder, title, event_time)
        else:
            print(f"❌ Skipped past event '{title}'")

# Initial load
schedule_google_events()

# Run pending tasks
while True:
    schedule.run_pending()
    time.sleep(1)