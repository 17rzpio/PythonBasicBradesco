a = 5
b = 15
c = 20
print("a == b and b > c : ", a == b and b > c)
print(" a < b or b > c : ", a < b or b > c)
print(" not a == b : ", not a == b)

idade = int(input("digite idade"))
if (idade >= 18):
    print ("maior de idade")
print ("testda")

a = int(input("digite vlor pra a"))
b = int(input("digite valor pra b"))
if (a>b):
    aux = a
    a = b
    b = aux
print ("valor de a agora eh",a)
print("valor de b agora eh",b)

idade = int(input("digite idade"))
if (idade >= 18):
    print ("maior de idade")
else:
    print("menor de idade")