# Muhammad Fa'iz
# NIM 2309116086

print("=" * 44)
print("APLIKASI KONVERSI SATUAN MASSA KILOGRAM (kg)")
print("=" * 44)


def satuan_konversi():
    print("1.POUNDS (lb)")
    print("2.OUNCE (ons)")
    print("3.GRAM (g)")


print('')
print("SEBELUM MEMULAI SILAHKAN MEMASUKKAN NAMA DAN NIM")
print('')
nama = str(input("Masukkan nama: "))
nim = int(input("Masukkan NIM: "))
print('')
print("Nama: ", nama)
print("NIM: ", nim)
print('')
input_data = str(input("APAKAH DATA YANG DIMASUKKAN SUDAH BENAR? (Y/N): "))
data_benar = "y"
data_salah = "n"


def konversipounds():
    print('')
    massa_awal = int(
        input("SILAHKAN MASUKKAN MASSA KILOGRAM (KG) YANG INGIN ANDA KONVERSI: "))
    satuan_konversi()
    print('')
    pilihan_konversi = int(input("PILIHAN KONVERSI (1/2/3): "))
    if pilihan_konversi == 1:
        hasil_konversi_pounds = massa_awal * 2.204523
        print('')
        print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA POUNDS (lb) ADALAH :",
              hasil_konversi_pounds, "lb")
        print('')
        restart_program = str(
            input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
        if restart_program == "y":
            konversipounds()
        elif restart_program == "n":
            raise SystemExit
    elif pilihan_konversi == 2:
        hasil_konversi_ounce = massa_awal * 35.274
        print('')
        print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA OUNCE (ons) ADALAH :",
              hasil_konversi_ounce, "ons")
        print('')
        restart_program = str(
            input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
        if restart_program == "y":
            konversipounds()
        elif restart_program == "n":
            raise SystemExit
    elif pilihan_konversi == 3:
        hasil_konversi_gram = massa_awal * 1000
        print('')
        print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA GRAM (g)) ADALAH :",
              hasil_konversi_gram, "g")
        print('')
        restart_program = str(
            input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
        if restart_program == "y":
            konversipounds()
        elif restart_program == "n":
            raise SystemExit
    else:
        print('')
        print("DATA YANG ANDA MASUKKAN TIDAK VALID")
        raise SystemExit


while True:
    if input_data == "y":
        print('')
        massa_awal = int(
            input("SILAHKAN MASUKKAN MASSA KILOGRAM (KG) YANG INGIN ANDA KONVERSI: "))
        satuan_konversi()
        print('')
        pilihan_konversi = int(input("PILIHAN KONVERSI (1/2/3): "))
        if pilihan_konversi == 1:
            hasil_konversi_pounds = massa_awal * 2.204523
            print('')
            print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA POUNDS (lb) ADALAH :",
                  hasil_konversi_pounds, "lb")
            print('')
            restart_program = str(
                input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
            if restart_program == "y":
                konversipounds()
            elif restart_program == "n":
                break
        elif pilihan_konversi == 2:
            hasil_konversi_ounce = massa_awal * 35.274
            print('')
            print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA OUNCE (ons) ADALAH :",
                  hasil_konversi_ounce, "ons")
            print('')
            restart_program = str(
                input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
            if restart_program == "y":
                konversipounds()
            elif restart_program == "n":
                break
        elif pilihan_konversi == 3:
            hasil_konversi_gram = massa_awal * 1000
            print('')
            print("HASIL KONVERSI MASSA KILOGRAM (kg) ANDA KE MASSA GRAM (g)) ADALAH :",
                  hasil_konversi_gram, "g")
            print('')
            restart_program = str(
                input("APAKAH ANDA INGIN MENGKONVERSI ULANG?: (Y/N): "))
            if restart_program == "y":
                konversipounds()
            elif restart_program == "n":
                break
        else:
            print('')
            print("DATA YANG ANDA MASUKKAN TIDAK VALID")
            break
    elif input_data == "n":
        print("SILAHKAN MASUKKAN ULANG NAMA DAN NIM")
        print('')
        nama = str(input("Masukkan nama: "))
        nim = int(input("Masukkan NIM: "))
        print('')
        input_data = str(
            input("APAKAH DATA YANG DIMASUKKAN SUDAH BENAR? (Y/N): "))

    else:
        print('')
        print("DATA YANG ANDA MASUKKAN TIDAK VALID")
        break
