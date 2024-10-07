# Datos
#Firma que ha generado con la clave privada-rsa-oaep

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os

#PKCS#1 v1.5


my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"
key = RSA.importKey(open(path_file_priv).read())


# Texto --> hashear ---> "Firma" (cifrar con la privada)
mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos", "utf8")
hash=SHA256.new(mensaje_bytes)

signer = PKCS115_SigScheme(key)

signature = signer.sign(hash)
print("Firma:", binascii.hexlify(signature))

