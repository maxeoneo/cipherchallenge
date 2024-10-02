import re
from collections import Counter

with open('cipher.txt', 'r') as file:
    cipher = file.read().rstrip().replace('\n', '')

print(cipher)

# Compile the regex to find repetitions of 3 or more letters
repeater = re.compile(r"(.{3,}).*?\1")

def repeated(s):
    matches = repeater.findall(s)
    for match in matches:
        print(f"Repeated string: {match}")
        occurences = [m.start() for m in re.finditer(match, s)]
        print(f"Occurences: {occurences}: Difference between occurences: {occurences[1] - occurences[0]}")
        # differences are 220, 45, 35, 130 and 10. So the key is probably 5 (shared divider)

repeated(cipher)

# split the text in 5 parts by index % 5
def split_by_modulo(s, n):
    parts = ['' for _ in range(n)]
    for i, char in enumerate(s):
        parts[i % n] += char
    return parts

# frequency analysis each part
def frequency_analysis(text):
    return Counter(text)

cipher_parts = split_by_modulo(cipher, 5)
for i, part in enumerate(cipher_parts):
        print(f"Part {i}: {part}")
        frequencies = frequency_analysis(part)
        print(f"Frequencies for part {i}: {frequencies}")

def shift_letter(letter, shift):
    if 'A' <= letter <= 'Z':
        return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= letter <= 'z':
        return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    else:
        return letter

def shift_text(text, shift):
    return ''.join(shift_letter(char, shift) for char in text)


shifts = [ord('W') - ord('E'), ord('G') - ord('E'), ord('Y') - ord('E'), ord('F') - ord('E'), ord('E') - ord('E')]

password = (chr(ord('A') + shifts[0]) + chr(ord('A') + shifts[1]) + chr(ord('A') + shifts[2]) + chr(ord('A') + shifts[3]) + chr(ord('A') + shifts[4]))
print (f"Password: {password}")
print(chr(ord('A') + shifts[0]), ord('W') - ord('E'))
print(chr(ord('A') + shifts[1]), ord('G') - ord('E'))
print(chr(ord('A') + shifts[2]), ord('Y') - ord('E'))
print(chr(ord('A') + shifts[3]), ord('F') - ord('E'))
print(chr(ord('A') + shifts[4]), ord('E') - ord('E'))

cipher_parts[0] = shift_text(cipher_parts[0], -shifts[0])
cipher_parts[1] = shift_text(cipher_parts[1], -shifts[1])
cipher_parts[2] = shift_text(cipher_parts[2], -shifts[2])
cipher_parts[3] = shift_text(cipher_parts[3], -shifts[3])
cipher_parts[4] = shift_text(cipher_parts[4], -shifts[4])

interleaved = ''.join(''.join(x) for x in zip(*cipher_parts))

plain = interleaved
print(f"Plain text:")
print(plain)