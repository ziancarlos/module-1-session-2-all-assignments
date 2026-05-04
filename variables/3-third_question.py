hariInput = input("hari: ")
hariInput = int(hariInput)

# Diambil

# tahun = hariInput dibagi 360. terus ambil floornya misal 1.6 ya ambil 1 aja 
tahun = hariInput // 360
# tahunSisa = hariInput modulus 360. akan mengembalikan sisa hari. jika tahun sudah dieliminasi
tahunSisa = hariInput % 360

# bulan = tahunSisa dibagi 30. terus ambil floor misal 1.5 ya di ambil 1 aja.
bulan = (tahunSisa) // 30
bulanSisa = tahunSisa % 30

# minggu = bulanSisa dibagi 7 ambil nilai satuannya aja
minggu = bulanSisa // 7
mingguSisa = bulanSisa % 7

hari = mingguSisa


print(f"{tahun} tahun")
print(f"{bulan} bulan")
print(f"{minggu} minggu")
print(f"{hari} hari")
