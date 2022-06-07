from __future__ import print_function
from unittest import result
from mergers.merge_base  import TableMerger
import csv

#Used to merge tables with the values of terminated for all royalty types
class TerminatedMerger(TableMerger):
    def __init__(self, input_file_name, output_file_name):        
        super().__init__(input_file_name, output_file_name)
        self.result_dict = {}

    #get all royalty_types
    def get_terminated_enum(self, csv_reader):
        headers_list = []        
        for row in csv_reader:
            if row[1] not in headers_list:
                headers_list.append(row[1])   
        headers_list = [value.lower() for value in headers_list]
        headers_list.pop(0)
        return headers_list
    # Execute the merge
    def merge_tables(self, table_name):
        # Go through each table and populate the dict with the terminated status
        with open(table_name, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            self.my_headers = self.get_terminated_enum(csv_reader)
        self.generate_dict_with_false()
        self.populate_dict(table_name)
        self.append_new_headers_to_output()
        self.generate_output_file()


    # Generate a dict with all terminated status as 'NO"
    def generate_dict_with_false(self):
        for row in self.input_reader:
            self.result_dict[row[0]] = ['NO' for i in range(len(self.my_headers))]

    # Check terminated status for each user_id and update status to 'YES' when a royalty type is terminated for that user_id
    def populate_dict(self, table_name):
        with open(table_name, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            next(csv_reader)
            # If royalty type is terminated, update status, do nothing otherwise
            for row in csv_reader:
                try:
                    self.result_dict[row[0]][self.my_headers.index(row[1])] = 'YES'
                except:
                    continue
                
    def append_new_headers_to_output(self):
        self.input_file.seek(0)
        first_row = next(self.input_reader)
        for head in self.my_headers:
            first_row.append(head)
        self.output_writer.writerow(first_row)

    def generate_output_file(self):
        for row in self.input_reader:
            row.append(','.join(self.result_dict[row[0]]))
            self.output_writer.writerow(row)



    