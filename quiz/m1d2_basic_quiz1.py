# Lengkapilah program berikut ini untuk menghitung total gaji harian seorang pegawai berdasarkan:
# - Nama pegawai
# - Jumlah jam kerja
# - Tarif per jam
# 
# Program juga harus membuat ID pegawai otomatis berdasarkan inisial nama dan total jam kerja.


print("=== Program Kalkulator Gaji Harian ===")

# TODO: Ambil input nama pegawai
nama = input("Nama pegawai: ")

# TODO: Ambil input jumlah jam kerja (int)
jam_kerja = int(input("Jam kerja pegawai: "))

# TODO: Ambil input tarif per jam (float)
tarif_per_jam = int(float(" input tarif per jam (float): "))

# TODO: Hitung total gaji
total_gaji = jam_kerja * tarif_per_jam

# TODO: Buat ID pegawai dari 3 huruf pertama nama + jam kerja
id_pegawai = nama+jam_kerja

# TODO: Tampilkan hasil
print("ID Pegawai :", id_pegawai)
print("Nama       :", nama)
print("Total Gaji : Rp", total_gaji)
