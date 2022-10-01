# Una pelota de deja caer de una altura h, y en cada rebote sube el 10% menos del anterior. Hacer el diagrama de flujo y el programa en Python, que le h y que calculé e imprima en cual rebote la pelota no alcanza a subir la quinta parte de la altura inicial.

#input

H = int(input("Digite la altura:"))

#processing
Q= H / 5
r = 0
while H>Q:
    H = H - (H * 0.1)
    r = r+1
    
#output
print("Numero de rebotes: "+str(r))
    