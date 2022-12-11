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
# Kecamatan/Kelurahan

linkPos = "https://kodepos-2d475.firebaseio.com/kota_kab/"+keyKota+".json"
hasilPos = requests.get(linkPos)
pos = hasilPos.json()

print('\nDaftar Kecamatan/Kelurahan\n')

for i in pos:
    print('Kecamatan\t:', i['kecamatan'], '\nKelurahan\t:', i['kelurahan'], '\n')

namaLurah = input("Masukkan Nama Kelurahan\t: ")

def getKodePos(inp):
    for i in pos:
        if inp == i['kelurahan']:
            print('Kecamatan\t:', i['kecamatan'], '\nKelurahan\t:', i['kelurahan'], 
            '\nKode Pos\t:', i['kodepos'], '\n')

getKodePos(namaLurah.title())

