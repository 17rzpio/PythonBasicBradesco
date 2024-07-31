nota1 = int(input("digite nota 1"))
nota2 = int(input("digite nota 2"))
media = (nota1 + nota2)/2
if media > 7:
    print ("aprovado")
else:
    print("reprovado")

idade = int(input("digite idade"))
if (idade >= 18):
    print ("maior de idade")
elif idade >- 16:
    print("juvenil")
else:
    print ("menor de idade")

for n in range (10):
    print(n)

for n in range(5,16):
    print(n)

for n in range(10,0,-1):
    print(n)

x = 0
while (x < 10):
    print (x)
    x+=1

a2 = 1
a = float(input("digite valor real"))
while ( a2 > 0.0):
    a2 = float(input("digite valor real"))
    a = ( a + a2)/2
print(a)