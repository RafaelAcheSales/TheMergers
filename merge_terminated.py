from . import merge_tables

class TerminatedMerger(merge_tables.TableMerger):
    def __init__(self, input_file_name, tables_list):
        super().__init__(input_file_name, tables_list)