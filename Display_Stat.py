class displaystat:
    def display(self, duplicates, floor_count, processing_time):

        print("\n1) Отображение дублирующихся записей с количеством повторений.")
        print("\nДублирующиеся записи:")

        for key, count in duplicates.items():
            if count > 1:
                print(f"Город - {key[0]} \nУлица - {key[1]} \nДом - {key[2]} \nКоличество повторений - {count}")

        print("\n2) Отображение количество n-этажных зданий. ")
        for city, floors in floor_count.items():
            print(f"Город: {city}")
            for floor, count in floors.items():
                print(f"Количество домов с {floor} этажами: {count}")

        print(f"\n3) Время обработки --- {processing_time:.2f} секунд\n")