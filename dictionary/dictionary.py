import json
from difflib import get_close_matches
from .gui import GUI
import random
# import importlib.resources
# import pkg_resources
import importlib.resources as pkg_resources

class Dictionary:
    def __init__(self, data_file=None):
       if data_file is None:
            # Load the file using importlib.resources
        with pkg_resources.open_text(__package__, 'data.json') as file:
            self.data = json.load(file)
        """Initializes the Dictionary with the data file."""
        self.language = "en-US"
        self.data_file = data_file
        self.data = self.load_data()  # Load data upon initialization

    def load_data(self):
        """Load data from the JSON file."""
        with pkg_resources.open_text(__package__, 'data.json') as file:
            return json.load(file)
    def word_of_the_day(self):
        """Returns a random word and its meaning."""
        random_word = random.choice(list(self.data.keys()))
        meaning = self.data[random_word]
        return random_word, meaning
   

    def translate(self, word):
        """Translates a word to its meaning."""
        word = word.lower()
        if word in self.data:
            return self.data[word]
        elif word.title() in self.data:
            return self.data[word.title()]
        elif word.upper() in self.data:
            return self.data[word.upper()]
        elif len(get_close_matches(word, self.data.keys())) > 0:
            return get_close_matches(word, self.data.keys())[0]
        else:
            return "The word doesn't exist. Please double-check it."

    def launchGUI(self):
        """Launches the GUI for the dictionary."""
        gui = GUI(self)
        gui.launchGUI()  # Ensure this method is called to start the GUI
