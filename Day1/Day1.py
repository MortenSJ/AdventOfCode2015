f = open("Day1/input.txt", "r")

up = 0
down = 0
floor = 0
count = 0

for i in f.read():
    up = i.count("(")+up
    down = i.count(")")+down
    if i == '(':
        floor = floor +1
    elif i == ")":
        floor = floor -1
    else: print("error")

floor = 0 + up -down

print(f"Floor is: {floor}")

f = open("Day1/input.txt", "r")
floor = 0

for i in f.read():
    count = count + 1
    up = i.count("(")+up
    down = i.count(")")+down
    if i == '(':
        floor = floor +1
    elif i == ")":
        floor = floor -1
    else: print("error")

    if floor == -1: 
        print(f'on move {count} is santa in the basement!')
        break