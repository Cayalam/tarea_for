m=int(input("¿Cuantos numeros enteros quieres calcular?: "))
x=0
 
for i in range(2,m+1):
    primos=True
    for r in range (2,i):
        if i==r:
            break
        elif i%r ==0:
            primos= False
        else:
            continue
    if primos == True:
        print("",i, end="")
        x+=1
print(x)
    

       
    

    
