from math import sqrt


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    @staticmethod
    def are_orthogonal(vec_1, vec_2):
        return vec_1.dot(vec_2) == 0


if __name__ == "__main__":
    vec1 = Vector3D(1, 2, 3)
    vec2 = Vector3D(4, 5, 6)

    print("Vector 1:", vec1)
    print("Vector 2:", vec2)
    print("Norm of Vector 1:", vec1.norm())
    print("Norm of Vector 2:", vec2.norm())
    print("Addition:", vec1 + vec2)
    print("Subtraction:", vec1 - vec2)
    print("Scalar Multiplication:", vec1 * 2)
    print("Dot Product:", vec1.dot(vec2))
    print("Cross Product:", vec1.cross(vec2))
    print("Are orthogonal:", Vector3D.are_orthogonal(vec1, vec2))
