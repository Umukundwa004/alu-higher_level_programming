#!/usr/bin/python3


def uppercase(str: str) -> None:
    for letter in str:
    
        if "a" <= letter <= "z":
            letter = chr(ord(letter) - (ord("a") - ord("A")))
        print("{}".format(letter), end="")
    print()
