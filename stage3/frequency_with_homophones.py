import pandas as pd

with open('cipher.txt', 'r') as file:
    cipher = file.read().rstrip().replace('\n', '')

def alphabet():
    usedChars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    usedChars.append('*')
    usedChars.append(' ')
    return usedChars

def initialize_frequency_analysis():
    return {letter: 0 for letter in alphabet()}

frequency_analysis = initialize_frequency_analysis()

neighbors = {}
beforeCounts = {letter: initialize_frequency_analysis() for letter in alphabet()}
afterCounts = {letter: initialize_frequency_analysis() for letter in alphabet()}

tripples = {}

plain = cipher
plain = plain.replace('X', ' ')
# plain = plain.replace('I', 'h') # I is h because it goes 38 times before X, but only 1 time after X
# plain = plain.replace('Q', 'h') # Q is h because it goes 38 times before X, but only 1 time after X
# plain = plain.replace('U', 't')
# plain = plain.replace('T', 'i')
# plain = plain.replace('*', 't')

# repeated letters are UU(5), EE(5), SS(4), **(3), YY(3), WW(3), XX(1), VV(1)
# these will probably represent the letters ss, ee, tt, ff, ll, mm and oo
# plain = plain.replace('U', 's')
# plain = plain.replace('E', 't')
# plain = plain.replace('S', 'e')
# plain = plain.replace('*', 'f')
# plain = plain.replace('Y', 'l')
# plain = plain.replace('W', 'm')
# plain = plain.replace('V', 's')

# plain = plain.replace('D', ' ')

plain = plain.replace('Q', 'i')
# plain = plain.replace('I', 'i')
# plain = plain.replace('M', 'i')
# plain = plain.replace('G', 'i')
# plain = plain.replace('C', 'i')
# plain = plain.replace('*', 'i')
# plain = plain.replace('B', 'i')

for i in range(len(plain)):
    frequency_analysis[plain[i]] += 1
    if i > 0:
        pair = plain[i-1] + plain[i]
        if pair not in neighbors:
            neighbors[pair] = 1
        else:
            neighbors[pair] += 1
        beforeCounts[plain[i]][plain[i-1]] += 1
        afterCounts[plain[i-1]][plain[i]] += 1

    if i > 1:
        tripple = plain[i-2] + plain[i-1] + plain[i]
        if tripple not in tripples:
            tripples[tripple] = 1
        else:
            tripples[tripple] += 1

def get_num (frequency_analysis):
    return frequency_analysis[1]

print("length of cipher: ", len(cipher))


unsorted_pairs = frequency_analysis.items()
sorted_items = sorted(unsorted_pairs, key = get_num)

descending = reversed(sorted_items)
descending = list(descending)

inorder = list()
for char in descending:
    inorder.append(char)

for key in inorder:
    print (key)

firstLetterCount = {}
secondLetterCount = {}
for pairs in neighbors:


    if pairs[0] not in firstLetterCount:
        firstLetterCount[pairs[0]] = 1
    else:
        firstLetterCount[pairs[0]] += 1

    if pairs[1] not in secondLetterCount:
        secondLetterCount[pairs[1]] = 1
    else:
        secondLetterCount[pairs[1]] += 1

print(firstLetterCount)
print("--------------------------------------------")
print(secondLetterCount)

unsorted_pairs = neighbors.items()
sorted_pairs = sorted(unsorted_pairs, key = get_num)

descending_pairs = reversed(sorted_pairs)
descending_pairs = list(descending_pairs)

for pairs in descending_pairs:
    if pairs[0][0] == pairs[0][1]:
        print(pairs, pairs[0][0] == pairs[0][1])

# Convert dictionaries to DataFrames
before_df = pd.DataFrame(beforeCounts).fillna(0)
after_df = pd.DataFrame(afterCounts).fillna(0)

# Print the DataFrames
print("Before Count:")
print(before_df)

print("\nAfter Count:")
print(after_df)

# Interleave the rows
mixed_df = pd.concat([before_df, after_df]).sort_index(kind='merge')

# Print the mixed DataFrame
print("Mixed Count:")
print(mixed_df)


unsorted_tripples = tripples.items()
sorted_tripples = sorted(unsorted_tripples, key = get_num)

descending_tripples = reversed(sorted_tripples)
descending_tripples = list(descending_tripples)

# for tripple in  descending_tripples:
#     if (tripple[1] > 1):
#         print(tripple)

words = plain.split()
wordCount = {}
for word in words:
    if word not in wordCount:
        wordCount[word] = 1
    else:
        wordCount[word] += 1

for word in wordCount:
    if len(word) == 1:
        print(word, wordCount[word])

print(cipher)
print("--------------------------------------------")
print(plain)
