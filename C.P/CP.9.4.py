def dotDash(string):
    if len(string)%2 == 0:
        return (f"-{'-'.join(string)}-")
    else:
        return (f".{'.'.join(string)}.")
