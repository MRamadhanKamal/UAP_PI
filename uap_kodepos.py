import requests
import json
import os

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


while(True):
    os.system('cls')
    listMenu = ["1. Cari Kode Pos", "2. Credits", "3. Keluar"]
    print("\t ~~~~KATALOG KODE POS~~~~\n\n")
    print("Menu Katalog Kode Pos")
    print("\t",listMenu[0])
    print("\t",listMenu[1])
    print("\t",listMenu[2])
    while(True):
        try:
            pilih = int(input("masukkan pilihan: "))
            break
        except (TypeError, ValueError):
            print("Invalid Input")
            x = input()
