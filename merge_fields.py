import sys
import csv
from typing import overload

# input_file -> detectar se ID ou Email
# argumento (nomes das colunas no DB)
# instancia a classe referente ao argumento

if __name__ == "__main__":
    new_tables_list = []
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        elif i == 1:
            input_file_name = arg
        else:
            new_tables_list.append(arg)

class FieldMerger:
    def __init__(self, input_file_name, tables_list):
        self.input_file = open(input_file_name, newline='')
        self.input_reader = csv.reader(self.input_file, delimiter=',', quotechar='|')
        self.output_file = open('output.csv', 'w+', newline='')
        self.output_writer = csv.writer(self.output_file, delimiter=',', quotechar='|')
        self.list_of_dicts = []
        for table in tables_list:
            self.list_of_dicts.append(self.generate_dict(table))

    def generate_dict(self, table):
        return_value = {}
        header = ""
        with open(table, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            header = next(csv_reader)[1]
            for row in csv_reader:
                return_value[row[0]] = row[1]
        return return_value, header

    
    def merge_fields(self, input_table, new_values_dict, header):
        for row in input_table:
            if row[0] in new_values_dict:
                value = "Yes" if new_values_dict[row[0]] == "true" else "No"
                row.append(value)
            else:
                row.append(header)
            self.output_writer.writerow(row)

    def merge_all_tables(self):
        for table, header in self.list_of_dicts:
            self.merge_fields(self.input_reader, table, header)


merger = FieldMerger(input_file_name, new_tables_list)
merger.merge_all_tables()



