# Run in visual env
from dictionary import Dictionary
 
book =Dictionary() 
word_to_translate = "example"
meaning = book.translate(word_to_translate)
print(f"The meaning of '{word_to_translate}' is: {meaning}")
print("Launching GUI...")
book.launchGUI()   
 