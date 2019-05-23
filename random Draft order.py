from random import *
order = []

with open('NBA teams.txt') as file:
    contents = file.readlines()
    count = 0
    while count < 30:
        num = randint(1,30)
        if contents[num - 1] != "0":
            order.append(contents[num-1])
            contents[num - 1] = "0"
            count += 1
count = 0
with open('Order.txt', 'w') as draft:

    while count < 30:
        draft.write(str(count))
        draft.write(order[count])
        draft.write("\n")
        count += 1
