#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cheng
#
# Created:     15/11/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
       with open("haiti_admin_names_fixed", "w") as out_csv:
        with open('Haiti_Admin_Names.csv') as in_csv:
            reader= csv.reader(in_csv, delimiter = ',')
            writer=csv.writer(out_csv)


            for row in reader:
                print row

if __name__ == '__main__':
    main()
