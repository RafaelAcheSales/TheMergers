# How to use it:
This tool was made for joining tables with same PK and generating an output that can be usefull for analysing diferent types of data.

To run this script you must place .csv files inside tables_to_merge folder and run the following command:
```
python main.py input_file_1 input_file_2 input_file_3 ...
```
(note: you don't need to use .csv suffix in the args, just the name of the input files)

$ tree
Main_folder
├── tables_to_merge
│   ├── input_file_1.csv
│   ├── input_file_2.csv
│   ├── input_file_3.csv
│   └── ...
├── mergers
│   ├── merge_base.py
│   ├── merge_bool.py
│   └── merge_terminated.py
├── main.py
├── outputX.csv (the output will be generated here, with X being the number of tables merged)
└── README.md

# Input data
Input data must be .csv files delimited with comma (",") and no quote char in order to work. All csv collums will be interpreted and the script will try to merge, so the best pratice is to have a csv file with only PK and the to-be-merge collums by removing the unwanted collums from the inputs.


The script requires 2 or more input files with the same PK. Example:
    1st file -> input.csv (file with a list of user identified by a numeric user_id)
    2nd file -> is_active.csv (file with the info 'is_active' about all users identified by a numeric user_id)
    3rd file -> vip.csv (file with the info 'vip' about all users identified by a numeric user_id)
    4th file -> ...
    5th file -> ...