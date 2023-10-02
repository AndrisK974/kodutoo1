# Fibonacci, Andris Kõiv
def fibonacci(n):
    a = 0				# Fibonacci esimene arv on 0
    b = 1				# Fibonacci teine arv on 1
    if n == 0:			# Kui tahetakse teada 0-ndat arvu
        return 0		# Tuleb vastuseks 0, kuna fibonacci 0-s arv on 0
    elif n == 1:		# Kui tahetakse teada fibonacci 1. arvu
        return 1		# Tagastatakse vastuseks number 1, kuna esimene fibonacci arv on 1
    else:
        for i in range(2, n): # Kui arv on suurusjärgus 2 kuni n, ehk siis 2 või suurem. Kui arv on väiksem, kui 2, kasutatakse üleval olevat funktsiooni
            c = a + b         # Funktsioon mis liidab arve järjest kokku. Kõigepealt liidetakse kokku 0+1, siis 1+1, siis 2+1, 3+2, 5+3 jne
            a = b
            b = c
        return b

print(fibonacci(12))				# Tagastatake n-is fibonacci arv. Kui sulgudes on 12, peaks vastus tulema 89