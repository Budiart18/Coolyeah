print('''GEROBAK FRIED CHICKEN
----------------------------------
Kode    Jenis Potong    Harga
D       Dada            Rp. 2500
P       Paha            Rp. 2000
S       Sayap           Rp. 1500
----------------------------------
\n''')

ayam = int(input('Banyak Jenis : '))

#input
listkode = []
listbanyak = []
for i in range(ayam):
    print('Jenis ke- ', i+1)
    kode = input('Kode potong [D/P/S] : ')
    listkode.append(kode)
    banyak = int(input('Banyak potong : '))
    listbanyak.append(banyak)

#output
print('\n\nGEROBAK FRIED CHICKEN')
print(40*'-')

#output program
print('''No.  Jenis       Harga     Banyak   Jumlah
     Potong      Satuan    Beli     Harga''')
print(50*'-')

#proses
total = 0
for i in range(ayam):
    if listkode[i] == 'D' or listkode[i] == 'd':
        jenis = 'Dada'
        harga = int(2500)
    elif listkode[i] == 'P' or listkode[i] == 'p':
        jenis = 'Paha'
        harga = int(2000)
    elif listkode[i] == 'S' or listkode[i] == 's':
        jenis = 'Sayap'
        harga = int(1500)
    else :
        jenis = '-'
        harga = int(0)

    total1 = harga * listbanyak[i]
    total = total + total1
    ppn = total * 0.1
    totalbayar = total + ppn

    print(i+1, '  ', jenis, '\t', harga, '\t  ', listbanyak[i], '\t   ', total1)
print(50*'-')
print('\t\tTotal Pembelian   :', total)
print('\t\tPpn               :', ppn)
print('\t\tTotal Bayar       :', totalbayar) 