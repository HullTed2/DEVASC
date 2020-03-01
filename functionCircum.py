# Print the circumference for circles with a radius of 2, 5, and 7

# In this example, circumference and
# printCircumference are the names of
# the functions. 'radius' is a parameter to
# the function and can be used in the function.
# This function returns the value of the
# circumferenceValue to the code that called
# the function.

def circumference(radius):
  # Formula for a circumference is c = pi * diameter
  # Formula for a diameter is d = 2 * radius
  pi = 3.14 # (Will hardcode pi in this example)
  circumferenceValue = pi * radius * 2
  return circumferenceValue

def printCircumference(radius):
  myCircumference = circumference(radius)
  print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(myCircumference))

radius1 = 2
radius2 = 5
radius3 = 7
# In the below line of code, the value of radius1 (2)
# is the argument to the printCircumference function
printCircumference(radius1)
printCircumference(radius2)
printCircumference(radius3)