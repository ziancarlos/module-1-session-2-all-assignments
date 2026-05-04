massa = int(input("Masukkan Massa (kg): "))
tinggiCm = int(input("Masukkan Tinggi (cm): "))
tinggiCm = tinggiCm/100

imt = massa/tinggiCm**2

if imt < 18.7:
    print(f"{imt}, BERAT BADAN KURANG!")
elif imt >=18.5 and imt <=24.9:
    print(f"{imt}, BERAT BADAN IDEAL!")
elif imt >=25.0 and imt <=29.9:
    print(f"{imt}, BERAT BADAN BERLEBIH!")
elif imt >=30.0 and imt <=39.9:
    print(f"{imt}, BERAT BADAN SANGAT BERLEBIH!")
else:
    print(f"{imt}, BERAT BADAN OBESITAS!")

