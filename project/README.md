# Weather Notifier

An automated email notification system that sends weather updates.

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MyWeatherNotifier/project
   ```

2. **Create environment variables file**
   Create a `.env` file and add the following configuration:
   ```
   API_KEY=your_openweathermap_api_key_here
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_gmail_app_password_here
   ```
   
   - `API_KEY`: API key from [OpenWeatherMap](https://openweathermap.org/api)
   - `EMAIL_ADDRESS`: Email address for sending notifications
   - `EMAIL_PASSWORD`: Gmail app password (not your regular login password)

3. **Configure recipient emails**
   Modify the `recipients` array in `config.json` file to add recipient email addresses:
   ```json
   {
       "recipients": [
           "recipient1@example.com",
           "recipient2@example.com"
       ]
   }
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the program**
   ```bash
   python3 src/main.py
   ```

## Features

- Automatically fetches weather information for your current location every minute
- Sends weather updates via email to configured recipients
- Includes logging functionality with logs saved to `src/log/app.log`
