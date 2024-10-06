from dictionary import Dictionary

def main():
    dictionary = Dictionary() 
    meaning = dictionary.word_of_the_day()
    print(f"The meaning is: {meaning}")
 
    dictionary.launchGUI()   

if __name__ == "__main__":
    main()
