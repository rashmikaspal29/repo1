def evaluateChessLocation(position):
    if position == a1 or position == h1 or position == a8 or position == h8:
        return "Corner"
    
    if position == 