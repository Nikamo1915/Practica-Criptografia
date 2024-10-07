#Datos:
#Firma con curva Elíptica ed25519
# Instalar en python pip install ed25519

import ed25519
from Crypto.Hash import SHA256

#clave privada porque se firma
privatekey = open("ed25519-priv","rb").read()

#Se crea un objeto para firmar y adjuntamos clave privada
signedKey = ed25519.SigningKey(privatekey)


msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
#El hash es un objeto
hash=SHA256.new(msg)

#se firma el hash
signature = signedKey.sign(bytes.fromhex(hash.hexdigest()), encoding='hex')

print("Firma Generada (64 bytes):", signature)

print("Proceso para validar la firma")

publickey = open ("ed25519-publ", "rb").read()

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, bytes.fromhex(hash.hexdigest()), encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")


