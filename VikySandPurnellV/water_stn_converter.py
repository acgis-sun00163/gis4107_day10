# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        water_stn_converter.py
#
# Purpose:
#    Converts a JSON file created using the water_stn_downloader module to
#    CSV or KML.
#    For the CSV, the output columns will be:
#      {Station_Number}, {Station_Name}, {Longitude}, {Latitude}, LINK
#
#    where LINK is
#    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}
#
#    Header for CSV will be:
#      StationNumber, StationName, Longitude, Latitude, WaterOfficeLink
#
#    For the KML, the <Placemark> element will have the following sub-elements:
#              <name>{Station_Name}</name>
#              <description>
#                 link
#              </description>
#              <Point>
#                <coordinates>{Longitude},{Latitude},0</coordinates>
#              </Point>
#
#   Items enclosed by { } are the keys in the dictionary associated with
#   each feature (a key:value dictionary of values).
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import csv
import json
import water_stn_downloader_client as wsdc

in_json_filename = ''
out_csv_filename = ''
out_kml_filename = ''

def json_to_csv():
    global out_csv_filename
    """Converts a JSON file created using the water_stn_downloader module
    to CSV"""

    # Call load_json_file_to_dict()
    #
    load_json_file_to_dict()
    # Create a unicode format string for 5 comma-separated values terminated
    # with a new line character (e.g. u'abc' is a unicode string)
    #
##    fmt = ' Station_Number', 'Station_name', 'Longitude', 'Latitude','W'

    # Use with to open out_csv_filename
    #

        # Write the header to the CSV file
        #


        # Loop through all the features and write the results to the CSV file
        # NOTE:  use .encode('utf-8') on the string before writing to the file
        #


    data= load_json_file_to_dict()
    with open(out_csv_filename, 'wb') as out_file:
        csv_header= 'Station_Number, Station_name, Longitude, Latitude, WaterOfficeLink'
        writer = csv.writer(out_file)
        writer.writerow(csv_header)

        for feature in range (0, len(data['features'])):
            four = get_values_from_feature(feature)
            four_utf =[]
            for item in four:

                item_utf= item.encode(encoding ='UTF-8')
                four_utf.append(item_utf)
            return four_utf

            wl =four_utf[0]


            four_utf.append(get_wateroffice_link(wl))
            writer.writerow(four)
    return 'Writing CSV file successfully !'



def json_to_kml():
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""


def load_json_file_to_dict():
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # Use with to open in_json_filename and use that file object as an
    # argument to json.load.  This will return a Python dict with nested
    # lists and dictionaries
    with open(in_json_filename, 'rb') as j_dic:
        json_dict= json.load(j_dic)

    return json_dict



def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude  """
    json_dict= load_json_file_to_dict()
    features = json_dict['features']

    character = features[feature]['attributes']


    attribute = []
    attribute.append(character ['Station_Number'])
    attribute.append(character ['Station_Name'])
    attribute.append(character ['Longitude'])
    attribute.append(character ['Latitude'])
    print attribute
    return attribute






def get_wateroffice_link(station_number):
    """Given a station_number, return the English wateroffice link"""
    return 'https://wateroffice.ec.gc.ca/report/real_time_e.html?stn=01AD002' + station_number

def get_kml_header():
    """Return the xml header including the Document start tag
    """
    return '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>'

def get_kml_footer():
    """Return the document and kml end tags
    """
    return '</Document>\n</kml>'

# Create a placemark format string that can be used for creating KML Placemark
# elements in get_placemark.  Remember to make this a unicode string since
# some of the placemark content will contain unicode characters
#
pm_fmt = ''


def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    NOTE:  .encode('utf-8') is used on the resulting string to ensure
           proper encoding of characters

    """
    for feature in get_values_from_feature():
        feature = KML.Placemark(
                      kml.name(feature[1]),
                      KML.Point(
                             KML.coordinates(feature[2], feature[3])))


