#Import math allows the program to access the math library
import math

#Input Stage: Ask the user for the radius of a garden
Radius = float(input("Please enter the radius of the garden in meters: "))

#Processing Stage: This stage calculates the information about the garden, like its area, circumference, squared root and more.
Area = math.pi * math.pow(Radius, 2)
Circumference = 2 * math.pi * Radius
SquaredArea = math.sqrt(Area)
RoundedDownArea = math.floor(Area)
RoundedUpArea = math.ceil(Area)

#Output Stage: This dstage displays the calculated information of the garden to the user
print(f"The area of the garden is {Area:.2f} square meters.")
print(f"The circumference of the garden is: {Circumference:.2f} square meters.")
print(f"The Square Root of the garden is: {SquaredArea:.2f}")
print("The Rounded Down Area is: ", RoundedDownArea, "square meters")
print("The Rounded Up Area is: ", RoundedUpArea, "square meters")