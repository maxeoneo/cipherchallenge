def decipher(content, shift):
        result = ""
        for char in content:
            ascii = ord(char)
            
            if ascii == 32:
                moved = 32
            else:
                moved = ascii - shift
                if moved < 65:
                    moved += 26

            result += chr(moved)
        return result

# Open the file in read mode
with open('cipher.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

for i in range(26):
    print(i)
    print(decipher(content, i))

# only i=7 makes sense
print("result:")
print(decipher(content, 7)) # latin for "each man is the smith of his own fortune"