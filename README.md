

# 🗣️ AI Voice Meeting Scheduler

**AI Voice Meeting Scheduler** is a smart voice-activated assistant that helps users effortlessly schedule meetings using natural language commands. It integrates with Google Calendar to create events, set reminders, and provides timely desktop notifications — making meeting management seamless and hands-free.

 ---

## 📽️ Demo Video

Watch the demo of **AI Voice Meeting Scheduler** in action:

[![Watch the video](https://github.com/user-attachments/assets/5788511e-79c4-4cd9-b15a-1feb3f6fcf31)](https://github.com/user-attachments/assets/5788511e-79c4-4cd9-b15a-1feb3f6fcf31)

> Click the image above or [watch the demo](https://github.com/user-attachments/assets/5788511e-79c4-4cd9-b15a-1feb3f6fcf31)


## 🚀 Features

- 🎙️ **Voice-Based Commands**  
  > Example: “Schedule my meeting with Raj on 14th July at 8 PM”  
  → Automatically schedules a calendar event with title, date, and time.

- 📅 **Google Calendar Integration**  
  - Adds events to your Google Calendar.  
  - Auto-generates meeting titles and timestamps from voice.

- ⏰ **Reminders & Notifications**  
  - Prompts user to set reminders after scheduling.  
  - Sends real-time desktop notifications before meetings.

 

## 🧠 How It Works

1. **Voice Input**: User gives a voice command.
2. **Natural Language Processing**: Extracts date, time, and title.
3. **Google Calendar API**: Event is created in your calendar.
4. **Reminder Handling**: Asks if a reminder should be set.
5. **Notification Scheduler**: Displays a system notification before the event.

 

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Arpit-Padmani/AI-Voice-Meeting-Scheduler.git
cd AI-Voice-Meeting-Scheduler
````

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

 

## ⚙️ Environment Setup

### 🔑 Google Calendar API Setup

To enable calendar access and event scheduling:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Calendar API**.
4. Go to **Credentials**:

   * Click **Create Credentials** → **OAuth Client ID**.
   * Choose **Desktop App**.
   * Download the file and rename it to `credentials.json`.
5. Place `credentials.json` in the **root directory** of the project.

### 📁 Required Files and Folders

* `credentials.json`
  → Contains the client ID and secret to access the Google Calendar API.

* `token.json`
  → Auto-generated after the first successful login and stores your access token.
  **Do not delete this file** unless you want to re-authenticate.

* `.env` *(Optional)*
  If you wish to manage environment-specific settings (e.g., default reminder time), you can use an `.env` file.

#### Example `.env`:

```env
DEFAULT_REMINDER_MINUTES=10
USE_DESKTOP_NOTIFICATION=true
```

 

## ▶️ Usage

```bash
python ai_voice_meeting_scheduler.py
```

Then speak:

> "Schedule a meeting with Alex on 10th August at 3 PM"

The app will:

* Extract meeting details from your voice
* Schedule it in Google Calendar
* Ask if you'd like a reminder
* Show notification before the meeting

 

## 🛠️ Technologies Used

* **Programming Language**: Python
* **Voice Recognition**: SpeechRecognition, PyAudio
* **Text-to-Speech**: pyttsx3
* **Date Parsing & NLP**: Dateparser, NLTK
* **Calendar Integration**: Google Calendar API
* **Desktop Notifications**: Plyer, Win10Toast / Notify2
* **Authentication & Tokens**: Google OAuth2 (`credentials.json`, `token.json`)
* **Scheduler / Timing**: `datetime`, `threading`, `time`
* **Environment Management**: python-dotenv

 

## 🛡️ Permissions

* Microphone Access (for speech input)
* Internet Access (for Google API)
* Google Account Authentication

 

## 🔮 Future Scope

* Add support for recurring and group meetings.
* Integrate with other platforms like Outlook, Zoom, or Microsoft Teams.
* Enable smart conflict detection and time suggestions.
* Build a mobile or web-based version for cross-platform use.
* Add multilingual voice command support.


 

## 📫 Contact

Developed by [Arpit Padmani](https://github.com/Arpit-Padmani)
Feel free to open issues or contribute via pull requests.

 
⭐ **Star this repo** if you found it useful!
