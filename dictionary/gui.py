import tkinter as tk
import pyperclip

class GUI:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.root = tk.Tk()

        self.root.title("Speaking Dictionary with Text To Speech")
        self.root.geometry("1000x500")
        bold_font = ('Courier New', 16, 'bold')

        self.label = tk.Label(self.root, text="Enter the word you want to search:", font=bold_font)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.textbox = tk.Entry(self.root, font=('Courier New', 14), width=30)
        self.textbox.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search", font=('Courier New', 12), command=self.search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

        self.meaning_label = tk.Label(self.root, text="", font=('Courier New', 12), wraplength=500, justify=tk.LEFT)
        self.meaning_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W)

        self.copy_button = tk.Button(self.root, text="Copy", font=('Courier New', 12), command=self.copy_meaning)
        self.copy_button.grid(row=2, column=0, padx=10, pady=10)


        self.word_of_day_button = tk.Button(self.root, text="Word of the Day", font=('Courier New', 12), command=self.word_of_the_day)
        self.word_of_day_button.grid(row=2, column=2, padx=10, pady=10)

        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def search(self):
        """Search for the meaning of the word entered in the textbox."""
        word = self.textbox.get()
        meaning = self.dictionary.translate(word)
        if isinstance(meaning, list):
            meaning = "\n".join([f"• {item}" for item in meaning])
        self.meaning_label.config(text=meaning)

    def copy_meaning(self):
        """Copy the meaning displayed in the label to the clipboard."""
        meaning = self.meaning_label.cget("text")
        pyperclip.copy(meaning)

    def word_of_the_day(self):
        """Display a random word of the day."""
        random_word, meaning = self.dictionary.word_of_the_day()
        self.textbox.delete(0, tk.END)
        self.textbox.insert(0, random_word)
        if isinstance(meaning, list):
            meaning = "\n".join([f"• {item}" for item in meaning])
        self.meaning_label.config(text=meaning)

    def launchGUI(self):
        """Launch the GUI."""
        self.root.mainloop()
