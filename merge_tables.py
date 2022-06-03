import sys
import csv


from . import merge_bool
from . import merge_terminated
# exe: python merge_fileds input_Table csv arg2 ....
# input_file -> detectar se ID ou Email
# instancia a classe referente ao argumento
TYPES_OF_MERGE = {
    "is_active": merge_bool.BoolMerger(),
    "has_yt_comp_term" : merge_terminated.TerminatedMerger(),
    "has_yt_sr_term": merge_terminated.TerminatedMerger(),
    "has_mech_streaming_term": merge_terminated.TerminatedMerger(),
    "has_mech_": merge_terminated.TerminatedMerger(),
}

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


def read_header(input_file_name: str) -> list:
    with open(input_file_name, "r") as input_file:
        reader = csv.reader(input_file)
        header = next(reader)
        return header

def header_analysis(header: list) -> list:
    collumns_to_be_added = header[1:]
    for collumn in collumns_to_be_added:
        merge_specific_collumn(collumn)

def merge_specific_collumn(self, collumn):
    my_merger = TYPES_OF_MERGE[collumn](input_file_name, )
    my_merger.merge_tables()

class TableMerger:
    def __init__(self, input_file_name, new_table):
        self.input_file = open(input_file_name, newline='')
        self.input_reader = csv.reader(self.input_file, delimiter=',', quotechar='|')
        self.output_file = open('output.csv', 'w+', newline='')
        self.output_writer = csv.writer(self.output_file, delimiter=',', quotechar='|')
        self.new_table_dict, self.new_table_header = self.generate_dict(new_table)

    def generate_dict(self, table):
        return_value = {}
        header = ""
        with open(table, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            header = next(csv_reader)[1]
            for row in csv_reader:
                return_value[row[0]] = row[1]
        return return_value, header
    
    def merge_tables(self):
        print(f'Merging {self.input_file.name} with {self.new_table_header}')




# merger = FieldMerger(input_file_name, new_tables_list)
# merger.merge_all_tables()
for table in new_tables_list:
    header_analysis(read_header(table))


