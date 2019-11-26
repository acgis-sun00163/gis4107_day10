#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#
# Edited by Chengjaiqi Sun
#
##Edited Date: Nov 15, 2019
#
#-------------------------------------------------------------------------------
import os
import csv
import array
import pandas as pd


in_csv = "Haiti_Admin_Names.csv"
out_csv = "haiti_admin_names_fixed.csv"
admin_code_column_index = 0


''' read the csv file
  ingnore the header part
  '''
def process_file():
    """in_csv = file where a column contains a admin_code that needs fixing.
                That is, the 5th character in admin_code needs to be removed.
       out_csv = file with same contents as in_csv with fixed admin_code
       admin_code_column_index = 0-based index of column containing the
                                 admin_code
    """
    file_route = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "data",
                            file_name)
    with open("haiti_admin_names_fixed", "wb") as out_csv:
        with open('Haiti_Admin_Names.csv',"rb") as in_csv:
            reader= csv.reader(in_csv, delimiter = ',')
            print  reader


            for row in next(reader):
                print row

                parts= row.split(',')
                admin_code= row[0]
                new_admin = admin_code[:4]+ admin[5:]
                witer.writerow(new_admin)

        writer=csv.writer(out_csv)



def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""
    return admin_code[:4]+ admin[5:]




