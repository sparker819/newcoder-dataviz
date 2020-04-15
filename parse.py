'''
Data visualization project
Part 1: parsing data from a CSV and returning it as a JSON object
'''

import csv
import pandas as pd
import json

MY_FILE = r'C:\Users\steve\MyPythonScripts\new-coder\dataviz\data\sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):
    """
    Parses a CSV file into a JSON object.
    INPUT:
        raw_file [file]: the CSV flie to parse
        delimeter [str]: how the CSV file is delimited
    RETURN:
        parsed_data [list]: a list of dictionaries that can be turned into a JSON object 
    """

    # open file and extract data
    open_file = open(raw_file)
    # read data
    csv_data = csv.reader(open_file, delimiter=delimiter)
    # set up destination
    parsed_data = []
    # headers 
    fields = csv_data.__next__()
    # data
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    # close file 
    open_file.close()

    return parsed_data

def parse_pandas(raw_file):
    """
    Parses a CSV file into a JSON object using pandas.
    INPUT:
        raw_file [file]: the CSV flie to parse
    RETURN:
        parsed_data [list]: a list of dictionaries that can be turned into a JSON object 
    """

    df = pd.read_csv(raw_file, dtype='object')
    df_str = df.to_json(orient='records')
    json_formatted = json.loads(df_str)

    return json_formatted



def main():
    bad_way = parse(MY_FILE, ',')
    pandas_data = parse_pandas(MY_FILE)

    print(len(bad_way))
    print(len(pandas_data))

    print(bad_way == pandas_data)

    print(bad_way[0:5])
    print(pandas_data[0:5])

if __name__ == "__main__":
    main()