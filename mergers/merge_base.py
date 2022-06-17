import csv
class TableMerger:
    def __init__(self, input_file_name, output_file_name, pk_index):
        # get the table that will receive new info for each user_id
        self.input_file = open(input_file_name, newline='', encoding='utf8')
        self.input_reader = csv.reader(self.input_file, delimiter=',', quotechar=' ')

        # Create the output file where the merged infos will be written
        self.output_file = open(output_file_name, 'w+', newline='', encoding='utf8')
        self.output_writer = csv.writer(self.output_file, delimiter=',', quotechar=' ')
        self.pk_index = pk_index
        
    #transform csv table into dict using the format {'user_id':value, ...}
    def generate_dict(self, table):
        table_dict = {}
        header = ""
        with open(table, newline='', encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            header = next(csv_reader)[1]
            
            # For each row of the csv table, creates a new entry in the dict
            # where row[0] is the user_id, and row[1] is it's value
            for row in csv_reader:
                table_dict[row[0]] = row[1]
            return table_dict, header
    
    def merge_tables(self, new_table):
        print("Not implemented")

    def close_files(self):
        self.input_file.close()
        self.output_file.close()