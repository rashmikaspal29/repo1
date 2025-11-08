def evaluateApt(numRooms, rent):
    if numRooms >= 2 and rent < 800:
        return "Rent it!"
    return "Keep looking"