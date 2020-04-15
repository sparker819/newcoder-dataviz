'''
Data visualization project
Part 3: Mapping the data with geoJSON

=== SAMPLE DATA ENTRY ===
    IncidntNum : 030203898
    Category : FRAUD
    Descript : FORGERY, CREDIT CARD
    DayOfWeek : Tuesday
    Date : 02/18/2003
    Time : 16:30
    PdDistrict : NORTHERN
    Resolution : NONE
    Location : 2800 Block of VAN NESS AV
    X : -122.424612993055
    Y : 37.8014488257836
'''

import geojson

from parse import parse_pandas, MY_FILE

def create_map(data_file):
    """
    Creates a GeoJSON file.
    INPUT:
        data_file [list] = a json-like list    
    RETURN:
        None
        Saves a .geojson file in the cwd which can be loaded to github gists
    """
    
    # define type of geoJSON we're creating
    geo_map = {'type': 'FeatureCollection'}
    # define empty list to collect points to be mapped
    item_list = []

    for index, line in enumerate(data_file):
        if line['X'] == '0' or line['Y'] == '0':
            continue
        # define empty dictionary to collect data about each point
        point_data = {}
        point_data['type'] = 'Feature'
        point_data['id'] = index
        point_data['properties'] = {'title': line['Category'],
                                    'description': line['Descript'],
                                    'date': line['Date']}
        point_data['geometry'] = {'type': 'Point',
                                'coordinates': (line['X'], line['Y'])}
        
        item_list.append(point_data)

    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

    return

def main():
    data = parse_pandas(MY_FILE)
    return create_map(data)

if __name__ == "__main__":
    main()         
