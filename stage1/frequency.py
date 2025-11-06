with open('cipher.txt', 'r') as file:
    data = file.read().rstrip()

# Split the content by spaces and convert to integers
integer_parts = list(map(int, data.split()))

# Now you can use the integer_parts list as needed
print(integer_parts)

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
result = result.replace('Q', 'p')
result = result.replace('C', 'i')
result = result.replace('U', 'c')
result = result.replace('H', 'o')
result = result.replace('I', 't')
result = result.replace('E', 'f')
result = result.replace('N', 'e')
result = result.replace('S', 'h')
result = result.replace('G', 'm')
result = result.replace('K', 'n')
result = result.replace('B', 'u')
result = result.replace('F', 'r')
result = result.replace('P', 'x')
result = result.replace('T', 's')
result = result.replace('Z', 'v')
result = result.replace('M', 'a')
result = result.replace('X', 'l')
result = result.replace('W', 'w')
result = result.replace('J', 'b')
result = result.replace('A', 'd')
result = result.replace('D', 'g')
result = result.replace('R', 'y')

# i = 0
# for key in inorder:
#     print(key[0], letters[i])
#     result = result.replace(key[0], letters[i])
#     print("--------------------------------------------")
#     print(i)
#     print(result)
#     i+=1

print(result)