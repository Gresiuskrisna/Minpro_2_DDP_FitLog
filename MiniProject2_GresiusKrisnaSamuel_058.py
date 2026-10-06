import os
import time
import pwinput
from prettytable import PrettyTable

# Data User
users = {
    "admin": {"password": "123", "role": "admin"},
    "samuel": {"password": "321", "role": "user"}
}

# Data Latihan 
data_latihan = {
    "EX01": {"nama": "Bench Press", "kategori": "Dada", "target": "4 x 10", "beban": 40},
    "EX02": {"nama": "Barbell Squat", "kategori": "Kaki", "target": "3 x 12", "beban": 50}
}

def tampilkan_tabel(data_dict):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Latihan", "Kategori", "Target", "Beban"]
    for id_latihan, isi in data_dict.items():
        tabel.add_row([id_latihan, isi["nama"], isi["kategori"], isi["target"], f"{isi['beban']} kg"])
    print(tabel)

def menu_admin():
    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print("=== MENU ADMIN FITLOG ===")
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Logout")

        # Error handling 
        pilih_input = input("Pilih menu (1-5): ")
        if not pilih_input.isdigit():
            print("Error: Harus masukin angka!")
            time.sleep(1)
            continue
            
        pilih = int(pilih_input)

        if pilih == 1:
            print("\n===== DAFTAR LATIHAN =====")
            if len(data_latihan) == 0:
                print("Data kosong.")
            else:
                tampilkan_tabel(data_latihan)
            input("\nTekan Enter buat kembali...")

        elif pilih == 2:
            print("\n===== TAMBAH DATA =====")
            id_baru = input("ID Latihan baru: ").upper()
            if id_baru in data_latihan:
                print("ID udah ada!")
                time.sleep(1)
                continue

            nama = input("Nama Latihan: ")
            kategori = input("Kategori: ")
            target = input("Target (contoh 4x10): ")

            # Error handling beban
            while True:
                beban_input = input("Beban (kg): ")
                if beban_input.isdigit():
                    beban = int(beban_input)
                    break
                print("Error: Beban harus pake angka!")
                
            data_latihan[id_baru] = {"nama": nama, "kategori": kategori, "target": target, "beban": beban}
            print("Data berhasil ditambah.")
            time.sleep(1)

        elif pilih == 3:
            print("\n===== UBAH DATA =====")
            if len(data_latihan) == 0:
                print("Data kosong.")
                time.sleep(1)
                continue
                
            tampilkan_tabel(data_latihan)
            id_ubah = input("Masukkan ID yang mau diubah: ").upper()

            if id_ubah in data_latihan:
                print("(Kosongkan lalu tekan Enter kalau nilai lama tidak mau diubah)")
                nama_baru = input(f"Nama Latihan ({data_latihan[id_ubah]['nama']}): ")
                if nama_baru == "":
                    nama_baru = data_latihan[id_ubah]['nama']

                kategori_baru = input(f"Kategori ({data_latihan[id_ubah]['kategori']}): ")
                if kategori_baru == "":
                    kategori_baru = data_latihan[id_ubah]['kategori']

                target_baru = input(f"Target ({data_latihan[id_ubah]['target']}): ")
                if target_baru == "":
                    target_baru = data_latihan[id_ubah]['target']

                while True:
                    beban_baru_input = input(f"Beban kg ({data_latihan[id_ubah]['beban']}): ")
                    if beban_baru_input == "":
                        beban_baru = data_latihan[id_ubah]['beban']
                        break
                    elif beban_baru_input.isdigit():
                        beban_baru = int(beban_baru_input)
                        break
                    print("Error: Beban harus pake angka!")

                data_latihan[id_ubah] = {"nama": nama_baru, "kategori": kategori_baru, "target": target_baru, "beban": beban_baru}
                print("Data berhasil diupdate.")
            else:
                print("ID tidak ketemu.")
            time.sleep(1)

        elif pilih == 4:
            print("\n===== HAPUS DATA =====")
            id_hapus = input("Masukkan ID yang mau dihapus: ").upper()
            if id_hapus in data_latihan:
                yakin = input(f"yakin mau hapus {data_latihan[id_hapus]['nama']}? (y/n): ")
                if yakin.lower() == 'y':
                    del data_latihan[id_hapus]
                    print("Data berhasil dihapus.")
                else:
                    print("Batal hapus.")
            else:
                print("ID tidak ketemu.")
            time.sleep(1)

        elif pilih == 5:
            print("Logout dari Admin...")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak ada.")
            time.sleep(1)

def menu_user():
    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print("=== MENU USER FITLOG ===")
        print("1. Lihat Daftar Latihan")
        print("2. Cari Berdasarkan Kategori")
        print("3. Logout")

        pilih_input = input("Pilih menu (1-3): ")
        if not pilih_input.isdigit():
            print("Error: Harus masukin angka!")
            time.sleep(1)
            continue
            
        pilih = int(pilih_input)

        if pilih == 1:
            if len(data_latihan) == 0:
                print("Data kosong.")
            else:
                tampilkan_tabel(data_latihan)
            input("\nTekan Enter buat kembali...")

        elif pilih == 2:
            cari = input("Masukkan kategori otot (misal: Dada): ").lower()
            ada_hasil = False
            
            tabel_cari = PrettyTable()
            tabel_cari.field_names = ["ID", "Nama Latihan", "Kategori", "Target", "Beban"]

            for id_latihan, isi in data_latihan.items():
                if cari in isi["kategori"].lower():
                    tabel_cari.add_row([id_latihan, isi["nama"], isi["kategori"], isi["target"], f"{isi['beban']} kg"])
                    ada_hasil = True

            if ada_hasil:
                print("\nHasil Pencarian:")
                print(tabel_cari)
            else:
                print("Kategori tidak ditemukan.")
            input("\nTekan Enter buat kembali...")

        elif pilih == 3:
            print("Logout dari User...")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak ada.")
            time.sleep(1)

# PROGRAM UTAMA
while True:
    os.system("clear" if os.name != "nt" else "cls")
    print("=== LOGIN FITLOG ===")
    print("1. Login Aplikasi")
    print("2. Keluar")

    menu_awal_input = input("Pilih (1/2): ")
    if not menu_awal_input.isdigit():
        print("Error: Input harus pake angka!")
        time.sleep(1)
        continue
        
    menu_awal = int(menu_awal_input)

    if menu_awal == 1:
        username = input("Username: ").lower()
        password = pwinput.pwinput("Password: ") 

        # Cek login  
        if username in users and users[username]["password"] == password:
            print(f"Login sukses! Halo {username}.")
            time.sleep(1)
            
            role_nya = users[username]["role"]
            if role_nya == "admin":
                menu_admin()
            elif role_nya == "user":
                menu_user()
        else:
            print("Username atau password salah!")
            time.sleep(1)

    elif menu_awal == 2:
        print("Program dihentikan.")
        break
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)
