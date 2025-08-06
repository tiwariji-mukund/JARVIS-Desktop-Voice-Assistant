# JARVIS Desktop Voice Assistant - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation and Setup](#installation-and-setup)
5. [Configuration](#configuration)
6. [Usage Guide](#usage-guide)
7. [Voice Commands Reference](#voice-commands-reference)
8. [File Structure](#file-structure)
9. [API Integration](#api-integration)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [Security](#security)
13. [License](#license)

## Overview

JARVIS (Just A Rather Very Intelligent System) is a desktop voice assistant inspired by the AI assistant from the Iron Man movies. Built with Python, it provides voice-controlled automation for common computer tasks, web browsing, entertainment, and productivity features.

### Key Capabilities
- Voice recognition and text-to-speech
- Application and website management
- Web searching and information retrieval
- Media playback control
- Weather and news updates
- Mathematical calculations
- WhatsApp automation
- Gaming features
- System monitoring

## Features

### 🎤 Voice Interaction
- **Wake Word Activation**: Responds to "wake up" command
- **Natural Language Processing**: Understands conversational commands
- **Text-to-Speech**: Provides vocal responses
- **Multi-language Support**: English (Indian) voice recognition

### 🖥️ System Control
- **Application Management**: Open/close applications with voice commands
- **Website Navigation**: Launch websites directly
- **System Information**: Battery status, RAM usage, CPU monitoring
- **Screenshot Capture**: Voice-activated screenshots
- **Volume Control**: Adjust system volume through voice

### 🌐 Web Integration
- **Google Search**: Voice-activated web searches
- **YouTube Control**: Play videos, control playback
- **Wikipedia Lookup**: Get information from Wikipedia
- **Weather Updates**: Current weather and temperature
- **News Reading**: Latest news from various categories

### 📱 Communication
- **WhatsApp Automation**: Send messages via voice commands
- **Reminder System**: Set and recall personal reminders
- **Calendar Integration**: Google Calendar event notifications

### 🎯 Productivity
- **Mathematical Calculator**: Solve complex expressions
- **Task Scheduling**: Manage daily tasks and schedules
- **Note Taking**: Voice-to-text note creation
- **Alarm System**: Set voice-activated alarms

### 🎮 Entertainment
- **Rock Paper Scissors Game**: Interactive voice-controlled game
- **Joke Generator**: Random joke delivery
- **Music Control**: Media playback management
- **Cricket Scores**: Live cricket match updates

## System Requirements

### Hardware Requirements
- **Microphone**: For voice input
- **Speakers/Headphones**: For audio output
- **Internet Connection**: For web-based features
- **Minimum RAM**: 4GB recommended
- **Storage**: 500MB free space

### Software Requirements
- **Operating System**: Windows 10/11 (primary support)
- **Python**: Version 3.8.5 or higher
- **Package Manager**: pip (Python package installer)

### Supported Applications
- Google Chrome
- Microsoft Edge
- Firefox
- Microsoft Word
- Microsoft Excel
- PowerPoint
- PyCharm
- VLC Media Player
- Sublime Text
- Windows Command Prompt
- PowerShell

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/JARVIS-Desktop-Voice-Assistant.git
cd JARVIS-Desktop-Voice-Assistant
```

### Step 2: Create Python Environment
```bash
# Using Anaconda
conda create -n jarvis python==3.8.5
conda activate jarvis

# Using venv
python -m venv jarvis-env
source jarvis-env/bin/activate  # On Windows: jarvis-env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install from installer.py
python installer.py

# Or install manually
pip install speechrecognition requests plyer pywhatkit pyaudio wikipedia beautifulsoup4 playsound python-decouple pyautogui pynput wolframalpha pygame vosk googletrans gtts pykeyboard pyjokes pyttsx3 Pillow tkinter
```

### Step 4: Install PyAudio
PyAudio requires special installation on Windows:
1. Download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
2. Install using: `pip install PyAudio-x.x.x-cpxx-cpxxm-win_amd64.whl`

### Step 5: Configure API Keys
Create necessary API accounts and configure keys (see Configuration section).

### Step 6: Run the Application
```bash
python jarvis_main.py
```

## Configuration

### Required API Keys

#### 1. OpenWeatherMap API
- **Purpose**: Weather information
- **Registration**: [OpenWeatherMap](https://openweathermap.org/api)
- **Configuration**: Update weather API calls in `jarvis_main.py`

#### 2. News API
- **Purpose**: Latest news updates
- **Registration**: [News API](https://newsapi.org/)
- **Configuration**: Update API key in `newsRead.py` line 40-54

#### 3. Wolframalpha API
- **Purpose**: Mathematical calculations and general queries
- **Registration**: [Wolframalpha](https://www.wolframalpha.com/)
- **Configuration**: Update API key in `calculate.py` line 20

### File Path Configuration
Update the following hardcoded paths in the source files:

#### jarvis_main.py
- Line 196: Update alarm sound path
- Line 287, 295, 304, 310: Update tasks.txt path
- Line 314, 342: Update notification sound path
- Line 356: Update screenshot save path

#### INTRO.py
- Line 15: Update GIF file path
- Line 19: Update intro sound path

#### WhatsApp.py
- Line 56, 62: Update phone numbers for WhatsApp automation

### Voice Configuration
Modify voice settings in any file:
```python
engine.setProperty("rate", 170)  # Speech rate
engine.setProperty("voice", voices[0].id)  # Voice selection (0 for male, 1 for female)
```

## Usage Guide

### Starting JARVIS
1. Run `python jarvis_main.py`
2. GUI window will appear with intro animation
3. Say "wake up" to activate JARVIS
4. Wait for "Listening..." prompt
5. Speak your command clearly

### Basic Interaction Pattern
1. **Activation**: "Wake up"
2. **Command**: Speak your request
3. **Response**: JARVIS will execute and respond
4. **Sleep**: "Go to sleep" (JARVIS continues listening for wake word)
5. **Shutdown**: "Goodbye" (completely exit)

### Example Conversations
```
User: "Wake up"
JARVIS: "Good morning, sir. I am JARVIS, your personal AI assistant. How may I help you?"

User: "What time is it?"
JARVIS: "Sir, the time is 10:30"

User: "Open Google Chrome"
JARVIS: "Opening Google Chrome"

User: "Search Google for Python tutorials"
JARVIS: "Working on that, sir. This is what I found on Google..."
```

## Voice Commands Reference

### System Control
| Command | Function |
|---------|----------|
| "wake up" | Activate JARVIS |
| "go to sleep" | Deactivate (still listens for wake word) |
| "goodbye" | Completely shut down |
| "time" | Get current time |
| "date" | Get current date |
| "temperature" | Get current temperature |
| "weather" | Get weather information |
| "screenshot" | Take a screenshot |
| "shutdown" | System shutdown |

### Application Management
| Command | Function |
|---------|----------|
| "open [application]" | Launch application |
| "close [application]" | Close application |
| "open [website.com]" | Open website |

**Supported Applications:**
- command prompt, cmd
- word, winword
- excel
- google chrome, chrome
- pycharm
- edge, msedge
- browser, firefox
- powerpoint
- powershell
- one note, onenote
- media player, vlc
- sublime text

### Web & Search
| Command | Function |
|---------|----------|
| "google [query]" | Search Google |
| "youtube [query]" | Search/play YouTube |
| "wikipedia [query]" | Search Wikipedia |

### Media Control
| Command | Function |
|---------|----------|
| "pause" | Pause video |
| "play" | Play/resume video |
| "mute" | Mute audio |
| "unmute" | Unmute audio |
| "volume up" | Increase volume |
| "volume down" | Decrease volume |
| "full screen" | Toggle fullscreen |
| "mini player" | Mini player mode |
| "theatre mode" | Theatre mode |
| "subtitle" | Toggle subtitles |
| "next" | Next video |
| "previous" | Previous video |

### Productivity
| Command | Function |
|---------|----------|
| "calculate [expression]" | Mathematical calculation |
| "remember that [note]" | Save a reminder |
| "what do you remember" | Recall saved reminder |
| "alarm" | Set an alarm |
| "schedule my day" | Add tasks to schedule |
| "show my schedule" | Display scheduled tasks |

### Communication
| Command | Function |
|---------|----------|
| "whatsapp" / "whats app" | Send WhatsApp message |

### Information & News
| Command | Function |
|---------|----------|
| "news" | Get latest news |
| "score" | Get cricket scores |

### Entertainment
| Command | Function |
|---------|----------|
| "game" | Play Rock Paper Scissors |
| "joke" | Tell a random joke |
| "take a picture" | Open camera app |

### Conversation
| Command | Response |
|---------|----------|
| "hello" | "Hello sir, how are you?" |
| "how are you" | "Perfect, sir" |
| "i am fine" | "That's great, sir" |
| "thank you" | "You are welcome, sir" |

## File Structure

```
JARVIS-Desktop-Voice-Assistant/
├── jarvis_main.py          # Main application driver
├── DictApp.py             # Application management functions
├── GreetUser.py           # Time-based greeting functions
├── INTRO.py               # GUI intro with animation
├── SearchNow.py           # Web search functions (Google, YouTube, Wikipedia)
├── WhatsApp.py            # WhatsApp automation
├── calculate.py           # Mathematical calculation functions
├── game.py                # Rock Paper Scissors game
├── installer.py           # Dependency installer
├── newsRead.py            # News reading functionality
├── keyboard.py            # Volume control functions
├── remember.txt           # Stores user reminders
├── tasks.txt              # Stores scheduled tasks
├── README.md              # Basic project information
├── SECURITY.md            # Security policy
├── ss.jpg                 # Screenshot sample
├── Downloads/             # Media files directory
│   ├── jarvis.gif         # Intro animation
│   ├── jarvis_Sound.mp3   # Intro sound
│   ├── music.mp3          # Alarm sound
│   └── notification.mp3   # Notification sound
└── Screenshot/            # Screenshots directory
```

### Core Modules Description

#### jarvis_main.py
- **Purpose**: Main application entry point
- **Functions**: Voice recognition loop, command processing, feature orchestration
- **Key Components**: Speech engine setup, main command loop, feature dispatch

#### DictApp.py
- **Purpose**: Application and website management
- **Functions**: `openAppWeb()`, `closeAppWeb()`
- **Features**: Application launching, tab management, website opening

#### SearchNow.py
- **Purpose**: Web search capabilities
- **Functions**: `searchGoogle()`, `searchYouTube()`, `searchWikipedia()`
- **Integration**: pywhatkit, webbrowser, wikipedia libraries

#### WhatsApp.py
- **Purpose**: WhatsApp message automation
- **Functions**: `send_message()`
- **Features**: Scheduled message sending, contact management

#### calculate.py
- **Purpose**: Mathematical computation
- **Functions**: `Calculator()`, `WolfRamAlpha()`
- **Features**: Expression parsing, Wolframalpha integration

#### newsRead.py
- **Purpose**: News aggregation and reading
- **Functions**: `latestNews()`
- **Categories**: Politics, business, sports, technology, entertainment

#### game.py
- **Purpose**: Interactive gaming
- **Functions**: `game_play()`
- **Game**: Rock Paper Scissors with score tracking

## API Integration

### Speech Recognition
- **Library**: SpeechRecognition
- **Engine**: Google Speech Recognition
- **Language**: English (Indian)
- **Configuration**: Adjustable threshold and timeout settings

### Text-to-Speech
- **Library**: pyttsx3
- **Engine**: SAPI5 (Windows)
- **Voice**: Configurable male/female voices
- **Rate**: Adjustable speech rate (default: 170-200 WPM)

### External APIs

#### News API Integration
```python
# Example API endpoints in newsRead.py
"top headlines": "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=YOUR_API_KEY"
```

#### Wolframalpha Integration
```python
# Mathematical query processing
apikey = "YOUR_WOLFRAM_API_KEY"
requester = wolframalpha.Client(apikey)
requested = requester.query(query)
```

#### Weather Data
- **Source**: Google Search scraping
- **Method**: BeautifulSoup HTML parsing
- **Data**: Temperature and weather conditions

## Troubleshooting

### Common Issues

#### 1. Microphone Not Working
**Symptoms**: JARVIS not responding to voice commands
**Solutions**:
- Check microphone permissions in Windows settings
- Verify microphone is set as default recording device
- Test microphone with other applications
- Adjust `r.energy_threshold` in voice recognition functions

#### 2. PyAudio Installation Error
**Symptoms**: Installation fails with compiler errors
**Solutions**:
- Use precompiled wheel files
- Install Microsoft Visual C++ Build Tools
- Use conda: `conda install pyaudio`

#### 3. Voice Recognition Accuracy Issues
**Symptoms**: Commands not recognized correctly
**Solutions**:
- Speak clearly and at moderate pace
- Reduce background noise
- Adjust `r.pause_threshold` and `r.energy_threshold`
- Check internet connection (Google Speech Recognition requires internet)

#### 4. Application Launch Failures
**Symptoms**: "Open [app]" commands don't work
**Solutions**:
- Verify application is installed
- Update application paths in `DictApp.py`
- Run as administrator for system applications
- Check application names in `dictApp` dictionary

#### 5. API Key Errors
**Symptoms**: Features like news, weather, or calculations not working
**Solutions**:
- Verify API keys are valid and active
- Check API rate limits
- Update hardcoded API keys in respective files
- Ensure internet connectivity

### Performance Optimization

#### Memory Usage
- Close unnecessary applications while running JARVIS
- Restart JARVIS periodically for long sessions
- Monitor system resources

#### Response Time
- Use SSD for faster file access
- Ensure stable internet connection for API calls
- Close resource-intensive background applications

### Debugging Tips

#### Enable Verbose Logging
Add debugging prints to track execution:
```python
print(f"Command received: {query}")
print(f"Processing: {function_name}")
```

#### Test Individual Modules
Run modules independently:
```bash
python SearchNow.py
python calculate.py
python newsRead.py
```

#### Voice Recognition Testing
Test speech recognition separately:
```python
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    print(r.recognize_google(audio))
```

## Contributing

### Development Setup
1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Update documentation for new features
5. Submit pull request with detailed description

### Code Standards
- Follow PEP 8 Python style guidelines
- Add docstrings for all functions
- Include error handling for external API calls
- Test voice commands thoroughly
- Update this documentation for new features

### Adding New Features
1. Create new module file for complex features
2. Import and integrate in `jarvis_main.py`
3. Add voice command recognition
4. Update command reference documentation
5. Test with various speech patterns

### Reporting Issues
- Use GitHub Issues for bug reports
- Include system information and Python version
- Provide steps to reproduce the issue
- Include error messages and logs

## Security

### Data Privacy
- Voice data is processed locally when possible
- Google Speech Recognition sends audio to Google servers
- No voice data is stored permanently
- User reminders and tasks are stored locally in text files

### API Key Security
- Store API keys in environment variables
- Never commit API keys to version control
- Rotate API keys regularly
- Use API key restrictions when available

### System Access
- JARVIS can execute system commands
- Review application paths before running
- Run with minimal necessary permissions
- Be cautious with commands that modify system settings

### Network Security
- All external API calls use HTTPS
- Validate API responses before processing
- Implement rate limiting for API calls
- Monitor network traffic for debugging

## Future Enhancements

### Planned Features
- Natural Language Processing improvements
- Enhanced GUI with modern design
- Additional API integrations
- Mobile companion app
- Voice training for better recognition
- Multi-user support
- Cloud synchronization for settings
- Smart home device integration

### Technical Improvements
- Modular plugin architecture
- Configuration file system
- Comprehensive error logging
- Unit test coverage
- Performance monitoring
- Docker containerization
- Cross-platform support

## License

This project is open source. Please refer to the LICENSE file for detailed licensing information.

## Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review existing issues and solutions
- Contribute to the project documentation

---

**Note**: This documentation covers the current state of the JARVIS Desktop Voice Assistant. Features and functionality may be updated in future versions. Always refer to the latest documentation and release notes.