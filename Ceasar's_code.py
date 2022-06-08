def shifrovanie():  # Функция шифра
    napravlenie = input('Вы хотите зашифровать или дешифровать данные? (Code / Decode) : ').upper()
    yazyk = input('Выберите используемый язык (ru / en) : ').upper()
    shag_sdviga = int(input('Выберите длину шага (враво) : '))
    ishodni_text = input('Введите текст для шифрования : ')
    ishodni_text_spisok = list(ishodni_text)
    russkie_bukvy_mal = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    russkie_bukvy_bol = 'АБВГДЕЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬЭЮЯ'
    angl_bukvy_mal = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    angl_bukvy_bol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    konechny_spisok = []
    konechny_text = ''

    if napravlenie == 'CODE' and yazyk == 'EN':
        for i in range(len(ishodni_text)):
            if ishodni_text[i] in angl_bukvy_bol:
                position = int(angl_bukvy_bol.find(ishodni_text[i]))
                konechny_spisok.extend(angl_bukvy_bol[position + shag_sdviga % 26])
            elif ishodni_text[i] in angl_bukvy_mal:
                position = int(angl_bukvy_mal.find(ishodni_text[i]))
                konechny_spisok.extend(angl_bukvy_mal[position + shag_sdviga % 26])
            else:
                konechny_spisok.extend(ishodni_text[i])
        konechny_text = ''.join(konechny_spisok)
        return konechny_text
    elif napravlenie == 'CODE' and yazyk == 'RU':
        for i in range(len(ishodni_text)):
            if ishodni_text[i] in russkie_bukvy_bol:
                position = int(russkie_bukvy_bol.find(ishodni_text[i]))
                konechny_spisok.extend(russkie_bukvy_bol[position + shag_sdviga % 32])
            elif ishodni_text[i] in russkie_bukvy_mal:
                position = int(russkie_bukvy_mal.find(ishodni_text[i]))
                konechny_spisok.extend(russkie_bukvy_mal[position + shag_sdviga % 32])
            else:
                konechny_spisok.extend(ishodni_text[i])
        konechny_text = ''.join(konechny_spisok)
        return konechny_text



print(shifrovanie())