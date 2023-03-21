import random

miasta = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
for i in range(0, int(input("Ile miast chcesz odwiedzić?>"))):
    index = int(random.randint(0, len(miasta) - 1))
    print(index)
    print(miasta[index])
    miasta.remove(miasta[index])
