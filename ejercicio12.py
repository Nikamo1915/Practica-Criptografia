#Ejercicio 12
#Datos:
#Key:E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74 
#Nonce:9Yccn/f5nJJhAt2S 
#Texto: He descubierto el error y no volveré a hacerlo mal 

#Resultado:
#Texto cifrado en hexadecimal: 5dcbb6261d0fba29ce39431e9a013b34cbca2a4e04bb2d90149d61f4afd04d65e2abdd9d84bba6eb8307095f5078fbfc16256d
#Texto cifrado en base64: Xcu2Jh0PuinOOUMemgE7NMvKKk4Euy2QFJ1h9K/QTWXiq92dhLum64MHCV9QePv8FiVt


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


plaintext_bytes = bytes("He descubierto el error y no volveré a hacerlo mal","UTF-8")
clave_bytes = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")
print('nonce  = ', nonce.hex())
#nonce = bytes.fromhex('47e6831df094b7a6')

# Cifrar el texto
cipher = AES.new(clave_bytes, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)

# Convertir a hexadecimal y base64
ciphertext_hex = ciphertext.hex()
ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')


print(f"Texto cifrado en hexadecimal: {ciphertext_hex}")
print(f"Texto cifrado en base64: {ciphertext_base64}")
print("Tag:", tag.hex())
   
    