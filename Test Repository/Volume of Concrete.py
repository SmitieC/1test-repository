length = float(input("Enter the length of the slab: "))
width = float(input("Enter the width of the slab: "))
height = float(input("Enter the height of the slab: "))
# get all inputs of measurements
volume = length * width * height
print(f"The volume of Concrete required for a slab:\n with a length of {length} "
      f"\nand a width of {width} \nand a height of {height}"
      f" is:\n{volume} Cubic Meters")
