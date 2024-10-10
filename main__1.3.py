# TODO Найдите количество книг, которое можно разместить на дискете

floppy_disk = 1.44 #мегабай на дискете 
floppy_disk *= 1000000 # 
pages = 100 # страниц
lines = 50 # строк
characters = 25 # символов
bytes_in_characters = 4 # байт в символе 

book = bytes_in_characters * characters * lines * pages

print(f"Количество книг, помещающихся на дискету: {floppy_disk / book:.0f}")