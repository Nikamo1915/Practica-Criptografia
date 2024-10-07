#Ejercicio 9
#Datos:
# Se requiere calcular el KCV de las siguiente clave AES: 
#A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72 
# KCV(SHA-256)  se corresponderá con los 3 primeros bytes del SHA-256
# KCV(AES)  se corresponderá con cifrar un texto del tamaño del bloque AES (16 bytes) compuesto con ceros binarios (00), así como un iv igualmente compuesto de ceros binarios. 

#Resultado:
#KCV(SHA-256): db7df2
#KCV(AES): 5244db

import hashlib
from Crypto.Cipher import AES

# Clave AES proporcionada
clave_aes = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

# Calcular KCV(SHA-256)
hash_sha256 = hashlib.sha256(clave_aes).digest()
kcv_sha256 = hash_sha256[:3]
print("KCV(SHA-256):", kcv_sha256.hex())

# Calcular KCV(AES)
# Bloque de texto y IV de 16 bytes de ceros binarios
textoPlano_bytes = bytes.fromhex('00000000000000000000000000000000')
#bloque_ceros = bytes(16)
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
#iv_ceros = bytes(16)

# Crear el objeto de cifrado AES en modo CBC
cipher = AES.new(clave_aes, AES.MODE_CBC, iv_bytes)
texto_cifrado = cipher.encrypt(textoPlano_bytes)
kcv_aes = texto_cifrado[:3]
print("KCV(AES):", kcv_aes.hex())
