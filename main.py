import sys
import csv

from merge_bool import BoolMerger
from merge_terminated import TerminatedMerger
from merge_base import TableMerger

OUTPUT_FILE_NAME = 'output'



TYPES_OF_MERGE = {
    "is_active": BoolMerger,
    "vip": BoolMerger,
    "royalty_type" : TerminatedMerger,
}




def read_header(table):
    with open(table, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        return header, table

def header_analysis(info: tuple, index) -> list:
    collumns_to_be_added = info[0][1:]
    for collumn in collumns_to_be_added:
        merge_specific_collumn(collumn, info[1], index)

def merge_specific_collumn(collumn, table_name, index):
    file_name = sys.argv[1] if index == 0 else (OUTPUT_FILE_NAME+str(index)+'.csv')
    output_file_name = OUTPUT_FILE_NAME+str(index+1)+'.csv'
    print(f'Merging {file_name} with {table_name}')
    my_merger = TYPES_OF_MERGE[collumn](file_name, output_file_name)
    my_merger.merge_tables(table_name)
    my_merger.close_files()

# merger = FieldMerger(input_file_name, new_tables_list)
# merger.merge_all_tables()
new_tables_list = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    elif i == 1:
        input_file_name = arg
    else:
        new_tables_list.append(arg)

        
for i in range(len(new_tables_list)):
    header_analysis(read_header(new_tables_list[i]), i)


