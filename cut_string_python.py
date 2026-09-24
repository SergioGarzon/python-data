# Example of string slicing in Python

nombre_persona = "Alicia Barrera"

print(nombre_persona[0:6])  # Output: Alicia
print(nombre_persona[7:14])  # Output: Barrera

print("\nOtro ejemplo")

print(nombre_persona[:6]) # Output: Alicia
print(nombre_persona[7:]) # Output: Barrera


print("\nOtro salto")

print(nombre_persona[::-1]) # Output: arerraB aicilA
print(nombre_persona[::2]) # Output: Aii arr
print(nombre_persona[:5:2]) # Output: Aii
print(nombre_persona[5:10:2]) # Output: aBr
print(nombre_persona[::-2]) # Output: aerBacl 

