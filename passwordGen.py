import random


def generatePass():
    with open('words.txt', 'r') as document:
        words = document.readlines()
    document.close()

    w = len(words)

    x = words[int(random.randrange(0, w))].capitalize()
    y = words[int(random.randrange(0, w))].capitalize()
    z1 = random.randrange(0, 9)
    z2 = random.randrange(0, 9)

    password = x + y + str(z1) + str(z2)

    return "".join(password.split())
