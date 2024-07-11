def MatrizMariposa(matriz):
  matriz_salida = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
  for i in range(len(m)):
    for j in range(len(m[0])):
      matriz_salida[len(m)-1-i][len(m[0])-1-j] = m[i][j]
  return matriz_salida
def MatrizEspejo(matriz):
  matriz_salida = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
  for i in range(len(m)):
    for j in range(len(m[0])):
      matriz_salida[i][len(m[0])-1-j] = m[i][j]
  return matriz_salida
m = [["a","b","c"],
 ["d","e","f"],
 ["g","h","i"]]
print(MatrizMariposa(m))
print(MatrizEspejo(m))