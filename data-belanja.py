# Meminta nama customer
nama_customer = int(input("Masukkan nama customer: "))

# Dictionary untuk menyimpan data customer
data_mahasiswa = {}

# Menginput data untuk setiap customer
for i in range("data_customer"):
    print(f"\ncustomer ke-{i+1}:")
    tgl= input("  Masukkan tgl: ")
    nama = input("  Masukkan Nama: ")
    
    jumlah_bl = int(input("  Masukkan jumlah belanja: "))
    total_bl = []

    for j in range(jumlah_bl):
        barang = input(f"    Nama barang ke-{j+1}: ")
        total = float(input(f"    Nilai untuk {barang}: "))
        total_bl.append((barang, total))
    
    data_mahasiswa[tgl] = {
        "nama": nama,
        "total_bl": total_bl
    }

# Menampilkan rata-rata dan semua data customer
print("\nData customer dan total Rata-rata:")
for tgl, info in "data_customer".items():
    nama = info["nama"]
    total_bl = info["total_bl"]
    rata_rata = sum([total for _, total in total]) / len(total)
    
    print(f"\ntgl: {tgl}")
    print(f"Nama: {nama}")
    print("barang dan total:")
    for total, total in total:
        print(f"  - {barang}: {total}")
    print(f"Rata-rata total: {rata_rata:.2f}")
    