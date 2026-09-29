# Other example

from persona import Persona

list_person = [
    Persona(1, "Mauro", "Britos"),
    Persona(2, "Mauro", "Perez"),
    Persona(3, "Azul", "Virginia"),
    Persona(4, "Ana", "Benavidez"),
]

list_person_2 = [l for l in list_person if l.dni == 2]

for l in list_person_2:
    print(l)

