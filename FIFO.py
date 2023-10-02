#FIFO, Andris Kõiv
# Importin massiivi mooduli
import array as massiiv
# Tekitan massiivi, kus i on indeks. See on vajalik, et saaks insert() funktsiooni kasutada, ehk siis arve sisestada ning neid hiljem kustutada kasutades pop()
x = massiiv.array("i", [])
# While loop, et programm ei läheks peale viimast käsku kinni
while True:
    lisatav = input("Kas soovid massiivi arvu lisada? y/n: ") # Küsitakse kasutajalt, kas ta soovib massiivi arvu lisada
    if lisatav == "y":
        lisatavint = int(input("Sisesta arv: "))  # Küsitakse kasutajalt, et ta sisestaks arvu. Kasutan ka int(), sest stringi ei saa massiivi lisada
        x.insert(0,lisatavint) # Iga arv sisestatakse indeksiga 0, seega iga sisestatud arv läheb esimeseks arvuks.
        print(x)				# Prinditakse massiiv koos uue lisatud arvuga
    else:
        print(x)				# Kui arvu ei lisata, prinditakse massiiv sellisena, nagu ta on
        
    kustuta= input("Kas soovid massiivist arve kustutada? y/n: ")	# Küsitakse, kas kasutaja soovib kustutada massiivist arve
    if kustuta == "y":												# Kui jah, siis kustutatakse esimene element massiivist.
        print(x.pop())	# Kustutatakse esimesena lisatud arv ehk siis viimane arv massiivis
        print(x)
    else:
        print(x)    												# Kui kasutaja ei soovi kustutada, näidatakse talle massiivi ning programm hakkab otsast peale