f = open("Day2/input.txt", "r")

areal_total = 0

for i in f:
    areal = 0
    print(f'i is {i}')
    gift = i.strip().split("x")
    print(gift)
    length = int(gift[0])
    widht = int(gift[1])
    hight = int(gift[2])

    lw = 2*(length*widht)
    print(f'lw = {lw}')
    wh = 2*(widht*hight)
    print(f'wh = {wh}')
    hl = 2*(hight*length)
    print(f'hl = {hl}')

    areal = lw+wh+hl
    print(f'areal is {areal}')
    
    if lw < wh and lw < hl:
        areal = areal + length*widht
        print("lw")
    elif wh < lw and wh < hl:
        areal = areal + widht*hight
        print("wh")
    elif hl < lw and hl < wh:
        areal = areal + hight*length
        print("hl")

    print(f'1 total is {areal_total}')
   
   
    areal_total = areal_total + areal
    print(f'2 total is {areal_total}')

print(areal_total)

#1590419 is too low
#1724154 is too high