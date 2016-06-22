import time
import pyperclip

clipboard_old = ""

while True:

    clipboard = pyperclip.paste()

    if (clipboard != clipboard_old):
        print "New ID!"
        clipboard_old = clipboard

    time.sleep(0.5)
    
headers={'Content-Type':'application/json','Accept':'application/vnd.api+json; version=1'}