from stelezhka import Stelezhka
from gruz import Gruz
from pozitsiya import Pozitsiya

def main():
    stelezhki = {}
    gruzy = {}
    pozitsii = []

    # Чтение входного файла
    try:
        with open("входной.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Файл 'входной.txt' не найден.")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(';')
        tip_zapisi = parts[0]

        if tip_zapisi == "STEL":
            kod_stelezhki = int(parts[1])
            nomer = int(parts[2])
            kolichestvo_yacheek = int(parts[3])
            dopustimaya_massa = float(parts[4])
            stelezhki[kod_stelezhki] = Stelezhka(kod_stelezhki, nomer, kolichestvo_yacheek, dopustimaya_massa)

        elif tip_zapisi == "GRUZ":
            kod_gruza = int(parts[1])
            nazvanie = parts[2]
            gruzy[kod_gruza] = Gruz(kod_gruza, nazvanie)

        elif tip_zapisi == "POZ":
            id = int(parts[1])
            kod_gruza = int(parts[2])
            kod_stelezhki = int(parts[3])
            nomer_yacheiki = int(parts[4])
            massa = float(parts[5])
            data_ukladki = parts[6]
            pozitsii.append(Pozitsiya(id, kod_gruza, kod_stelezhki, nomer_yacheiki, massa, data_ukladki))

            # Обновляем стеллаж
            if kod_stelezhki in stelezhki:
                stelezhka = stelezhki[kod_stelezhki]
                stelezhka.zanyatye_yacheiki.add(nomer_yacheiki)
                stelezhka.obschaya_massa += massa

    # Формирование отчёта
    result_lines = [
        "Отчёт о заполнении стеллажей\n",
        "-" * 60 + "\n",
        "№\tКод\tСвободных\tЗаполнение по массе (%)\n",
        "-\t---\t--------\t-------------------\n"
    ]

    for kod_stelezhki, stelezhka in sorted(stelezhki.items(), key=lambda x: x[1].nomer):  #ошибка была, что items без скобок. Добавила items() и все правилно
        svobodnye = stelezhka.kolichestvo_yacheek - len(stelezhka.zanyatye_yacheiki)
        if stelezhka.dopustimaya_massa > 0:
            procent = (stelezhka.obschaya_massa / stelezhka.dopustimaya_massa) * 100
        else:
            procent = 0.0
        result_lines.append(f"{stelezhka.nomer}\t{kod_stelezhki}\t{svobodnye}\t\t{procent:.1f}\n")

    # Запись в выходной файл
    with open("выходной.txt", "w", encoding="utf-8") as out_file:
        out_file.writelines(result_lines)

    print("Обработка завершена. Результат в 'выходной.txt'.")

if __name__ == "__main__":
    main()

