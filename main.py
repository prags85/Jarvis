import os
import eel

eel.init("www")

# Full path to Chrome (change if your Chrome is not in default location)
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# URL to launch in app mode
url = "http://localhost:8000/index.html"

# Launch Chrome in app mode
os.system(f'"{chrome_path}" --app="{url}"')

# Start the Eel server
eel.start('index.html', mode=None, host='localhost', block=True)
