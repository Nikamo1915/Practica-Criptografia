#Datos:
#Generar clave AES usando HKDF con un SHA-512
#Clave maestra A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72
#Valor hexadecimal e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3

#Resultado: Clave??
#Clave derivada 1: e2a1f58fffb8bf7188e46d88141cd0d4eef55293a1c6719b1546a0d98013521d
#Clave derivada 2: 135482591993f53019660241a98f3812b57f13c7bfd9d35a59e6905b3e2e3456

from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets


salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

#salt = secrets.token_bytes(16)
#print(salt.hex())



master_secret = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

key1 = HKDF(master_secret, 16, salt, SHA512, 1)

print("Clave key1: ", key1.hex())

