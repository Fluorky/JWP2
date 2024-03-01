import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        logging.info(f"Point moved to ({self.x}, {self.y})")

    @staticmethod
    def distance(point_1, point_2):
        distance = math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
        logging.info(f"Distance between {point_1} and {point_2}: {distance}")
        return distance

    def __eq__(self, other):
        equal = self.x == other.x and self.y == other.y
        logging.info(f"Points {self} and {other} are {'equal' if equal else 'not equal'}")
        return equal

    def __add__(self, other):
        new_point = Point2D(self.x + other.x, self.y + other.y)
        logging.info(f"Added points {self} and {other} to get {new_point}")
        return new_point


# Usage examples:
if __name__ == "__main__":
    point1 = Point2D(3, 4)
    logging.info(point1)  # Should log: Point2D(3, 4)
    logging.info(point1.length())  # Should log: 5.0

    point1.move(1, -2)  # Should log: Point moved to (4, 2)
    logging.info(point1)  # Should log: Point2D(4, 2)

    point2 = Point2D(1, 1)
    Point2D.distance(point1, point2)  # Should log the distance between point1 and point2

    logging.info(point1 == point2)  # Should log: Points Point2D(4, 2) and Point2D(1, 1) are not equal
    point2.move(3, 1)
    logging.info(point1 == point2)  # Should log: Points Point2D(4, 2) and Point2D(4, 2) are equal

    p3 = point1 + point2
    logging.info(p3)  # Should log: Added points Point2D(4, 2) and Point2D(4, 2) to get Point2D(8, 4)
