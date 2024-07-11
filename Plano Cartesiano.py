#Ejercicio 2
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Punto(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Punto(self.x / other.x, self.y / other.y)
p1 = Punto(4,6)
p2 = Punto(2,3)
print(p1/p2)