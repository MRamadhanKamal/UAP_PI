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

# Kota/Kabupaten

linkKota = "https://kodepos-2d475.firebaseio.com/list_kotakab/"+keyProv+".json"
hasilKota = requests.get(linkKota)
kota = hasilKota.json()

print('\nDaftar Kota/Kabupaten\n')

for i in kota:
    print(kota[i])

namaKota = input("\nMasukkan Nama Kota\t: ")
print()

def getKeyKota(inp):
    for key, value in kota.items():
        if inp == value:
            return key

    return "Key not found"

keyKota = getKeyKota(namaKota.title())
