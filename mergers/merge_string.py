from mergers.merge_base import TableMerger

class StringMerger(TableMerger):
    def __init__(self, input_file_name, output_file_name, pk_index):
        super().__init__(input_file_name, output_file_name, pk_index)

    def merge_tables(self, new_table):
        self.new_table_dict, self.new_table_header = self.generate_dict(new_table)

        #For each user_id in the input file, merge the self.new_table_dict['user_id'] value
        for row in self.input_reader:
            if row[self.pk_index] in self.new_table_dict:
                #Merge the input user_id's values with the to-be-added user_id's values
                value = self.new_table_dict[row[self.pk_index]]
                row.append(value)
            else:
                #Merge the input header with the to-be-added header
                row.append(self.new_table_header)
            
            # Write the merged row of info in the output file
            self.output_writer.writerow(row)