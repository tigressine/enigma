#! /usr/bin/env python3
import enigma

e = enigma.Machine()
#print(e.all_rotors)
#print('\n')

x = e.translate("yahooggg")
y = e.translate("B[l]_")
z = e.translate("yahooyahooyahooyahooyahooyahooyahooyahooyahoo")
zz = e.translate(z)
print(x)
print(y)
print(z)
print(zz)
print(len(z))
