#Ejercicio 5
#Datos del ejercicio 5-A y 5-C con mismos resultados
#Genera  un SHA3  de 256 bits con el siguiente texto: “En KeepCoding 
#aprendemos cómo protegernos con criptografía.” 
#¿Qué propiedad destacarías del 
#hash, atendiendo a los resultados anteriores?

#Resultado: 302be507113222694d8c63f9813727a85fef61a152176ca90edf1cfb952b19bf

import hashlib

# Texto de entrada
texto = "En KeepCoding aprendemos cómo protegernos con criptografía."

# Crear un objeto hash SHA3-256
hash_objeto = hashlib.sha3_256()

# Actualizar el objeto hash con el texto codificado en bytes
hash_objeto.update(texto.encode('utf-8'))

# Obtener el hash en formato hexadecimal
hash_hex = hash_objeto.hexdigest()

print(hash_hex)

# Datos ejercicio 5-B :

# Hcer un SHA2, y obtenemos el siguiente resultado: 4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f 6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833
import hashlib

# Texto de entrada
texto = "En KeepCoding aprendemos cómo protegernos con criptografía."

# Crear un objeto hash SHA-512
hash_objeto = hashlib.sha512()

# Actualizar el objeto hash con el texto codificado en bytes
hash_objeto.update(texto.encode('utf-8'))

# Obtener el hash en formato hexadecimal
hash_hex = hash_objeto.hexdigest()

print(hash_hex)


