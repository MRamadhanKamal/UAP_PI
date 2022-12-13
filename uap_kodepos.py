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

    if pilih == 1:
        # Provinsi
        linkProv = "https://kodepos-2d475.firebaseio.com/list_propinsi.json"
        getProv = requests.get(linkProv)
        prov = getProv.json()

        print('Daftar Provinsi\n')

        for i in prov:
            print(prov[i])

        namaProv1 = input("\nMasukkan Nama Provinsi\t: ")
        prov1 = Provinsi(namaProv1.title())
        prov1.getKeyProv()
        keyProv = prov1.getKeyProv()
