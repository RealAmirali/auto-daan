# Auto Daan
Try to enter upcoming class in daan system  
This script helps you to enter the class in daan system automatically.  
Instead of refresh the page and try to enter the class, run this script and it's going to refresh and try for you every 15s.  

## Installation
Make sure you have the latest version of Chrome

### For windows users:
download latest version from [here](https://github.com/realamirali/auto-daan/releases).

### For linux and osx users:
You can follow this steps or wait until the build release.
- Install the latest version of Python
- Install the chromedriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Clone this repository: `git clone https://github.com/realamirali/auto-daan.git`
- Go to script directory and install the requirements: `pip install -r requirements.txt`
- Run the script: `python app.py`

## Usage
After the first run script asks you some config.  
- First you should select your branch of Islamic Azad University (Enter the number from list and if your branch isn't there contact me with Github Issues or Email)
- Second enter your user ID number
- And last enter your Password

These config gonna save in configuration file and for next times not gonna asks you these

## Configuration
The configuration file is in `{HOME DIRECTORY}/daan.json`
