import json

class DataAccessObject:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.data = json.load(f)
            print(self.data)