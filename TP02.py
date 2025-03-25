nombre = int(input("Choisir un nombre : "))

a,b = 0,1
alist = []
for i in range(nombre):
    alist.append(a)
    a,b = b,a + b

atuple = tuple(alist)
adict = dict(enumerate(alist))

for nombre in alist:
    print(nombre)