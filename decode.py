import string
import hashlib
import json
from pip._vendor import requests
import sys

with open('answer.json', 'r') as answer:
    data = json.loads(answer.read())
    cifrado = data['cifrado']
    key = data['numero_casas']
    token = data['token']

alphabet = string.ascii_lowercase # alfabeto

def Desencriptar():

    encrypted_message = cifrado.strip()
    print()
    chave = int(key)

    decrypted_message = ""

    for i in encrypted_message:

        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position - chave) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += i

    with open('answer.json', 'r') as answer:
      data=json.load(answer)

    data['decifrado'] = decrypted_message



    with open('answer.json', 'w') as answer:
      json.dump(data, answer)

    print(decrypted_message)

Desencriptar()



with open('answer.json', 'r') as answer:
    data = json.load(answer)

resumo = hashlib.sha1(data['decifrado'].encode('utf-8')).hexdigest()
data['resumo_criptografico'] = resumo

with open('answer.json', 'w') as answer:
    json.dump(data, answer)

