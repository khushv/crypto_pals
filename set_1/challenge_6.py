import base64
from challenge_5 import text_to_bytes

def mod_ham(x, y):
    return sum(bin(i^j).count("1") for i,j in zip(x,y))

def likely_candidate(text, min=2, max=40):
    result = {}
    for i in range(min, max):
        result[i] = mod_ham(text[0:i], text[i:2*i])

def base64_file_to_bytes(filename):
    #reads file and strips newline characters
    with open(filename) as f:
        data = f.read().replace("\n", "")

    x = len(text_to_bytes(base64.decode(data))
    #y = len(text_to_bytes(base64.decode(data)))

if __name__ == "__main__":
    a = text_to_bytes("this is a test")
    b = text_to_bytes("wokka wokka!!!")
    #print(mod_ham(a,b))

    x = base64_file_to_bytes("6.txt")
