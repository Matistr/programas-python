#Ejercicio 1
class Triangulo:
  def __init__(self, l1, l2, l3):
    self.lado1 = l1
    self.lado2 = l2
    self.lado3 = l3
  
  def CalcularPerimetro(self):
    return self.lado1 + self.lado2 + self.lado3 

t1 = Triangulo(1,2,3)
t2 = Triangulo(100, 40, 30)

print(t1.lado1, t1.lado2, t1.lado3)
print("Perimetro de t1", t1.CalcularPerimetro() )

print(t2.lado1, t2.lado2, t2.lado3)
print("Perimetro de t2", t2.CalcularPerimetro() )
