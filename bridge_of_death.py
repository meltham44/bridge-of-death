#!/usr/bin/env python3
global name


def introduction():
    print("Stop! Who would cross the Bridge of Death")
    print("Must answer me these questions three, 'ere the other side he see.")
    print("")
    name_check()


def name_check():
    global name
    name = input("What is your name? ").upper()
    if "ARTHUR" in name:
        print("My liege! You may pass!")
    else:
        quest_check()


def quest_check():
    quest = input("What is your quest? ").upper()
    if "GRAIL" in quest:
        colour_check()
    else:
        print("Only those who seek the Grail may pass.")


def colour_check():
    colour = input("What is your favourite colour? ").upper()
    if colour[0] == name[0]:
        print("You may pass!")
    else:
        print("Incorrect! You must now face the Gorge of Eternal Peril.")


if __name__ == '__main__':
    introduction()
