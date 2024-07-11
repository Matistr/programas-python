print("Bienvenido a Mamá Juana")
pizzas = int(input("Cuántas pizza desea ordenar:"))
if pizzas > 0:
    cont=0
    total = 0
    suma_ingred = 0
    while(cont < pizzas):
        cont = cont +1
        ingred_tot=int(input("Ingrese la cantidad de ingredientes de su pizza "+str(cont) + ":"))
        suma_ingred = suma_ingred + ingred_tot
        print("1.- Tomate $300")
        print("2.- Piña $500") 
        print("3.- Pepperoni $400") 
        print("4.- Aceitunas $600")
        cont_ing = 0
        subtotal = 1000
        while(cont_ing < ingred_tot):
            cont_ing = cont_ing +1
            ingred = int(input("Ingrese el ingrediente " + str(cont_ing) + ":"))
            while ingred < 1 or ingred > 4:
                print("Por favor, ingrese un ingrediente válido ")
                cont_ing = cont_ing -1
                break
            if ingred == 1:
                subtotal = subtotal + 300
            if ingred == 2:
                subtotal = subtotal + 500
            if ingred == 3:
                subtotal = subtotal + 400
            if ingred == 4:
                subtotal = subtotal + 600         
        print("Subtotal $ " + str(subtotal))
        total = total + subtotal
    #El numero de pizzas e ingredientes sea par
    if pizzas % 2 == 0:
        if suma_ingred % 2 == 0:
            total = total * 0.9
            print("Su compra tiene un 10 % de descuento")           
    print("El total es $ " + str(total))