#Práctica Final
#Ejercicio 1

#DATOS:
#Desarrollador clave fija B1EF2ACFE2BAEEFF
#Clave final 91BA13BA21AABB12
#RESULTADO:

#Clave del Key Manager 20553975C31055ED

def xor_data (binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip (binary_data_1, binary_data_2)])


m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("91BA13BA21AABB12")

print(xor_data (m,k).hex().upper())

#Datos:
#Clave fija B1EF2ACFE2BAEEFF
#Clave dinamica de produccion B98A15BA31AEBB3F
#RESULTADO:
#Clave de memoria 08653F75D31455C0
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip (binary_data_1, binary_data_2)])


m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("B98A15BA31AEBB3F")

print(xor_data (m,k).hex().upper())




