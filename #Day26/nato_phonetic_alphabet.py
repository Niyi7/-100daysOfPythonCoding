import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_name = (input("Whats is you name?: ")).upper()
phonetic_words = [data_dict[letter] for letter in user_name]
print(phonetic_words)
# for letters in user_name:
#     phonetic_words.append(data_dict[letters])

# C:/Users/Front Desk/Documents/#100daysOfPythonCoding/#Day26
