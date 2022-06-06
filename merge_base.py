import csv
class TableMerger:
    def __init__(self, input_file_name, output_file_name):
        self.input_file = open(input_file_name, newline='')
        self.input_reader = csv.reader(self.input_file, delimiter=',', quotechar=' ')
        self.output_file = open(output_file_name, 'w+', newline='')
        self.output_writer = csv.writer(self.output_file, delimiter=',', quotechar=' ')
        

    def generate_dict(self, table):
        return_value = {}
        header = ""
        with open(table, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            header = next(csv_reader)[1]
            for row in csv_reader:
                return_value[row[0]] = row[1]
            return return_value, header
    
    def merge_tables(self, new_table):
        print("Not implemented")

    def close_files(self):
        self.input_file.close()
        self.output_file.close()