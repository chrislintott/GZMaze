import time
import pyperclip

clipboard_old = ""

while True:

    clipboard = pyperclip.paste()

    if (clipboard != clipboard_old):
        print "New ID!"
        clipboard_old = clipboard

    time.sleep(0.5)