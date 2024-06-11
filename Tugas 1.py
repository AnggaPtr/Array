class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

class Barang:
    def __init__(self, nama, kode, jumlah):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah

class Transaksi:
    def __init__(self, tipe, deskripsi, jumlah):
        self.tipe = tipe  # 'pemasukan' atau 'pengeluaran'
        self.deskripsi = deskripsi
        self.jumlah = jumlah

# Fungsi untuk kasus Mahasiswa
def input_mahasiswa():
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    prodi = input("Masukkan Prodi: ")
    nilai = float(input("Masukkan Nilai: "))
    return Mahasiswa(nama, nim, prodi, nilai)

def tampilkan_mahasiswa(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    for m in mahasiswa_list:
        print(f"Nama: {m.nama}, NIM: {m.nim}, Prodi: {m.prodi}, Nilai: {m.nilai}")

def hitung_rata_rata(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    total_nilai = sum(m.nilai for m in mahasiswa_list)
    rata_rata = total_nilai / len(mahasiswa_list)
    print(f"Rata-rata Nilai: {rata_rata:.2f}")

def cari_mahasiswa_tertinggi_terendah(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    tertinggi = max(mahasiswa_list, key=lambda m: m.nilai)
    terendah = min(mahasiswa_list, key=lambda m: m.nilai)
    print(f"Mahasiswa dengan Nilai Tertinggi: {tertinggi.nama}, Nilai: {tertinggi.nilai}")
    print(f"Mahasiswa dengan Nilai Terendah: {terendah.nama}, Nilai: {terendah.nilai}")

# Fungsi untuk kasus Barang
def input_barang():
    nama = input("Masukkan Nama Barang: ")
    kode = input("Masukkan Kode Barang: ")
    jumlah = int(input("Masukkan Jumlah Barang: "))
    return Barang(nama, kode, jumlah)

def tampilkan_barang(barang_list):
    if not barang_list:
        print("Tidak ada data barang.")
        return
    for b in barang_list:
        print(f"Nama: {b.nama}, Kode: {b.kode}, Jumlah: {b.jumlah}")

def cari_barang_berdasarkan_kode(barang_list, kode):
    barang = next((b for b in barang_list if b.kode == kode), None)
    if barang:
        print(f"Ditemukan - Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")
    else:
        print("Barang tidak ditemukan.")
    return barang

def hapus_barang_berdasarkan_kode(barang_list, kode):
    barang = cari_barang_berdasarkan_kode(barang_list, kode)
    if barang:
        barang_list.remove(barang)
        print(f"Barang dengan kode {kode} telah dihapus.")

# Fungsi untuk kasus Keuangan Pribadi
def input_transaksi():
    tipe = input("Masukkan Tipe (pemasukan/pengeluaran): ").strip().lower()
    deskripsi = input("Masukkan Deskripsi: ")
    jumlah = float(input("Masukkan Jumlah: "))
    return Transaksi(tipe, deskripsi, jumlah)

def tampilkan_transaksi(transaksi_list):
    if not transaksi_list:
        print("Tidak ada transaksi.")
        return
    for t in transaksi_list:
        print(f"{t.tipe.capitalize()}: {t.deskripsi} - {t.jumlah}")

def hitung_total(transaksi_list, tipe):
    return sum(t.jumlah for t in transaksi_list if t.tipe == tipe)

def hitung_saldo_akhir(transaksi_list):
    total_pemasukan = hitung_total(transaksi_list, 'pemasukan')
    total_pengeluaran = hitung_total(transaksi_list, 'pengeluaran')
    return total_pemasukan - total_pengeluaran

# Menu utama untuk memilih kasus studi
def main():
    mahasiswa_list = []
    barang_list = []
    transaksi_list = []

    while True:
        print("\nMenu Utama:")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Inventaris Barang")
        print("3. Kelola Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            submenu_mahasiswa(mahasiswa_list)
        elif pilihan == '2':
            submenu_barang(barang_list)
        elif pilihan == '3':
            submenu_keuangan(transaksi_list)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def submenu_mahasiswa(mahasiswa_list):
    while True:
        print("\nMenu Mahasiswa:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Hitung Rata-rata Nilai")
        print("4. Cari Mahasiswa dengan Nilai Tertinggi dan Terendah")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            mahasiswa_list.append(input_mahasiswa())
        elif pilihan == '2':
            tampilkan_mahasiswa(mahasiswa_list)
        elif pilihan == '3':
            hitung_rata_rata(mahasiswa_list)
        elif pilihan == '4':
            cari_mahasiswa_tertinggi_terendah(mahasiswa_list)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def submenu_barang(barang_list):
    while True:
        print("\nMenu Barang:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang Berdasarkan Kode")
        print("4. Hapus Barang Berdasarkan Kode")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            barang_list.append(input_barang())
        elif pilihan == '2':
            tampilkan_barang(barang_list)
        elif pilihan == '3':
            kode = input("Masukkan Kode Barang: ")
            cari_barang_berdasarkan_kode(barang_list, kode)
        elif pilihan == '4':
            kode = input("Masukkan Kode Barang: ")
            hapus_barang_berdasarkan_kode(barang_list, kode)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def submenu_keuangan(transaksi_list):
    while True:
        print("\nMenu Keuangan:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Total Pemasukan")
        print("4. Total Pengeluaran")
        print("5. Saldo Akhir")
        print("6. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            transaksi_list.append(input_transaksi())
        elif pilihan == '2':
            tampilkan_transaksi(transaksi_list)
        elif pilihan == '3':
            print(f"Total Pemasukan: {hitung_total(transaksi_list, 'pemasukan'):.2f}")
        elif pilihan == '4':
            print(f"Total Pengeluaran: {hitung_total(transaksi_list, 'pengeluaran'):.2f}")
        elif pilihan == '5':
            print(f"Saldo Akhir: {hitung_saldo_akhir(transaksi_list):.2f}")
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()