'''Lakukankan pengulangan input data sebanyak 2 kali dengan data dibawah ini :
Data Ke- <berulang>
Masukkan NIM anda : <Input Data Ke 1>
Masukkan Nilai UTS : <Input Data Ke 1>
Masukkan Nilai UAS : <Input Data Ke 1>
Nim anda adalah <outputnim1> nilai UTS anda <outpututs1> nilai UTS anda
<outputuas1>'''


ulang = 1
for i in range(ulang):
    print ("Data Ke - " + str(i+1))
nama=input("Masukkan NIM anda : ")
uts=int(input("Masukkan Nilai UTS anda :"))
uas=int(input("Masukkan Nilai UAS : "))
print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama,uts,uas))
print("-------------------------------------\n")

for i in range(ulang):
    print ("Data Ke - " + str(i+2))
nama=input("Masukkan NIM anda : ")
uts=int(input("Masukkan Nilai UTS anda :"))
uas=int(input("Masukkan Nilai UAS : "))
print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama,uts,uas))
print("-------------------------------------\n")