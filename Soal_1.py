data_mahasiswa = []

while True:
    nim = input("Masukkan NIM mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ")
    
    mahasiswa = {'Nama': nama, 'NIM': nim}
    data_mahasiswa.append(mahasiswa)
    
    lagi = input("Apakah ingin memasukkan data mahasiswa lain? (y/n): ")
    if lagi.lower() != 'y':
        break

print("\nData Mahasiswa:")
for mahasiswa in data_mahasiswa:
    print(f"Nama: {mahasiswa['Nama']}, NIM: {mahasiswa['NIM']}")
