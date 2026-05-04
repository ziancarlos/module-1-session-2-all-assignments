print("=== Kalkulator Profil Produk ===")

produk = input("Masukkan nama produk: ")
harga = int(input("Masukkan harga satuan produk: "))
jumlah = int(input("Masukkan jumlah produk yang dibeli: "))
diskon = int(input("Masukkan diskon (dalam persen): "))

# Format nama produk
nama_format = produk.upper()

# Hitung total sebelum diskon
total = harga * jumlah

# Hitung besar diskon
nilai_diskon = total * diskon / 100

# Hitung total akhir
total_akhir = total - nilai_diskon

# Cetak hasil
print("Produk:", nama_format)
print("Total sebelum diskon: Rp", total)
print("Diskon: Rp", nilai_diskon)
print("Total yang harus dibayar: Rp", total_akhir)