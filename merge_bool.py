from merge_base import TableMerger

#Used to merge tables with boolean values
class BoolMerger(TableMerger):
    def __init__(self, input_file_name, output_file_name):
        super().__init__(input_file_name, output_file_name)

    def merge_tables(self, new_table):
        self.new_table_dict, self.new_table_header = self.generate_dict(new_table)

        #For each user_id in the input file, merge the self.new_table_dict['user_id'] value
        for row in self.input_reader:
            if row[0] in self.new_table_dict:
                #Merge the input user_id's values with the to-be-added user_id's values
                value = "YES" if self.new_table_dict[row[0]] == "true" else "NO"
                row.append(value)
            else:
                #Merge the input header with the to-be-added header
                row.append(self.new_table_header)
            
            # Write the merged row of info in the output file
            self.output_writer.writerow(row)
        