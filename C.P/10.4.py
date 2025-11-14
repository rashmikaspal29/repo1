def evaluateChessLocation(position):
    if position == a1 or position == h1 or position == a8 or position == h8:
        return "Corner"
    
    if position[0] == 'a' or position[0] == 'h' or position[1] == '1' or position[1] == '8':
        return "Border"
    
    else:
        return "Inside"
