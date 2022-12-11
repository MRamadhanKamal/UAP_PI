import requests
import json

# Provinsi

linkProv = "https://kodepos-2d475.firebaseio.com/list_propinsi.json"
getProv = requests.get(linkProv)
prov = getProv.json()

print('Daftar Provinsi\n')

for i in prov:
    print(prov[i])

namaProv = input("\nMasukkan Nama Provinsi\t: ")

def getKeyProv(inp):
    for key, value in prov.items():
        if inp == value:
            return key

    return "Key not found"

keyProv = getKeyProv(namaProv.title())
