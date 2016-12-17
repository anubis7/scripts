#!/usr/bin/python
# @mpalonso SharifCTF2016 - Forensic 150 (concatenate the part of flag)
cadena2 = "cb13bbb59dde"
partecadena1 = "95cd605b"
parte2cadena1 = "9065f44530"
#TEORIA 1
##############################################
#Si hacemos el bucle tenemos una longitud de:
	# 95cd605b (+1) 9065f44530
	# 19 digitos en una parte
	# 12 digitos en la cadena 2
	# TOTAL: 31 digitos

#Si quitamos la "i"
	# 95cd605b9065f44530
	# 18 digitos en una parte
	# 12 digitos en la otra
	# TOTAL: 30 digitos
	# asumimos que esta es la correcta, pero de ser asi en que digito nos estamos equivocando
	
dic = "abcdef0123456789"
dicmay = "ABCDEF0123456789"

print "\n"
print "######################################################################"
print "CADENA 1 + CADENA 2 minus"
print "######################################################################"
print "\n"
for i in dic:
	for j in i:
		print "SharifCTF{" + partecadena1 + i + parte2cadena1 + cadena2 + "}"

print "\n"
print "######################################################################"
print "CADENA 2 + CADENA 1 minus "
print "######################################################################"
print "\n"
for i in dic:
	for j in i:
		print "SharifCTF{" + cadena2 + partecadena1 + i + parte2cadena1 + "}"
print "\n"
print "######################################################################"
print "CADENA NORMAL minus"
print "######################################################################"
print "\n"
print "SharifCTF{" + partecadena1 + parte2cadena1 + cadena2 + "}"
print "SharifCTF{" + cadena2 + partecadena1 + parte2cadena1 + "}"

print "\n"
print "######################################################################"
print "CADENA 1 + CADENA 2 mayus"
print "######################################################################"
print "\n"
for i in dicmay:
	for j in i:
		print "SharifCTF{" + partecadena1.upper() + i + parte2cadena1.upper() + cadena2.upper() + "}"

print "\n"
print "######################################################################"
print "CADENA 2 + CADENA 1 mayus "
print "######################################################################"
print "\n"
for i in dicmay:
	for j in i:
		print "SharifCTF{" + cadena2.upper() + partecadena1.upper() + i + parte2cadena1.upper() + "}"

print "\n"
print "######################################################################"
print "CADENA NORMAL mayus"
print "######################################################################"
print "\n"
print "SharifCTF{" + partecadena1.upper() + parte2cadena1.upper() + cadena2.upper() + "}"
print "SharifCTF{" + cadena2.upper() + partecadena1.upper() + parte2cadena1.upper() + "}"

print "\n"
print "\n"
for i in dic:
	for j in i:
		print partecadena1 + i + parte2cadena1 + cadena2

for i in dic:
	for j in i:
		print  cadena2 + partecadena1 + i + parte2cadena1

print partecadena1 + parte2cadena1 + cadena2
print cadena2 + partecadena1 + parte2cadena1


for i in dicmay:
	for j in i:
		print partecadena1.upper() + i + parte2cadena1.upper() + cadena2.upper()

for i in dicmay:
	for j in i:
		print cadena2.upper() + partecadena1.upper() + i + parte2cadena1.upper()

print partecadena1.upper() + parte2cadena1.upper() + cadena2.upper()
print cadena2.upper() + partecadena1.upper() + parte2cadena1.upper()
