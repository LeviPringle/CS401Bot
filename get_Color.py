def getColor(r,g,b):
    avg = (r + g + b)/3
    if abs(r-avg) <= 20 and abs(g-avg) <= 20 and abs(b-avg) <= 20 and r >= 100:
        return 'White'
    elif abs(r-avg) <= 20 and abs(g-avg) <= 20 and abs(b-avg) <= 20 and r < 100:
        return 'Black'
    elif g >= r and g >= b:
        if r >= 180:
            return 'Yellow'
        else:
            return 'Green'
    elif b >= r and b >= g:
        if r > 150 or g > 150:
            return 'White'
        else:
            return 'Blue'
    elif r >= g and r >= b:
        d = r - g
        e = g - b
        if abs(d) <= 50:
            return 'Yellow'
        elif abs(e) <= 40:
            return 'Red'
        else:
            return 'Orange'
    


        
