def triangle_type(side1, side2, side3):
  """
  This function takes three side lengths as input and determines the type of triangle and its area (if valid).

  Args:
      side1: The length of the first side.
      side2: The length of the second side.
      side3: The length of the third side.

  Returns:
      A tuple containing a string describing the type of triangle and its area (float) or "invalid" if the triangle cannot be formed.
  """

  # Check for invalid triangle (sum of any two sides must be greater than the third)
  if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
    return "invalid"

  # Check for triangle type
  if side1 == side2 == side3:
    triangle_type = "equilateral"
    # Area for equilateral triangle: (sqrt(3) * side^2) / 4
    area = (3**0.5) * (side1**2) / 4
  elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle_type = "isosceles"
    # Heron's formula for non-right isosceles (assuming base = side1, other sides = side2)
    s = (side1 + side2 + side3) / 2  # Semi-perimeter
    area = (s * (s - side1) * (s - side2))**0.5
  else:
    triangle_type = "scalene"
    # Heron's formula for general triangles
    s = (side1 + side2 + side3) / 2  # Semi-perimeter
    area = (s * (s - side1) * (s - side2) * (s - side3))**0.5

  return triangle_type, area

# Get side lengths from user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Call the function to determine type and area
result = triangle_type(side1, side2, side3)

# Print the result (unpack the tuple)
triangle_type, area = result

if triangle_type == "invalid":
  print("The triangle is invalid.")
else:
  print("The triangle is:", triangle_type)
  print("The area of the triangle is:", area)
