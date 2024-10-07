#Ejercicio 3.1 Propuesta de mejora con algoritmo ChaCha20-Poly1305
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')

datos_autenticados = bytes("","UTF-8")

#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = bytes.fromhex('fbdbffb77f5966b3')
print('nonce  = ', nonce_mensaje.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
cipher.update(datos_autenticados)
texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)

print("texto cifrado:", texto_cifrado.hex())
print("tag:" , tag.hex())