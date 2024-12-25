from collections import defaultdict

class processor:
    def identify_duplicates(self, records):
        duplicate_count = defaultdict(int)
        for entry in records:
            address_key = (entry[0], entry[1], entry[2])  # (city, street, house)
            duplicate_count[address_key] += 1
        return duplicate_count

    def process_city_data(self, records):
        # Заменяем _identify_duplicates на identify_duplicates
        duplicate_records = self.identify_duplicates(records)  # Исправили на правильный метод
        city_floor_distribution = self.calculate_floor(records)
        return duplicate_records, city_floor_distribution

    def calculate_floor(self, records):
        floor_statistics = defaultdict(lambda: defaultdict(int))
        for entry in records:
            city, street, house, floor = entry
            floor_statistics[city][floor] += 1
        return floor_statistics
