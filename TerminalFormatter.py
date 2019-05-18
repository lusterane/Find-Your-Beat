'''
Toby Chow
TerminalFormatter.py

Finds the number of columns
'''
import shutil


class TermForm:
    columns = -1

    def __init__(self):
        self.columns = shutil.get_terminal_size().columns