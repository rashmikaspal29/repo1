import math
def computeVolume(radius):
    volume = (4/3)*math.pi * radius**3
    return (volume)

def main():
    radius = float(input("Enter the radius of a sphere: "))
    print(f"The volume is {round(computeVolume(radius), 3)}")
main()
