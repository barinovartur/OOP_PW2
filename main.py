import time
import os
from File_Parser import fileparser
from Process_Data import processor
from Display_Stat import displaystat

class MainApp:
    def __init__(self):
        self.file_pars = fileparser()
        self.processor = processor()
        self.display_data = displaystat()

    def start(self):
        while True:
            file_path = input("Введите путь до файла для обработки (если хотите остановить программу, введите 0).\nВвод: ")

            match file_path.lower():
                case '0':
                    break

                case _ if not os.path.exists(file_path):
                    print("Файл не найден.")
                    continue

                case _:
                    start_time = time.time()

                    try:
                        data = self.file_pars.read(file_path)
                    except ValueError as e:
                        print(e)
                        continue

                    duplicate_records, floor_statistics = self.processor.process_city_data(data)
                    processing_time = time.time() - start_time

                    self.display_data.display(duplicate_records, floor_statistics, processing_time)

if __name__ == "__main__":
    main = MainApp()
    main.start()
