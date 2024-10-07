#Ejercicio 4
#Datos:
#jwt:clave es “Con KeepCoding aprendemos
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSB
#sb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0
#dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE

#Resultado:
#Algoritmo de firma: El HS256 (HMAC con SHA-256)
#Body del jwt:
#{
  #"usuario": "Don Pepito de los palotes",
 # "rol": "isNormal",
  #"iat": 1667933533
#}

import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"
secret = "Con KeepCoding aprendemos"

try:
    decoded = jwt.decode(token, secret, algorithms=["HS256"])
    print(decoded)
except jwt.InvalidTokenError:
    print("Token inválido")
