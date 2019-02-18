import os
import pandas as pd

## create csv file (directory.csv)
# nazwa katalogu roboczego
col_numbers = 0
poczatek = 500
katalog = os.getcwd()
col_names = []
for files in os.listdir(katalog):
    if files.endswith(".txt"):
        f = open(files)
        col1 = []
        col2 = []
        f1 = f.readlines()
        for lines in f1:
            if lines.startswith(poczatek):
                col1.append(lines.split()[0])
                col2.append(lines.split()[1])
        col_names.append(str(files))
        col_numbers += 1
        if col_numbers < 2:
            add columns (col1,col2) to csv file
        else:
            add col2 to csv file
        close file

save large csv file
make plot

    
    
