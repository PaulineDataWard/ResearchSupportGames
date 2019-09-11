#!/usr/bin/env python3

# By Alex Ball (University of Bath), very quickly

import random
import time


def displayIntro():
    print('''You are sat writing your grant proposal. The call
documentation says you have to supply a data management
plan. Perhaps you should see if the funder has a template
you could use. Or then again, you could just write about
you intention to publish your papers in open access
journals.''')
    print()


def chooseCave():
    cave = ''
    while not (cave.lower().startswith('y') or cave.lower().startswith('n')):
        print("Will you look for a template? (Yes or No)")
        cave = input('> ')

    if cave.lower().startswith('y'):
        return True

    return False


def checkCave(chosenCave):
    print()
    print('You write your plan...')
    time.sleep(2)
    print('You send it off with your grant proposal...')
    time.sleep(2)
    print('''Weeks later, an envelope comes back. You tear it open,
trembling with anticipation...''')
    print()
    time.sleep(2)

    prize = random.randint(1, 40)
    prize_money = "£{}0,000".format(prize)

    if chosenCave:
        print("Your grant application was successful, and you have been awarded {}!"
              .format(prize_money))
    else:
        print('''Your grant application was denied. One of the
reasons cited is that your data management plan was
disastrous.''')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print()
    print('Do you want to play again? (yes or no)')
    playAgain = input()
