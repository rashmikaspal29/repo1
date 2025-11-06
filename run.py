def verse(thing, verb, noise):
    print(f"The {thing} on the bus {verb} {noise},\n{noise};")
    print(f"{noise}.\nThe {thing} on the bus {verb} {noise},")
    print("all through the town.")

def main():
    verse('wheels', 'go', 'round and round')
    print()
    verse('wipers', 'go', 'swish, swish, swish')
    print()
    verse('horn', 'goes', 'beep, beep, beep')
main()