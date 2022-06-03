# Changes the primary key from email to id if necessary 

if __name__ == "__main__":
    new_tables_list = []
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        elif i == 1:
            input_file_name = arg
        else:
            new_tables_list.append(arg)