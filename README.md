# JARVIS-Desktop-Voice-Assistant
This was my attempt to make a voice assistant similar to JARVIS (in iron man movie)<br><br>
Let's be honest, it's not as intelligent as in the movie, but it can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.<br>

## Built With
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height=50 /> <img src="https://raw.githubusercontent.com/github/explore/d8574c7bce27faa27fb879bca56dfe351ee66efd/topics/pycharm/pycharm.png" height=50 />  <img src="https://avatars.githubusercontent.com/u/684879?s=280&v=4" height=50 />

## Features
It can do a lot of cool things, some of them being:
<ul>
  <li> Greet user</li>
  <li> Tell current time and date</li>
  <li> Launch applications/softwares</li>
  <li> Open any website</li>
  <li> Tells about weather of any city</li>
  <li> Open location of any place plus tells the distance between your place and queried place</li>
  <li> Tells your current system status (RAM Usage, battery health, CPU usage)</li>
  <li> Tells about your upcoming events (Google Calendar)</li>
  <li> Tells about any person (via Wikipedia)</li>
  <li> Can search anything on Google</li>
  <li> Can play any song on YouTube</li>
  <li> Tells top headlines</li>
  <li> WhatsApp automation</li>
  <li> Can handle browser on your voice command</li>
  <li> Plays music</li>
  <li> Can play game on the console which you build</li>
  <li> Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)</li>
  <li> Answer any generic question (via Wolframalpha)</li>
  <li> Take important note in notepad</li>
  <li> Tells a random joke</li>
  <li> Tells the latest news</li>
  <li> Tells the latest cricket score</li>
  <li> Can take screenshot and save it with custom filename</li>
  <li> Has a cool Graphical User Interface</li>
</ul>

## API Keys

To run this program you will require a bunch of API keys. Register your API key by clicking the following links<nr><br>
<ul>
  <li> <a href="https://openweathermap.org/api">OpenWeatherMap API</a></li>
  <li> <a href="https://www.wolframalpha.com/">Wolframalpha</a></li>
  <li> <a href="https://newsapi.org/">News API</a></li>
</ul>
  
## Installation
  
  <ul>
    <li> First clone the repo</li>
    <li> Make a config.py file and include the following in it:</li><br>
  
      email = "&lt;your_email&gt;"
      email_password = "&lt;your_email_password&gt;"
      wolframalpha_id = "&lt;your_wolframalpha_id&gt;
    
   <li>Copy the config.py file in Jarvis>config folder</li>
   <li>Make a new python environment If you are using anaconda just type <code>conda create -n jarvis python==3.8.5</code> in anaconda prompt</li>
   <li>To activate the environment <code>conda activate jarvis</code></li>
   <li>Navigate to the directory of your project</li>
   <li>Install all the requirements by just hitting <code>pip install -r requirements.txt</code></li>
    <li>Install PyAudio from wheel file by following instructions given <a href="#">here</a>.</li>
    <li>Run the program by <code>python main.py</code></li>
   <li>Enjoy !!!</li>
  </ul>
  
## Code Structure
      
      ├── __init__.py         # Definition of feature's functions
      ├── DictApp.py          # opening and closing of all applications and browser tabs function
      ├── GreetUser.py        # function to greet user according to time
      ├── INTRO.py            # beautiful GUI runs whenever we open the project
      ├── SearchNow.py        # all search functions for google, youtube and wikipedia
      ├── WhatsApp.py         # WhatsApp automation function
      ├── calculate.py        # function for solving arithmetic questions
      ├── game.py             # game file to play game on console
      ├── jarvis_main.py      # main driver program of Jarvis
      ├── installer.py        # all packages required
      ├── remember.txt        # all upcoming events
      ├── newsRead.py         # read news function
      ├── keyboard.py         # automate browser through voice command
   
  
## Future Improvements
  <ul>
    <li> Generalized conversations can be made possible by incorporating Natural Language Processing</li>
    <li> GUI can be made more nicer to look at and functional</li>
    <li> Security can be improved</li>
    <li> More functionalities can be added</li>
  </ul>
