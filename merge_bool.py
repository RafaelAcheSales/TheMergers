from . import merge_tables

class BoolMerger(merge_tables.TableMerger):
    def __init__(self, input_file_name, tables_list):
        super().__init__(input_file_name, tables_list)

    def merge_tables(self, input_table, new_values_dict, header):
        for row in input_table:
            if row[0] in new_values_dict:
                value = "YES" if new_values_dict[row[0]] == "true" else "NO"
                row.append(value)
            else:
                row.append(header)
            self.output_writer.writerow(row)