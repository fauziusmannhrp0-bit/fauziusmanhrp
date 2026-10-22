# INPUT
tugas = float(input("Masukkan nilai Tugas\t: "))
uts = float(input("Masukkan nilai UTS\t: "))
uas = float(input("Masukkan nilai UAS\t: "))
kehadiran = float(input("Masukkan kehadiran\t: "))

# PROSES
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# OUTPUT
print("\nNilai Akhir\t\t:", nilai_akhir)

# KONDISI
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status\t\t\t: Lulus Dengan Predikat")

elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status\t\t\t: Lulus")

else:
    print("Status\t\t\t: Tidak Lulus")