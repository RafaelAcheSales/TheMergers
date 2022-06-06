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

# Analyse the new content table header to define the type of merge to be used
def analyse_new_table_and_merge(table, index) -> list:
    # reads the header of the current to-be-merged table
    info = read_header(table)
    collumns_to_be_added = info[0][1:]
    for collumn in collumns_to_be_added:
        merge_specific_collumn(collumn, info[1], index)

# get the header of a table
def read_header(table):
    with open(table, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        return header, table

# add the new column in agreement with the TYPES_OF_MERGE
def merge_specific_collumn(collumn, table_name, index):
    # creates temporary files for each iteration of the merge
    file_name = sys.argv[1] if index == 0 else (OUTPUT_FILE_NAME+str(index)+'.csv')
    output_file_name = OUTPUT_FILE_NAME+str(index+1)+'.csv'
    
    # merges the new table with the most recent output file
    my_merger = TYPES_OF_MERGE[collumn](file_name, output_file_name)
    my_merger.merge_tables(table_name)
    
    # closes used files for the next iteration to use them
    my_merger.close_files()

#--------------------------------------------------------------------------------------------------------------------------------
# Get all the new tables file names from arguments
new_tables_list = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    elif i == 1:
        # gets name of source input file
        input_file_name = arg
    else:
        # gets name of the tables to be merged into source input file
        new_tables_list.append(arg)

# merge all the tables sent by argv in sequence
print("ASDADWDWA")
print(len(new_tables_list))
for i in range(len(new_tables_list)):
    analyse_new_table_and_merge(new_tables_list[i], i)

