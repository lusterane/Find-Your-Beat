'''
Toby Chow
TerminalFormatter.py

Formats outputs in terminal to support better user experience
'''
import shutil

class TermForm():
    columns = -1

    def __init__(self):
        self.columns = shutil.get_terminal_size().columns