
def getColor(r,g,b):
    avg = (r + g + b)/3
    
    if abs(r-avg) < 30 and abs(g-avg) < 30 and abs(b-avg) < 30:
        print('White')
    elif g > r and g > b:
        print('Green')
    elif b > r and b > g:
        print('Blue')
    elif r > g and r > b:
        d = r - g
        e = g - b
        if abs(d) < 30:
            print('Yellow')
        elif abs(e) < 15:
            print('Red')
        else:
            print('Orange')

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

        
