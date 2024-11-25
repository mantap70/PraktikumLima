data_mahasiswa = {}

def tambah_data():
    print("\nTambah Data")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    nilai_tugas = float(input("Masukkan Nilai Tugas: "))
    nilai_uts = float(input("Masukkan Nilai UTS: "))
    nilai_uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": nilai_tugas,
        "uts": nilai_uts,
        "uas": nilai_uas,
        "akhir": nilai_akhir
    }
    print("Data berhasil ditambahkan!")

def ubah_data():
    print("\nUbah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data_mahasiswa:
        print(f"Data ditemukan untuk NIM {nim}")
        nama = input("Masukkan Nama baru: ")
        nilai_tugas = float(input("Masukkan Nilai Tugas baru: "))
        nilai_uts = float(input("Masukkan Nilai UTS baru: "))
        nilai_uas = float(input("Masukkan Nilai UAS baru: "))
        nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
        data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": nilai_tugas,
            "uts": nilai_uts,
            "uas": nilai_uas,
            "akhir": nilai_akhir
        }
        print("Data berhasil diubah!")
    else:
        print("Data tidak ditemukan!")

def hapus_data():
    print("\nHapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

def tampilkan_data():
    print("\nDaftar Nilai Mahasiswa")
    print("=" * 60)
    print(f"| {'NIM':<10} | {'NAMA':<15} | {'TUGAS':<6} | {'UTS':<6} | {'UAS':<6} | {'AKHIR':<6} |")
    print("=" * 60)
    if data_mahasiswa:
        for nim, data in data_mahasiswa.items():
            print(f"| {nim:<10} | {data['nama']:<15} | {data['tugas']:<6.2f} | {data['uts']:<6.2f} | {data['uas']:<6.2f} | {data['akhir']:<6.2f} |")
    else:
        print("TIDAK ADA DATA")
    print("=" * 60)

def cari_data():
    print("\nCari Data")
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print(f"Data ditemukan: {data}")
    else:
        print("Data tidak ditemukan!")

while True:
    print("\n[L]ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilihan: ").lower()
    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")