#Operator Logika

#NOT (kebalikan)
print('---NOT---')
a = True
b = not a
print('data a =', a)
print('data b = ', b)

#OR (jika salah satu true, maka hasilnya true)
print('---OR---')
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

#AND (jika keduanya true, maka hasilnya true)
print('---AND---')
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

#XOR (akan true jika salah satu true, sisanya false)
print('---XOR---')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)




#Operator Penugasan/Assignment

print('Operator Penugasan')
x = 5
print('\nnilai x =',x)

x += 3 #artinya adalah x = x + 3
print('nilai x += 3 adalah', x)

x -= 2 #artinya adalah x = x - 2
print('nilai x -= 2 adalah', x)

x *= 5 #artinya adalah x = x * 5
print('nilai x *= 5 adalah', x)

x /= 2 #artinya adalah x = x / 2
print('nilai x /= 2 adalah', x)

x %= 3 #modulus (hasil sisa pembagian dari x dibagi 3)
print('nilai x %= 3 adalah', x)

y = 10
y //= 4 #floor division (pembulatan dari hasil y dibagi 4)
print('nilai y //= 10 adalah', y)

y **= 3 #artinya y pangkat 3
print('nilai y **= 3 adalah', y)




#Operator Bitwise

print('Operator Bitwise')
a = 7
b = 4
print('\nnilai a =', a, 'binary :', format(a,'08b'))
print('nilai b =', b, 'binary :', format(b,'08b'))

#Bitwise OR (|)
c = a | b
print('nilai a | b =', c, 'binary :', format(c,'08b'))

#Bitwise AND (&)
c = a & b
print('nilai a & b =', c, 'binary :', format(c,'08b'))

#Bitwise NOT (~)
c = ~a
print('nilai ~a =', c, 'binary :', format(c,'08b'))

#Bitwise XOR (^)
c = a ^ b
print('nilai a ^ b =', c, 'binary :', format(c,'08b'))

#Bitwise shift right (>>)
c = a >> 2
print('nilai a >> 2 =', c, 'binary :', format(c,'08b'))

#Bitwise shift left (<<)
c = b << 2
print('nilai b << 2 =', c, 'binary :', format(c,'08b'))



#Operator Identitas/Identity

print('Operator Identitas')
data1 = {1,2,3}
data2 = {3,4,5}
print('data1 is data2 :', data1 is data2)
print('data1 is not data2 :', data1 is not data2)



#Operator Keanggotaan/Membership

print('\nOperator Keanggotaan')
data = {'Hello', 'World'}
print('Apakah Hello ada di dalam data?', 'Hello' in data)
print('Apakah World tidak ada di dalam data?','World' not in data)
print('Apakah Python ada di dalam data?','Python' in data)
print('Apakah BSI tidak ada di dalam data?','BSI' not in data)