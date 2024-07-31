def frase():
    print("python eh show")

frase()

def lernotas():
    c = float(input("digite nota"))
    return c

def media(d,e):
    f = ( d + e)/2
    return f

a = lernotas()
b = lernotas()
g = media(a,b)
print("a media eh", g)