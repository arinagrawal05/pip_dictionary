# Speaking Dictionary with Text To Speech

This is a Python package that provides a speaking dictionary application using text-to-speech functionality. Users can search for words, hear their meanings, and manage a history of searched words.

## Features

- Search for words and get their meanings.
- Text-to-speech functionality to pronounce the meanings.
- Copy the meaning of a word to the clipboard.
- "Word of the Day" feature to discover new words.
- History of searched words.

# Dictionary📖🧾

`dictionary` is a simple yet powerful Python package designed to retrieve word meanings and offer an intuitive GUI for users to explore word definitions. It helps developers easily integrate word lookups into their applications.

## 🌟 Features

- **Retrieve Word Definitions**: Get definitions of words directly through code.
- **Word of the Day**: Access the word of the day, updated daily.
- **Graphical User Interface (GUI)**: Interact with the dictionary using an easy-to-use graphical interface.
- **Simple Integration**: Easily embed the dictionary functionality in any Python project.

## 🚀 Installation

To install the package, use:

```bash
pip install dictionary
```

## Usage/Examples

```python
from dictionary import Dictionary 

book = Dictionary() 

word_to_translate = "example"
meaning = book.word_of_the_day
print(f"The meaning of '{word_to_translate}' is: {meaning}")

print("Launching GUI...")
book.launchGUI()

```

## Output

The meaning of 'example' is: a representative form or pattern.
Launching GUI...

## Installation

To install this package, clone the repository and navigate to the directory:

```bash
# git clone https://github.com/yourusername/speaking_dictionary.git
# cd speaking_dictionary
