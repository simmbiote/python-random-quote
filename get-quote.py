import random


def primary():
    file = open("quotes.txt")
    quotes = file.readlines()
    file.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)

    print(quotes[rnd])
    print(quotes[rnd])
    print(quotes[rnd])


if __name__ == "__main__":
    primary()
