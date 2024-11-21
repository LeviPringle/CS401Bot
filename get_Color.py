def getColor(r,g,b):
    avg = (r + g + b)/3
    if abs(r-avg) <= 20 and abs(g-avg) <= 20 and abs(b-avg) <= 20:
        print('White')
    elif g >= r and g >= b:
        if b > 100:
            print('Blue')
        elif r >= 180:
            print('Yellow')
        else:
            print('Green')
    elif b >= r and b >= g:
        if r > 150 or g > 150:
            print('White')
        else:
            print('Blue')
    elif r >= g and r >= b:
        d = r - g
        e = g - b
        if abs(d) <= 50:
            print('Yellow')
        elif b <= 40 and g <= 40:
            print('Red')
        else:
            print('Orange')
    else:
        print('White')

q = 0
while q != 1:
    print('do you want to get color?(y-yes/q-quit)')
    run = input()
    if run == 'q':
        q = 1
    else:
        
        a = int(input('give me red value:'))
        b = int(input('give me green value:'))
        c = int(input('give me blue value:'))
        getColor(a, b, c) 

        
