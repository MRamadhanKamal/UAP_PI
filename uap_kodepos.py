import requests
import json
 
# Provinsi
 
linkProv = "https://kodepos-2d475.firebaseio.com/list_propinsi.json"
getProv = requests.get(linkProv)
prov = getProv.json()

print('Daftar Provinsi\n')

for i in prov:
    print(prov[i])

class Provinsi:
    def __init__(self, namaProv):
        self.namaProv = namaProv
        self.linkProv = linkProv
        self.getProv = getProv
        self.prov = prov
 
    def getKeyProv(self):
        for key, value in self.prov.items():
            if self.namaProv == value:
                return key
 
        return "Key not found"
 
namaProv1 = input("\nMasukkan Nama Provinsi\t: ")
prov1 = Provinsi(namaProv1.title())
prov1.getKeyProv()
keyProv = prov1.getKeyProv()
