from triangle import Triangle

# Default constructor object
t1 = Triangle()
print("t1 =", t1)

# Equilateral constructor object
t2 = Triangle(3)
print("t2 =", t2)

# Isosceles constructor object
t3 = Triangle(3, 5)
print("t3 =", t3)

# Scalene constructor object
t4 = Triangle(3, 5, 9)
print("t4 =", t4)

# Clone constructor object
t5 = Triangle(t2)
print("t5 (clone of t2) =", t5)

# Perimeter Calculation
print(f"Perimeter of t3: {t3.get_perimeter()}")

# Right-Angled Triangle Check
print(f"Is t3 a right-angled triangle? {t3.is_right_triangle()}")

# Getter and Setter Test
print(f"Original side a of t2: {t2.a}")
t2.a = 10
print(f"Updated side a of t2: {t2.a}")

# Total Triangle Objects Created
print(f"Total Triangle Objects Created: {Triangle.total_created()}")

