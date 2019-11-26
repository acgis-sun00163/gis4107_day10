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


file_name = "Haiti_Admin_Names.csv"
file_route = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "data",
                            file_name)


with open("haiti_admin_names_fixed.csv", "wb") as out_csv:
    with open(file_route,"rb") as in_csv:
        reader= csv.reader(in_csv, delimiter = ',')
        print  reader


        for row in reader:
            print row[0]

            parts= row.split(',')
            admin_code= row[0]
            new_admin = admin_code[:4]+ admin[5:]
            witer.writerow(new_admin)

    writer=csv.writer(out_csv)
