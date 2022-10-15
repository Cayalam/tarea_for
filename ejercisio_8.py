N=int(input("Digita No.de elementos de la serie: "))
s="serie: "

for i in range(1,N+1):
    if i<N:
        s=s+str(i**(i-1))+","
        
    else:
        s=s+str(i**(i-1))
print(s)