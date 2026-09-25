lista_data = list(range(-5, 5))

filtro_menor_cero = list(filter(lambda x: x < 0, lista_data))

print("Lista completa: " + str(lista_data))
print("Lista filtrada: " + str(filtro_menor_cero))


print(filter(lambda x: x < 0, lista_data))