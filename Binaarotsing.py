#Binaarotsing, Andris Kõiv
def otsing(massiiv, vahim, suurim, x):  						# Defineerin massiivi, vähima, suurima ja x-i
    if suurim >= vahim:											# Kui suurim on suurem võrdne kui vähim
        keskmine =(vahim + suurim) // 2							# Arvutatakse keskmine, mis on vähim + suurim jagatud 2ga. Nii saame keskkoha
        if massiiv[keskmine] == x:								# Kui sisestatud arv on juhuslikult massiivi keskel, tagastatakse selle sama arvu indeks
            return keskmine
        elif massiiv[keskmine] < x:								# Kui keskmine on väiksem kui x, siis otsime massiivi paremalt poolt
            return otsing(massiiv, keskmine + 1, suurim, x)		 
        else:
            return otsing(massiiv, vahim, keskmine -1, x)		# Kui keskmine on suurem kui x, otsime massiivi vasakult poolt
    else:
        return -1												# Kui väärtust pole massiivis, tagastatakse -1

massiiv = [10, 15, 16, 20, 30, 45, 50, 52, 61]					# Sorditud massiiv, vähimast suuremani
x = 30															# Väärtus, mida massiivist otsime

indeks = otsing(massiiv, 0, len(massiiv)-1, x)					# Indeksi on massiiv, 0, len(massiiv)-1, mis tagastab viimase masiivis oleva liikme indeksi ning x, mis on otsitav arv massiivist
if indeks == -1:												# Kui indeks on -1 (ehk siis otsitavat arvu ei ole massiivis, sellepärast lisasin ka return -1), siis teatatakse kasutajale, et arvu pole massiivis
    print("Otsitud väärtust pole massiivis")
else:
    print("Otsitud väärtuse indeks on", str(indeks))			# Kui otsingu tulemus ei ole -1, siis järelikult on arv massiivis ning sellisel juhul prinditakse tema indeks 