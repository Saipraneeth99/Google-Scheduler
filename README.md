
# Google Scheduler

Google Scheduler allows you to manage Google Calendar events using Python. You can add, list, and delete events from your Google Calendar.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Saipraneeth99/Google-Scheduler.git
   cd Google-Scheduler
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Google API Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing project.

3. Enable the Google Calendar API for your project:
   - Go to the [Google Calendar API page](https://console.developers.google.com/apis/library/calendar.googleapis.com).
   - Click "Enable".

4. Create OAuth 2.0 credentials:
   - Go to the [Credentials page](https://console.developers.google.com/apis/credentials).
   - Click "Create credentials" and select "OAuth 2.0 Client IDs".
   - Configure the consent screen if prompted.
   - Set the application type to "Desktop app" and complete the form.
   - Download the `credentials.json` file and place it in the root directory of your project.

## Running the Script

1. Ensure your `credentials.json` file is in the root directory.

2. Run the script:
   ```bash
   python3 main.py
   ```

## Project Structure

```
.
├── addEventsToLibrary.py
├── backupCalendar.py
├── decorators.py
├── googleCalendarApi.py
├── googleCalendarServiceImpl.py
├── manageEventsInCalendar.py
├── main.py
├── updated_weekly_schedule.csv
├── requirements.txt
├── credentials.json
├── token.pickle
├── .gitignore
└── README.md
```

## Logging

The script logs its operations to `calendar_log.log`. You can check this file for detailed execution logs.



### Additional Steps to Set Up the Google Console

1. **Go to the Google Cloud Console**: [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a New Project**:
   - Click on the project drop-down on the top left of the screen.
   - Click "New Project".
   - Enter a project name and click "Create".

3. **Enable the Google Calendar API**:
   - Go to the [Google Calendar API page](https://console.developers.google.com/apis/library/calendar.googleapis.com).
   - Select your project from the drop-down menu.
   - Click "Enable".

4. **Create OAuth 2.0 Credentials**:
   - Go to the [Credentials page](https://console.developers.google.com/apis/credentials).
   - Click "Create Credentials" and select "OAuth 2.0 Client IDs".
   - Configure the OAuth consent screen if prompted:
     - Select "External" and click "Create".
     - Enter the required information and save.
   - Set the application type to "Desktop app" and name your OAuth client.
   - Click "Create" and then download the `credentials.json` file.
   - Place the `credentials.json` file in the root directory of your project.
