#Ejercicio 3
# Pasos a seguir:
# Pasar la clave,texto y nonce a bytes
# Clave chacha20-256:AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120
# Texto: KeepCoding te enseña a codificar y a cifrar
# Nonce: 9Yccn/f5nJJhAt2S
# Utilizar una biblioteca criptografica que soporte ChaCha20 para realizar el cifrado

#Resultado:
#Texto cifrado: en word.
from Crypto.Cipher import ChaCha20
import base64

# Datos
textoPlano = bytes('Keepcoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = base64.b64decode("9Yccn/f5nJJhAt2S")

print('nonce  = ', nonce_mensaje.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado.hex() )
#print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode())


#Descifrado...
decipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintext = decipher.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))

#texto = "KeepCoding te enseña a codificar y a cifrar"
#clave = bytes.fromhex("AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120")
#nonce_mensaje = base64.b64decode("9Yccn/f5nJJhAt2S")

# Convertir el texto a bytes
#texto_bytes = texto.encode('utf-8')

# Crear el cifrador ChaCha20
#cipher = ChaCha20.new(key=clave, nonce= nonce_mensaje)
 
# Cifrar el texto
#texto_cifrado = cipher.encrypt(texto_bytes)

#print("Texto cifrado:", texto_cifrado.hex())

