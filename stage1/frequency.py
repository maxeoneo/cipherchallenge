with open('cipher.txt', 'r') as file:
    data = file.read().rstrip()

frequency_analysis = { "A" : 0,  "B" : 0,  "C" : 0,  "D" : 0,  "E" : 0,                      "F" : 0,  "G" : 0,
    "H" : 0,  "I" : 0,  "J" : 0,  "K" : 0,  "L" : 0,  "M" : 0,  "N" : 0,  "O" :   0,
    "P" : 0,  "Q" : 0,  "R" : 0,  "S" : 0,  "T" : 0,  "U" : 0,  "V" : 0,  "W" : 0,
    "X" : 0,  "Y" : 0,  "Z" : 0 }

frequency_analysis2 = { "A" : 0,  "B" : 0,  "C" : 0,  "D" : 0,  "E" : 0,                      "F" : 0,  "G" : 0,
"H" : 0,  "I" : 0,  "J" : 0,  "K" : 0,  "L" : 0,  "M" : 0,  "N" : 0,  "O" :   0,
"P" : 0,  "Q" : 0,  "R" : 0,  "S" : 0,  "T" : 0,  "U" : 0,  "V" : 0,  "W" : 0,
"X" : 0,  "Y" : 0,  "Z" : 0 }

letters = 'eariotnslcudpmhgbfywkvxzjq'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in data:
    if letter.isalpha():
        frequency_analysis[letter.upper()] += 1

def get_num (frequency_analysis):
        return frequency_analysis[1]


unsorted_items = frequency_analysis.items()
sorted_items = sorted(unsorted_items, key = get_num)

descending = reversed(sorted_items)
descending = list(descending)

inorder = list()
for char in descending:
    inorder.append(char)

for key in inorder:
    if key[1] > 0:
        print (key)

result = data
result = result.replace('X', 'e')
result = result.replace('J', 't')
result = result.replace('P', 'h')
result = result.replace('T', 'n')
result = result.replace('B', 'i')
result = result.replace('C', 'o')
result = result.replace('I', 'f')
result = result.replace('V', 'r')
result = result.replace('M', 'a')
result = result.replace('W', 'g')
result = result.replace('N', 'd')
result = result.replace('R', 's')
result = result.replace('D', 'v')
result = result.replace('U', 'u')
result = result.replace('L', 'm')
result = result.replace('Y', 'w')
result = result.replace('A', 'c')
result = result.replace('G', 'l')
result = result.replace('Q', 'p')
result = result.replace('H', 'k')
result = result.replace('F', 'b')
result = result.replace('E', 'y')
result = result.replace('K', 'q')
result = result.replace('Z', 'x')
result = result.replace('S', 'j')
result = result.replace('O', 'z')

# i = 0
# for key in inorder:
#     print(key[0], letters[i])
#     result = result.replace(key[0], letters[i])
#     print("--------------------------------------------")
#     print(i)
#     print(result)
#     i+=1

print(result)