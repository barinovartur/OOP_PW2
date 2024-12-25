import xml.etree.ElementTree as ET
import csv

class fileparser:
    def read(self, file_path):

        if not file_path:
            raise ValueError("Путь к файлу не может быть пустым")
        if file_path.endswith('.xml'):
            return self.pars_xml(file_path)
        elif file_path.endswith('.csv'):
            return self.pars_csv(file_path)
        else:
            raise ValueError("Неподдерживаемый формат файла. Ожидаются только XML или CSV.")

    def pars_csv(self, file_path):
        data = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file, delimiter=';')
                for row in csv_reader:
                    city = row['city']
                    street = row['street']
                    house = row['house']
                    floor = row['floor']
                    data.append((city, street, house, floor))
            return data

        except FileNotFoundError:
            raise ValueError(f"Файл не обнаружен: {file_path}")
        except csv.Error as e:
            raise ValueError(f"Ошибка при чтении файла: {e}")

    def pars_xml(self, file_path):

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = []
            for item in root.findall('item'):
                city = item.get('city')
                street = item.get('street')
                house = item.get('house')
                floor = item.get('floor')
                data.append((city, street, house, floor))
            return data
        except FileNotFoundError:
            raise ValueError(f"Файл не обнаружен: {file_path}")
        except csv.Error as e:
            raise ValueError(f"Ошибка при чтении файла: {e}")


