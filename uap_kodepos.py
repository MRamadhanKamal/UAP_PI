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

# Kota/Kabupaten
 
linkKota = "https://kodepos-2d475.firebaseio.com/list_kotakab/"+keyProv+".json"
hasilKota = requests.get(linkKota)
kota = hasilKota.json()

print('\nDaftar Kota/Kabupaten\n')

for i in kota:
    print(kota[i])
 
class Kota:
    def __init__(self, namaKota):
        self.namaKota = namaKota
        self.linkKota = linkKota
        self.hasilKota = hasilKota
        self.kota = kota
 
    def getKeyKota(self):
        for key, value in self.kota.items():
            if self.namaKota == value:
                return key
 
        return "Key not found"
 
namaKota1 = input("\nMasukkan Nama Kota\t: ")
kota1 = Kota(namaKota1.title())
kota1.getKeyKota()
keyKota = kota1.getKeyKota()

# Kecamatan/Kelurahan
 
linkPos = "https://kodepos-2d475.firebaseio.com/kota_kab/"+keyKota+".json"
hasilPos = requests.get(linkPos)
pos = hasilPos.json()

print('\nDaftar Kecamatan/Kelurahan\n')

for i in pos:
    print('Kecamatan\t:', i['kecamatan'], '\nKelurahan\t:', i['kelurahan'], '\n')

class Pos:
    def __init__(self, namaLurah):
        self.namaLurah = namaLurah
        self.linkPos = linkPos
        self.hasilPos = hasilPos
        self.pos = pos
 
    def getKeyPos(self):
        for i in pos:
            if self.namaLurah == i['kelurahan']:
                print('\nKecamatan\t:', i['kecamatan'], '\nKelurahan\t:', i['kelurahan'], 
                '\nKode Pos\t:', i['kodepos'], '\n')
                f = open("history.txt", "a")
                f.write("\nKecamatan\t:"+ i['kecamatan']+ "\nKelurahan\t:"+ i['kelurahan']+"\nKode Pos\t:"+ i['kodepos']+ "\n")
                f.close()
 
namaLurah1 = input("Masukkan Nama Kelurahan\t: ")
pos1 = Pos(namaLurah1.title())
pos1.getKeyPos()
