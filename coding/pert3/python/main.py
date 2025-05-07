nim = "20240801292"

jumlah= 0
for angka in nim:
    if angka.isdigit():
        jumlah += int(angka)

        print("jumlah semua angka dalam NIM:", jumlah)