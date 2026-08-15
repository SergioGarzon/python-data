names = [ "Jhon", "Peter", "Sarah", "Linda", "Jade", "Evelyn" ]

for name in names:
    print(name)

contador = 0

while contador != 100:
    print(contador)
    contador += 1
 
contador = 0

while contador != 100:    
    if contador % 2 == 0:
        print("Par " + str(contador))
        #continue
    contador += 1

contador = 0

while contador != 100:
    if contador % 2 != 0:
        print("Impar " + str(contador))
        break
    contador += 1


for name in names:
    if(name == "Virginia"):
        print("Se encontro Virginia")
else:
    print("No se encontro virginia")

