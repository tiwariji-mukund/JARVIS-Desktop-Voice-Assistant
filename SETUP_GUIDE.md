# JARVIS Desktop Voice Assistant - Quick Setup Guide

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Windows 10/11
- Python 3.8.5+
- Microphone and speakers
- Internet connection

### Step 1: Download and Setup
```bash
# Clone the repository
git clone https://github.com/your-username/JARVIS-Desktop-Voice-Assistant.git
cd JARVIS-Desktop-Voice-Assistant

# Create virtual environment
python -m venv jarvis-env
jarvis-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Install PyAudio (Windows)
```bash
# Download PyAudio wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Choose the file matching your Python version and architecture
pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl  # Example filename
```

### Step 3: Get API Keys (Optional but Recommended)
1. **News API**: Register at [newsapi.org](https://newsapi.org/) - Free tier available
2. **Wolframalpha**: Register at [wolframalpha.com](https://www.wolframalpha.com/) - Free tier available
3. **OpenWeatherMap**: Register at [openweathermap.org](https://openweathermap.org/api) - Free tier available

### Step 4: Configure (Optional)
```bash
# Copy configuration template
copy config_template.py config.py

# Edit config.py with your API keys and paths
notepad config.py
```

### Step 5: Create Required Directories
```bash
mkdir Downloads
mkdir screenshots
```

### Step 6: Run JARVIS
```bash
python jarvis_main.py
```

## 🎯 First Time Usage

1. **Start**: Run `python jarvis_main.py`
2. **Watch**: Intro animation will play
3. **Activate**: Say "wake up" when the animation ends
4. **Test**: Try "what time is it?" or "hello"
5. **Explore**: Use commands from the voice reference below

## 🗣️ Essential Voice Commands

### Basic Commands
- `"wake up"` - Activate JARVIS
- `"time"` - Get current time
- `"date"` - Get current date
- `"hello"` - Basic greeting
- `"go to sleep"` - Deactivate (still listens for wake word)
- `"goodbye"` - Complete shutdown

### Quick Actions
- `"open google chrome"` - Launch Chrome
- `"google python tutorials"` - Search Google
- `"youtube funny videos"` - Search YouTube
- `"wikipedia artificial intelligence"` - Search Wikipedia
- `"calculate 25 plus 67"` - Math calculation
- `"screenshot"` - Take screenshot
- `"joke"` - Tell a joke

## 🔧 Troubleshooting

### Common Issues & Quick Fixes

#### "JARVIS not responding to voice"
- Check microphone permissions in Windows settings
- Ensure microphone is default recording device
- Test with: `python -c "import speech_recognition as sr; r=sr.Recognizer(); print('Say something:'); print(r.recognize_google(r.listen(sr.Microphone())))"`

#### "PyAudio installation failed"
- Download wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install using pip with the downloaded wheel file
- Alternative: `conda install pyaudio` (if using Anaconda)

#### "Application not opening"
- Check if the application is installed
- Update application paths in `DictApp.py`
- Run as administrator for system applications

#### "News/Weather not working"
- Add API keys to configuration
- Check internet connection
- Verify API key validity

### Performance Tips
- Close unnecessary applications while running JARVIS
- Use wired microphone for better recognition
- Speak clearly and at moderate pace
- Ensure stable internet connection

## 📋 Feature Status

### ✅ Works Out of the Box
- Basic conversation
- Time and date
- Application launching
- Volume control
- Screenshot capture
- Simple Google search
- YouTube search
- Wikipedia search
- Mathematical calculations (basic)
- Rock Paper Scissors game
- Jokes

### 🔑 Requires API Keys
- Detailed news reading
- Advanced mathematical queries
- Weather information

### ⚙️ Requires Configuration
- WhatsApp automation (phone numbers)
- Advanced features with custom file paths

## 🆘 Need Help?

1. **Check Full Documentation**: Read `DOCUMENTATION.md` for complete details
2. **Review Error Messages**: Most issues are clearly indicated in console output
3. **Test Components**: Run individual modules to isolate problems
4. **Check Dependencies**: Ensure all packages are properly installed
5. **Verify Configuration**: Double-check API keys and file paths

## 🎉 You're Ready!

Once setup is complete, you can:
- Control your computer with voice commands
- Get information without touching keyboard
- Automate daily tasks
- Have fun with interactive features

Say **"wake up"** and start exploring JARVIS!

---

**Next Steps**: Read the full `DOCUMENTATION.md` for advanced features and detailed configuration options.