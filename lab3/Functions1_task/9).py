import math

def sphere_volume(radius):
    # Volume formula: (4/3) * π * r^3
    volume = (4/3) * math.pi * radius**3
    return volume

radius = 5
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {volume}")
