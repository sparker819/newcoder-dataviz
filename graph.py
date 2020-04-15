'''
Data visualization project
Part 2: Taking parsed data and plotting it with matplotlib

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

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from parse import MY_FILE, parse_pandas

def visualize_days(parsed_data):
    """
    Visualse data by day of the week.
    INPUT:
        parsed_data [list]: JSON-like list of crime data
    RETURN:
        None
    """
    # create a counter dict that counts how many records per day of week
    counter = Counter(item['DayOfWeek'] for item in parsed_data)

    # create the y axis data in the order of days of the week
    data_in_week_order = [
        counter['Monday'],
        counter['Tuesday'],
        counter['Wednesday'],
        counter['Thursday'],
        counter['Friday'],
        counter['Saturday'],
        counter['Sunday']
        ]
    # create x axis labels
    week_order_tuple = tuple(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    # plot line graph of incidents by day of week
    plt.plot(data_in_week_order)
    # add in the x axis labels 
    plt.xticks(ticks=range(len(week_order_tuple)), labels=week_order_tuple)
    # save a png version of the figure
    plt.savefig('Incidents_by_Days.png')
     # display the figure
    plt.show()
    # close the figure
    plt.clf()

    return 


def visualize_type(parsed_data):
    """
    Visualse data by the category of incident.
    INPUT:
        parsed_data [list]: JSON-like list of crime data
    RETURN:
        None
    """
    # create a counter dict that counts how many records per day of week
    counter = Counter(item['Category'] for item in parsed_data)

    # create x axis labels
    x_labels = tuple(counter.keys())

    # format x axis labels
    x_locations = np.arange(len(x_labels)) + 0.5

    # width of bar
    width = 0.5

    plt.bar(x= x_labels, height=counter.values(), width=width)
    plt.xticks(x_locations + width / 2, labels=x_labels, rotation=90)
    plt.subplots_adjust(bottom=0.45)
    plt.rcParams['figure.figsize'] = 12, 8


    # save a png version of the figure
    plt.savefig('Incidents_by_Category.png')
     # display the figure
    plt.show()
    # close the figure
    plt.clf()

    return 


def pd_viz_day_region (raw_data):
    """
    Visualize the data by day and region using pandas.
    INPUT:
        raw_data [path]: a path to a CSV file containing the data
    RETURN:
        Returns None
        Saves a .PNG file to cwd.
    """
    df = pd.read_csv(raw_data)
    grouped = df.groupby(['DayOfWeek', 'PdDistrict'])['IncidntNum'].count()
    unstacked = grouped.unstack(level=-1)
    
    wk_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_ordered = unstacked.reindex(index=wk_index)
    week_ordered = week_ordered.fillna(0.0)

    ax = week_ordered.plot(kind= 'line',
                           figsize= (12, 8),
                           title= 'Incidents by District & Day of Week'
                           )
    ax.set_ylabel('Incident Count')
    ax.set_xlabel('Day of Week')
    ax.legend(title='District')
    fig = ax.get_figure()
    fig.savefig('Incidents_by_Day_District.png')

    return


def pd_viz_day(raw_data):
    """
    Visualize the data by day using pandas.
    INPUT:
        raw_data [path]: a path to a CSV file containing the data
    RETURN:
        Returns None
        Saves a .PNG file to cwd.
    """
    wk_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df = pd.read_csv(raw_data)
    grouped = df.groupby(['DayOfWeek'])['IncidntNum'].count()
    week_ordered = grouped.reindex(wk_index)
    ax = week_ordered.plot(kind='line',
                           title= 'Incidents by Day of Week')
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Incident Count')
    fig = ax.get_figure()
    fig.savefig('Incidents_by_Day_pd.png')

    return



def main():
    data = parse_pandas(MY_FILE)
    visualize_days(data)
    visualize_type(data)
    pd_viz_day(MY_FILE)
    pd_viz_day_region(MY_FILE)

    return

if __name__ == "__main__":
    main()