a = 1+2+3+4+5
print(a)

b = 1+2+ \
    3+4+\
        5
print(b)

c = (1+2+3)
print(c)

d = ('Januari', 'Februari', 'Maret')
print(d)

e = {'Januari', 'Februari', 
'Maret'}
print(e)

kata = 'kata'
kalimat = 'Contoh kalimat'
paragraf = """Contoh penggunaan
kalimat"""
print(kata)
print(kalimat)
print(paragraf)

'''Koding penggunaan paragraf'''
f = '''Jl. banten no. 1
karang pawitan'''
print(f)

print("=+=+=+=+ Data Diri Mahasiswa +=+=+=+=")
nim = input("NIM : ")
nama = input("Nama Lengkap : ")
jurusan = input("Jurusan : ")
alamat = input("Alamat : ")

print("Hasil cetak data diatas adalah")
print("Nim : "+str(nim))
print("Nama : "+str(nama))
print("Jurusan : "+str(jurusan))
print("Alamat : "+str(alamat))