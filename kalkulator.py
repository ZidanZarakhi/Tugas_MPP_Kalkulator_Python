def tambah(num1, num2):
    return num1 + num2

def kurang(num1, num2):
    return num1 - num2

def kali(num1, num2):
    return num1 * num2

def bagi(num1, num2):
    if num2 == 0:
        return "Error (Tidak bisa dibagi dengan nol)"
    return num1 / num2


def ambil_input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.\n")


num1 = ambil_input_angka("Masukan Angka Pertama: ")
num2 = ambil_input_angka("Masukan Angka Kedua: ")

kalkulator_on = True
hasil = 0

while kalkulator_on:
    while True:
        pilih_operator = input("Pilih Operator ('+', '-', '*', '/') atau 'q' untuk keluar: ").lower()
        if pilih_operator in ["+", "-", "*", "/", "q"]:
            break 
        print("Operator tidak valid! Masukkan ('+', '-', '*', '/') atau 'q'\n")

    # Langsung keluar jika memilih 'q'
    if pilih_operator == "q":
        print("Terima kasih telah menggunakan kalkulator!")
        break

    # Eksekusi operasi aritmatika
    if pilih_operator == "+":
        hasil = tambah(num1, num2)
        print(f"Hasil dari Pertambahan {num1} + {num2} = {hasil}")
    elif pilih_operator == "-":
        hasil = kurang(num1, num2)
        print(f"Hasil dari Pengurangan {num1} - {num2} = {hasil}")
    elif pilih_operator == "*":
        hasil = kali(num1, num2)
        print(f"Hasil dari Perkalian {num1} * {num2} = {hasil}")
    elif pilih_operator == "/":
        hasil = bagi(num1, num2)
        print(f"Hasil dari Pembagian {num1} / {num2} = {hasil}")

    print("\n===========================================\n")

    while True:
        lanjut_kalkulasi = input(f"Apakah angka {hasil} mau dilanjutkan untuk kalkulasi? ('y'/'n'): ").lower()
        if lanjut_kalkulasi in ["y", "n"]:
            break
        print("Pilihan tidak valid! Tolong masukkan 'y' atau 'n'.\n")

    if lanjut_kalkulasi == "y":
        num1 = hasil
        print(f"Angka 1: {num1}")
        num2 = ambil_input_angka("Masukan Angka Kedua: ")
    else:
        keluar_kalkulator = input("Apakah ingin keluar dari kalkulator? ('y'/'n'): ").lower()
        if keluar_kalkulator == "y":
            print("Terima kasih telah menggunakan kalkulator!")
            break
        else:
            num1 = ambil_input_angka("Masukan Angka Pertama Baru: ")
            num2 = ambil_input_angka("Masukan Angka Kedua Baru: ")
