nama = input("Nama lengkap: ").strip()
usia = int(input("Usia: "))
jumlahTransaksi = int(input("Jumlah transaksi dalam sebulan: "))
totalBelanjaRp = int(input("Total belanja dalam rupiah: "))

pernahKomplain = input("Apakah pernah komplain bulan ini (ya/tidak): ").strip().lower()
jenisKelamin = input("Jenis kelamin (laki/perempuan): ").strip().lower()
perangkat = input("Perangkat (mobile/web): ").strip().lower()
kategori = input("Kategori favorit (fashion/elektronik/kebutuhan rumah): ").strip().lower()


isValid = True

if pernahKomplain not in ["ya", "tidak"]:
    isValid = False

if jenisKelamin not in ["laki", "perempuan"]:
    isValid = False

if perangkat not in ["mobile", "web"]:
    isValid = False

if kategori not in ["fashion", "elektronik", "kebutuhan rumah"]:
    isValid = False

if not isValid:
    print("Input tidak valid")
else:
    totalBelanjaJuta = totalBelanjaRp / 1000000

    inisial = nama.split()[0][0].upper()
    idPelanggan = f"{inisial}{usia}{perangkat}"

    if usia < 25:
        segmenUsia = "Gen Z"
    elif usia <= 40:
        segmenUsia = "Millennial"
    else:
        segmenUsia = "Mature Customer"

    if jumlahTransaksi >= 10:
        frekuensi = "High Frequency"
    elif jumlahTransaksi >= 5:
        frekuensi = "Medium Frequency"
    else:
        frekuensi = "Low Frequency"

    if totalBelanjaJuta >= 3:
        nilai = "Platinum"
    elif totalBelanjaJuta >= 1:
        nilai = "Gold"
    else:
        nilai = "Silver"

    if perangkat == "mobile":
        if kategori == "fashion":
            preferensi = "Mobile Fashion Enthusiast"
        elif kategori == "elektronik":
            preferensi = "Mobile Tech Hunter"
        else:
            preferensi = "Mobile Shopper"
    elif perangkat == "web":
        if kategori == "elektronik":
            preferensi = "Tech Savvy Web User"
        else:
            preferensi = "Web Explorer"
    else:
        preferensi = "General User"

    if nilai == "Platinum" and frekuensi == "High Frequency" and pernahKomplain == "tidak":
        target = "YA"
    else:
        target = "TIDAK"

    print(f"ID Pelanggan: {idPelanggan}")
    print(f"Nama: {nama}")
    print(f"Usia: {usia} ({segmenUsia})")
    print(f"Jenis Kelamin: {jenisKelamin}")
    print(f"Total Belanja: Rp {totalBelanjaRp:,} ({totalBelanjaJuta:.2f} juta)")
    print(f"Frekuensi Transaksi: {frekuensi}")
    print(f"Nilai Pelanggan: {nilai}")
    print(f"Segmen Preferensi: {preferensi}")
    print(f"Target Kampanye: {target}")

    if nilai == "Silver" and jumlahTransaksi <= 1:
        print("Peringatan: Pelanggan pasif")