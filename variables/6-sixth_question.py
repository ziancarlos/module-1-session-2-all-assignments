apel=input("masukkan jumlah apel: ")
jeruk=input("masukkan jumlah jeruk: ")
anggur=input("masukkan jumlah anggur: ")

hasilApel = int(apel) *10000
hasilJeruk = int(jeruk) *15000
hasilAnggur = int(anggur) *20000

print("Detail Belanja")
print(f"Apel: {apel} x 10000 = {hasilApel}")
print(f"Jeruk: {jeruk} x 10000 = {hasilJeruk}")
print(f"Anggur: {anggur} x 10000 = {hasilAnggur}")


hasilTotal = hasilApel + hasilAnggur + hasilJeruk
print(f"Total: {hasilTotal}")