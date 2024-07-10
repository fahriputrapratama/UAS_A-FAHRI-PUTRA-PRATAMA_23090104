# Data mahasiswa
data_mahasiswa = [
    ["Nama", "Algoritma dan struktur data", "matematika numerik"],
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]

# Menghitung rata-rata nilai tiap mata kuliah
total_algoritma = 0
total_matematika = 0
jumlah_mahasiswa = len(data_mahasiswa) - 1  

for mahasiswa in data_mahasiswa[1:]:
    total_algoritma += mahasiswa[1]
    total_matematika += mahasiswa[2]

rata_rata_algoritma = total_algoritma / jumlah_mahasiswa
rata_rata_matematika = total_matematika / jumlah_mahasiswa

# Menghitung rata-rata nilai tiap mahasiswa
rata_rata_mahasiswa = []
for mahasiswa in data_mahasiswa[1:]:
    rata_rata = (mahasiswa[1] + mahasiswa[2]) / 2
    rata_rata_mahasiswa.append([mahasiswa[0], rata_rata])

# Tampilkan data dan rata-rata
print("Data Mahasiswa:")
for mahasiswa in data_mahasiswa:
    print(mahasiswa)

print("\nRata-rata Nilai Tiap Mata Kuliah:")
print(f"Algoritma dan struktur data: {rata_rata_algoritma}")
print(f"Matematika numerik: {rata_rata_matematika}")

print("\nRata-rata Nilai Tiap Mahasiswa:")
for mahasiswa in rata_rata_mahasiswa:
    print(f"{mahasiswa[0]}: {mahasiswa[1]}")