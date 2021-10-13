# Slip Gaji Karyawan PT DINGIN DAMAI

# Data Input Karyawan
print('PROGRAM HITUNG GAJI KARYAWAN\n\n')
nama = input('Nama Karyawan     : ')
golongan = input('Golongan Jabatan  : ')
pendidikan = input('Pendidikan        : ')

# Tunjangan Jabatan
GP = int(300000)
if golongan == '1':
    golongan1 = GP * 5/100
    tj = golongan1
elif golongan == '2':
    golongan2 = GP * 10/100
    tj = golongan2
else :
    golongan3 = GP * 15/100
    tj = golongan3

# Tunjangan Pendidikan
if pendidikan == 'SMA':
    pendidikan1 = GP * 2,5/100
    tp = pendidikan1
elif pendidikan == 'D1':
    pendidikan2 = GP * 5/100
    tp = pendidikan2
elif pendidikan == 'D3':
    pendidikan3 = GP * 20/100
    tp = pendidikan3
else :
    pendidikan4 = GP * 30/100
    tp = pendidikan4

# Honor Lembur
jam = int(input('Jumlah Jam Kerja  : '))
if jam >=9:
  lembur1 = (jam - 8) * 3500
  lembur = lembur1
else :
    lembur = int(0)


# Total Gaji
print('\n')
print(30*'=')
print('\nKaryawan yang bernama ', str(nama))
print('Honor yang diterima')
print('\tTunjangan Jabatan        Rp', int(tj))
print('\tTunjangan Pendidikan     Rp', int(tp))
print('\tHonor lembur             Rp',int(lembur))
total = GP + tp + tj + lembur
print('\t\t\t\t\t\t\t\t\t\t\t ---------  +')
print('Total Gaji                       Rp',int(total))
print('Gaji pokok + Tunjangan + Lembur')