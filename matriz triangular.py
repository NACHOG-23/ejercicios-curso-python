filas=int(input())
matriz =[[0 for i in range(filas)]for j in range (filas)]
boler=True
for a in range(filas):
    cadena=input()
    for b in range (filas):
        matriz[a][b]=int(cadena[b*2])
    for b in range (filas):
        if a>b:
            if matriz[a][b]!=0:
                boler=False
if boler==True:
    print("Es identidad")
else:
    print("No es identidad")
