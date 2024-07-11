habitantes = int(input("Cantidad total de habitantes:"))
ingreso_total = int(input("Ingrese el ingreso total del hogar:"))
tercera_edad = int(input("Total personas de la tercera edad:"))
ingreso_per_capita = ingreso_total/habitantes 
if habitantes <= 4:
    if ingreso_per_capita <= 60000:
        nivel_se = "C3"
    elif ingreso_per_capita > 60000 and ingreso_per_capita <= 100000:
        nivel_se = "C2"
    elif ingreso_per_capita > 100000 and ingreso_per_capita <= 300000:
        nivel_se = "C1"
    elif ingreso_per_capita > 300000:
        nivel_se = "AB"        
elif habitantes >= 5:
    if ingreso_per_capita <= 40000:
        nivel_se = "C3"
    elif ingreso_per_capita > 40000 and ingreso_per_capita <= 80000:
        nivel_se = "C2"
    elif ingreso_per_capita > 80000 and ingreso_per_capita <= 250000:
        nivel_se = "C1"
    elif ingreso_per_capita > 250000:
        nivel_se = "AB"
if tercera_edad >= 2:
    nivel_se = "C3"
print("Su nivel socioeconómico es:" + nivel_se)