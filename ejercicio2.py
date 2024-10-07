#Datos Ejercicio 2:
#Clave AES A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72
#iv en hex a ceros binarios*16
#texto en claro:TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI= 
#Modo de operacion:AES/CBC/PKCS7

#Resultados:
#Que se obtiene al descifrarlo?? Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.
# que obtenemos si cambiamos el padding a x923 en el descifrado?? respuesta en word.
# cuanto padding se ha añadido en el cifrado??respuesta en word.


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave e iv
clave_bytes = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
iv_bytes = bytes.fromhex('00' * 16)

# Dato cifrado en base64
texto_en_claro = base64.b64decode('TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=')

# Definir el cifrador
cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)

mensaje_des_bytes = cipher.decrypt(texto_en_claro)
print (mensaje_des_bytes.hex())

# Descifrar y deshacer el padding PKCS7
#mensaje_des_bytes =unpad(cipher.decrypt(texto_en_claro), AES.block_size)

print("Texto en claro:", mensaje_des_bytes.decode('utf-8'))
