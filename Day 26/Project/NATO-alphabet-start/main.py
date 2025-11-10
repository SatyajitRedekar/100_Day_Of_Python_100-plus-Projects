#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

final_dict = {
    k.strip(): v.strip()
    for k, v in (line.strip().split(",") for line in open("nato_phonetic_alphabet.csv"))
}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

ans = input("Enter your name : ")
ans = ans.upper()
new_list = []
for char in ans:
    new_list.append(final_dict[char])
print(new_list)