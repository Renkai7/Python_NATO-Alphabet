import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.set_index("letter")["code"].to_dict()
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word: ").upper()
alpha_list = [phonetic_dict[letter] for letter in word]

print(alpha_list)
