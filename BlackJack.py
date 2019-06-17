from random import *
def cards(num):
    if 1 <= num <= 4:
        return "A"
    elif 5 <= num <= 8:
        return 2
    elif 9 <= num <= 12:
        return 3
    elif 13 <= num <= 16:
        return 4
    elif 17 <= num <= 20:
        return 5
    elif 21 <= num <= 24:
        return 6
    elif 25 <= num <= 28:
        return 7
    elif 29 <= num <= 32:
        return 8
    elif 33 <= num <= 36:
        return 9
    elif 37 <= num <= 52:
        return 10

def game():
    money = 20
    loop = True
    print("WELCOME TO BLACKJACK")
    while loop:
        dealer = 0
        user = 0
        print("You currently have ", money, " dollars in your account")
        wager = input("How much would you like to wager")
        wager = int(wager)
        if wager <= money:
            i = 0
            while i < 4:
                num = randint(1,52)
                card = cards(num)
                if i < 2:
                    if card == "A":
                        if dealer + 11 > 21:
                            dealer += 1
                        else:
                            dealer += 11
                    else:
                        dealer += card
                else:
                    if card == "A":
                        if user + 11 > 21:
                            user += 1
                        else:
                            user += 11
                    else:
                        user += card
                i += 1
            print("Dealer has ", dealer)
            print("You have ", user)
            if user == 21 and dealer != 21:
                print("YOU WON")
                money += wager
                play = input("Would you like to play again?")
                if play == "No" or play == "no":
                    loop = False
                    print("Thank you for playing you earned ", money, " dollars")
                    exit()
            elif user != 21 and dealer == 21:
                print("You lost :(")
                money -= wager
                if money <= 0:
                    print("You ran out of money. You can no longer play")
                    exit()
                else:
                    play = input("Would you like to play again?")
                    if play == "No" or play == "no":
                        loop = False
                        print("Thank you for playing you earned ", money, " dollars")
                        exit()
            else:
                hit = input("Would you like to draw another card?")
                if hit == "yes":
                    num = randint(1,52)
                    card = cards(num)
                    if card == "A":
                        if user + 11 > 21:
                            user += 1
                        else:
                            user += 11
                    else:
                        user += card
                if user > 21:
                    print("BUST. you lost :(")
                    print("Dealer has ", dealer)
                    print("You have ", user)
                    money -= wager
                elif user >= dealer:
                    print("YOU WON")
                    print("Dealer has ", dealer)
                    print("You have ", user)
                    money += wager
                elif dealer > user:
                    print("You lost :(")
                    print("Dealer has ", dealer)
                    print("You have ", user)
                    money -= wager
                if money <= 0:
                    print("You ran out of money. You can no longer play")
                    exit()
                else:
                    play = input("Would you like to play again?")
                    if play == "No" or play == "no":
                        loop = False
                        print("Thank you for playing you earned ", money, " dollars")
                        exit()
game()
