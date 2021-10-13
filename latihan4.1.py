# Pendaftaran Mahasiswa Baru

# Input data
nama = input('Masukkan Nama                  : ')
nis = input('Masukkan NIS                   : ')
jurusan = input('Masukkan Kode Jurusan [SI/SIA] : ')

# Proses
if jurusan == 'SI':
    namaprodi = 'Sistem Informasi'
    harga = 2400000
else :
    namaprodi = 'Sistem Informasi Akuntansi'
    harga = 2000000

# Cetak Hasil
print(30*'-')
print('Pendaftaran Mahasiswa Baru')
print(30*'-')
print('Nama         : ', str(nama))
print('NIS          : ', str(nis))
print('Jurusan      : ', str(namaprodi))
print('Jumlah bayar : ', str(harga))