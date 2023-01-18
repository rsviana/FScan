## Essa funcao precisa ser revisada e entendida

import random, string, os
def generate_wordlist(length, num_words):
    words = []
    for _ in range(num_words):
        word = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        words.append(word)
    wlist = input("Enter name your wordlist: ")
    with open(wlist, "w") as f:
        for word in words:
            f.write(word + "\n")
    print()
    input("Press any key to return menu")
    os.system('python main.py') 
    return words


                