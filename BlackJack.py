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

def opening_draw(player):
    i = 0
    while i < 2:
        num = randint(1,52)
        card = cards(num)
        if card == "A":
            value = 11
            player.append(value)
        else:
            player.append(card)
        i += 1
    return checkaces(player)

def checkaces(player):
    i = 0
    while i < len(player):
        if player[i] == 11 and sum(player) > 21:
            player[i] = 1
        i += 1
    return player
def draw(player):
    num = randint(1,52)
    card = cards(num)
    if card == "A":
        value = 11
        player.append(value)
    else:
        player.append(card)
    return checkaces(player)

def checkwin(user,dealer):
    if sum(user) > 21:
        print("BUST. you lost :(")
        print("Dealer has ", dealer)
        print("You have ", user)
        return False
    elif sum(dealer) > 21:
        print("YOU WON")
        print("Dealer has ", dealer)
        print("You have ", user)
        return True
    elif sum(user) >= sum(dealer):
        print("YOU WON")
        print("Dealer has ", dealer)
        print("You have ", user)
        return True
    elif sum(dealer) > sum(user):
        print("You lost :(")
        print("Dealer has ", dealer)
        print("You have ", user)
        return False

def game():
    money = 20
    loop = True
    print("WELCOME TO BLACKJACK")
    while loop:
        dealer = []
        user = []
        print("You currently have ", money, " dollars in your account")
        wager = input("How much would you like to wager")
        wager = int(wager)
        if wager <= money:
            i = 0
            dealer = opening_draw(dealer)
            user = opening_draw(user)
            print("Dealer has ", dealer)
            print("You have ", user)
            if sum(user) == 21 and sum(dealer) != 21:
                print("YOU WON")
                money += wager
                play = input("Would you like to play again?")
                if play == "No" or play == "no":
                    loop = False
                    print("Thank you for playing you earned ", money, " dollars")
                    exit()
            elif sum(user) != 21 and sum(dealer) == 21:
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
                loop2 = True
                while loop2:
                    hit = input("Would you like to draw another card?")
                    if hit == "yes":
                        draw(user)
                        if sum(user) < 21 and sum(user) > sum(dealer):
                            draw(dealer)
                        print("Dealer has ", dealer)
                        print("You have ", user)
                        if sum(user) > sum(dealer) or sum(user) == 21:
                            loop2 = False
                    else:
                        loop2 = False
                win = checkwin(user,dealer)
                if win == True:
                    money += wager
                else:
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
