from merge_base import TableMerger

class BoolMerger(TableMerger):
    def __init__(self, input_file_name, output_file_name):
        super().__init__(input_file_name, output_file_name)

    def merge_tables(self, new_table):
        self.new_table_dict, self.new_table_header = self.generate_dict(new_table)
        for row in self.input_reader:
            if row[0] in self.new_table_dict:
                value = "YES" if self.new_table_dict[row[0]] == "true" else "NO"
                row.append(value)
            else:
                row.append(self.new_table_header)
            self.output_writer.writerow(row)
        