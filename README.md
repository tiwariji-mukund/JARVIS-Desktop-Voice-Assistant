# JARVIS-Desktop-Voice-Assistant
This was my attempt to make a voice assistant similar to JARVIS (in iron man movie)<br><br>
Let's be honest, it's not as intelligent as in the movie, but it can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.<br>

## Built With
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height=50 />

## Features
It can do a lot of cool things, some of them being:<br>
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
<li> Tells top headlines (via Times of India)</li>
<li> Plays music</li>
<li> Send email (with subject and content)</li>
<li> Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)</li>
<li> Answer any generic question (via Wolframalpha)</li>
<li> Take important note in notepad</li>
<li> Tells a random joke</li>
<li> Tells your IP address</li>
<li> Can switch the window</li>
<li> Can take screenshot and save it with custom filename</li>
<li> Can hide all files in a folder and also make them visible again</li>
<li> Has a cool Graphical User Interface</li>
</ul>

## API Keys

To run this program you will require a bunch of API keys. Register your API key by clicking the following links<nr><br>
<ul>
  <li> <a href="#">OpenWeatherMap API</a></li>
  <li> <a href="#">Wolframalpha</a></li>
  <li> <a href="#">Google Calendar API</a></li>
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
      ├── driver
      ├── Jarvis              # Main folder for features 
      │   ├── config          # Contains all secret API Keys
      │   ├── features        # All functionalities of JARVIS 
      │   └── utils           # GUI images
      ├── __init__.py         # Definition of feature's functions
      ├── gui.ui              # GUI file (in .ui format)
      ├── main.py             # main driver program of Jarvis
      ├── requirements.txt    # all dependencies of the program
   
  
## Future Improvements
  <ul>
    <li> Generalized conversations can be made possible by incorporating Natural Language Processing</li>
    <li> GUI can be made more nicer to look at and functional</li>
    <li> More functionalities can be added</li>
  </ul>
