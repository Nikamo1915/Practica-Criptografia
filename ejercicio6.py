#Ejercicio 6
#Datos:
#Calcula el hmac-256 A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB del siguiente texto:  
#Siempre existe más de una forma de hacerlo, y más de una solución válida. 

#Resultado:



# Texto de entrada


from Crypto.Hash import HMAC, SHA256


mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.","UTF-8")

clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
# Crear el objeto HMAC-SHA256
hmac_objeto = HMAC.new(clave_bytes, msg=mensaje_bytes, digestmod=SHA256)

print("HMAC:", hmac_objeto.hexdigest())




