# JARVIS Configuration Template
# Copy this file to config.py and update with your API keys and paths

# =============================================================================
# API KEYS - Register at the respective websites to get these keys
# =============================================================================

# News API - Get from: https://newsapi.org/
NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"

# Wolframalpha API - Get from: https://www.wolframalpha.com/
WOLFRAM_API_KEY = "YOUR_WOLFRAM_API_KEY_HERE"

# OpenWeatherMap API - Get from: https://openweathermap.org/api
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY_HERE"

# =============================================================================
# FILE PATHS - Update these paths according to your system
# =============================================================================

# Base project directory (update this to your project location)
BASE_DIR = r"C:\Users\YourUsername\Path\To\JARVIS-Desktop-Voice-Assistant"

# Audio files
ALARM_SOUND = rf"{BASE_DIR}\Downloads\music.mp3"
NOTIFICATION_SOUND = rf"{BASE_DIR}\Downloads\notification.mp3"
INTRO_SOUND = rf"{BASE_DIR}\Downloads\jarvis_Sound.mp3"

# Visual files
INTRO_GIF = rf"{BASE_DIR}\Downloads\jarvis.gif"
SCREENSHOT_PATH = rf"{BASE_DIR}\screenshots"

# Data files
TASKS_FILE = rf"{BASE_DIR}\tasks.txt"
REMEMBER_FILE = rf"{BASE_DIR}\remember.txt"
PASSWORD_FILE = rf"{BASE_DIR}\password.txt"

# =============================================================================
# WHATSAPP CONFIGURATION
# =============================================================================

# WhatsApp contacts (add phone numbers with country code)
WHATSAPP_CONTACTS = {
    "contact1": "+1234567890",  # Replace with actual numbers
    "contact2": "+0987654321",
    # Add more contacts as needed
}

# =============================================================================
# VOICE SETTINGS
# =============================================================================

# Speech recognition settings
SPEECH_ENERGY_THRESHOLD = 300
SPEECH_PAUSE_THRESHOLD = 1
SPEECH_TIMEOUT = 4

# Text-to-speech settings
TTS_RATE = 170  # Words per minute
TTS_VOICE_INDEX = 0  # 0 for male, 1 for female (system dependent)

# =============================================================================
# APPLICATION PATHS
# =============================================================================

# Update these if your applications are installed in different locations
APP_PATHS = {
    "command prompt": "cmd",
    "word": "winword",
    "excel": "EXCEL",
    "google chrome": "chrome",
    "pycharm": "pycharm64",
    "edge": "msedge",
    "browser": "firefox",
    "powerpoint": "POWERPNT",
    "powershell": "powershell",
    "one note": "onenote",
    "media player": "VLC",
    "sublime text": r"C:\Program Files\Sublime Text\sublime_text"
}

# =============================================================================
# USAGE INSTRUCTIONS
# =============================================================================

"""
1. Copy this file to config.py
2. Update all the API keys with your actual keys
3. Update file paths to match your system
4. Add your WhatsApp contacts
5. Adjust voice and speech settings as needed
6. Update application paths if they differ from defaults

To get API keys:
- News API: Register at https://newsapi.org/
- Wolframalpha: Register at https://www.wolframalpha.com/
- Weather API: Register at https://openweathermap.org/api

Make sure to create the following directories:
- Downloads/ (for audio and visual files)
- screenshots/ (for screenshot storage)
"""