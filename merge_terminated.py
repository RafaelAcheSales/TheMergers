from merge_base import TableMerger
import csv
class TerminatedMerger(TableMerger):
    def __init__(self, input_file_name, output_file_name):
        super().__init__(input_file_name, output_file_name)

    #get all royalty_types
    def get_terminated_headers(self, csv_reader):
        headers_list = []        
        for row in csv_reader:
            if row[1] not in headers_list:
                headers_list.append(row[1])   
        headers_list.pop(0)
        return headers_list

    def merge_tables(self, table_name):
        with open(table_name, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            self.my_headers = self.get_terminated_headers(csv_reader)

        
        result_dict = {}
        for row in self.input_reader:
            result_dict[row[0]] = ['NO' for i in range(len(self.my_headers))]

        with open(table_name, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar=' ')
            next(csv_reader)
            for row in csv_reader:
                try:
                    result_dict[row[0]][self.my_headers.index(row[1])] = 'YES'
                except:
                    continue
                    
        
        self.input_file.seek(0)
        first_row = next(self.input_reader)
        for head in self.my_headers:
            first_row.append(head)
        print(first_row)
        self.output_writer.writerow(first_row)
        for row in self.input_reader:
            row.append(','.join(result_dict[row[0]]))
            self.output_writer.writerow(row)

