import pandas as pd

def generate_phonetic_code(word):
    """
    Generate a phonetic code for a given word.
    """
    try:
        result = [phonetic_dict[letter] for letter in word.upper()] # convert a word to a list of the fonetic code
    except KeyError:
        print("Invalid word")
    else:
        print(f"NATO phonetic code: {word} {result}")

df = pd.read_csv("nato_phonetic_alphabet.csv") # read a csv file
phonetic_dict = {row.letter: row.code for (_, row) in df.iterrows()} # create a dictionary from csv

word = input("Word: ") # get a word from a user
generate_phonetic_code(word) # generate a phonetic code