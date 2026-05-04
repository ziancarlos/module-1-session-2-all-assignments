jamAwal = 9
a=60
b=40

jarakAwal = 120
jarakTertutup = a + b

waktu = jarakAwal / jarakTertutup

jam = waktu // 1
sisaWaktu = waktu % 1

menit = sisaWaktu * 60

print(f'{int(jamAwal + jam)}:{int(menit)}')