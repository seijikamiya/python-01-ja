def encode(word):
    unicode = ""
    for character in word:
        if character != (""):
            unicode += str(ord(character)) + " "
    return unicode

def decode(unicodes):
    word = ""
    for unicode in unicodes.split(" "):
        if unicode != (""):
            word += chr(int(unicode))
    return word

if __name__ == "__main__":
    print(encode("Hello World"))
    print(decode("72 101 108 108 111 32 119 111 114 108 100"))
    print(encode(""))
    print(decode(""))