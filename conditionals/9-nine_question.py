apel=input("masukkan jumlah apel: ")
jeruk=input("masukkan jumlah jeruk: ")
anggur=input("masukkan jumlah anggur: ")


print("Detail Belanja")
hasilApel = int(apel) *10000
hasilJeruk = int(jeruk) *15000
hasilAnggur = int(anggur) *20000
print(f"Apel: {apel} x 10000 = {hasilApel}")
print(f"Jeruk: {jeruk} x 10000 = {hasilJeruk}")
print(f"Anggur: {anggur} x 10000 = {hasilAnggur}")


hasilTotal = hasilApel + hasilAnggur + hasilJeruk
print(f"Total: {hasilTotal}")


jumlahUang = int(input("Masukkan jumlah uang: "))

print()
if jumlahUang < hasilTotal:
    print("Transaksi anda dibatalkan")
    print(f"Uangnya kurang sebesar {hasilTotal - jumlahUang}")
elif jumlahUang == hasilTotal:
    print("Terima kasih")
else:
    print(f"Uang kembali anda {jumlahUang - hasilTotal}")