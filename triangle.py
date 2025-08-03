class Triangle:
    _instance_count = 0  # Static/class-level counter

    def __init__(self, a=1.0, b=None, c=None):
        # Clone constructor if first argument is a Triangle
        if isinstance(a, Triangle):
            clone = a
            self._a = clone.a
            self._b = clone.b
            self._c = clone.c

        # Equilateral triangle
        elif b is None and c is None:
            self._a = self._b = self._c = float(a)

        # Isosceles triangle (two equal sides)
        elif c is None:
            self._a = self._b = float(a)
            self._c = float(b)

        # Scalene triangle (all sides different)
        else:
            self._a = float(a)
            self._b = float(b)
            self._c = float(c)

        Triangle._instance_count += 1  # Increase instance counter

    # Getter and Setter for side a
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side 'a' must be greater than zero.")

    # Getter and Setter for side b
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError("Side 'b' must be greater than zero.")

    # Getter and Setter for side c
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if value > 0:
            self._c = value
        else:
            raise ValueError("Side 'c' must be greater than zero.")

    # Instance method: calculate perimeter
    def get_perimeter(self):
        return self._a + self._b + self._c

    # Check if triangle is right-angled using Pythagorean Theorem
    def is_right_triangle(self):
        sides = sorted([self._a, self._b, self._c])
        x, y, z = sides
        return abs(x**2 + y**2 - z**2) < 1e-9

    # String representation
    def __str__(self):
        return f"Triangle(a={self._a}, b={self._b}, c={self._c})"

    # Class method: total instances created
    @classmethod
    def total_created(cls):
        return cls._instance_count
