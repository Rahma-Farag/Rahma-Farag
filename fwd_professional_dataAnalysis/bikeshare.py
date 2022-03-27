import time
import pandas as pd
import numpy as np
import scipy.stats

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while(city not in CITY_DATA.keys()):
        print('please choose city to analyze\n')
        print('type name of city or number\n')
        print('1-chicago\n2-new york city\n3-washington\n')
        
        city = input().lower()
        if(city in ['1','2','3']):
            #if user enters a number map it to the city
            city = list(CITY_DATA.keys())[int(city)-1]
    print("city to analyze is ",city)

    
    # TO DO: get user input for month (all, january, february, ... , june)

    months = {'all':0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    month = ''
    
    while(month not in months.keys()):
        print('please choose month from January to June to analyze\n')
        print('type name of the month or number\n')
        print('type 0 or all for all months\n')
        print('0-all\n1-january\n2-february\n3-march\n4-april\n5-may\n6-june')
        
        month = input().lower()
        if(month in ['0', '1', '2', '3', '4', '5', '6']):
            #if user enters a number map it to the month
            month = list(months.keys())[int(month)]
    print("month to analyze is ",month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = {'all':0, 'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}
    day = ''
    while(day not in days.keys()):
        print('please choose day from monday to sunday to analyze\n')
        print('type name of the day or number from list\n')
        print('type 0 or all for all days\n')
        print('0-all\n1-monday\n2-tuesday\n3-wednesday\n4-thursday\n5-friday\n6-saturday\n7-sunday')
        
        day = input().lower()
        if(day in ['0', '1', '2', '3', '4', '5', '6', '7']):
            #if user enters a number map it to the day
            day = list(days.keys())[int(day)]
    print("day/s to analyze is ",day)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    months = {'all':0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
    
    #Load data for city
    city_path = CITY_DATA[city]
    df = pd.read_csv(city_path)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    
    if(month != 'all'):
        month_n = months[month]
        df = df[df['month'] == month_n]
    if(day != 'all'):
        day_n = days[day]
        df = df[df['day of week'] == day_n]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = {1:'january', 2:'february', 3:'march', 4:'april' , 5:'may', 6:'june'}
    days = {0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
    
    # TO DO: display the most common month
    pop_month = scipy.stats.mode(df['month'])[0][0]
    print("most popular month for travel is ",months[pop_month])
    # TO DO: display the most common day of week
    pop_day = scipy.stats.mode(df['day of week'])[0][0]
    print("most popular day of the week to travel is ",days[pop_day])

    # TO DO: display the most common start hour
    pop_hour = scipy.stats.mode(df['hour'])[0][0]
    print("most popular hour to travel is ", pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['start comb end'] = "From "+ df['Start Station'] + " To "+ df['End Station']
    # TO DO: display most commonly used start station
    pop_start_station = scipy.stats.mode(df['Start Station'])[0][0]
    print("most popular start station is ", pop_start_station)

    # TO DO: display most commonly used end station
    pop_end_station = scipy.stats.mode(df['End Station'])[0][0]
    print("most popular end station is ", pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    pop_from_to_stations = scipy.stats.mode(df['start comb end'])[0][0]
    print("most popular combination of start and end stations are ", pop_from_to_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['dur'] = df['End Time'] - df['Start Time']
    # TO DO: display total travel time
    total_trip_duration = np.sum(df['dur'])
    print("Total trip duration is ", total_trip_duration)

    # TO DO: display mean travel time
    avg_trip_duration = np.mean(df['dur'])
    print("Average trip duration is ", avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_user_count = df['User Type'].value_counts()
    print("types of users by number\n",type_user_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\ntype of users by gender\n", gender_count)
    else:
        "No gender column"

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest = df['Birth Year'].min()
        print("\nOldest user was born in year ", int(oldest))
        youngest = df['Birth Year'].max()
        print("Youngest user was born in year ", int(youngest))
        most_comman = scipy.stats.mode(df['Birth Year'])[0][0]
        print("Most users were born in year ", int(most_comman))
    else:
        "No Birth year column"

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_5rows(df):
    response = input("Do you want to view 5 rows of data: ")
    i = 0
    rows = 5
    while((response.lower() != 'no') and (i < len(df))):
        if(response.lower()== 'yes'):
            if((i+rows) > len(df)):
                print(df[i:])
                i += rows
            else:
                print(df[i:i+rows])
                i += rows
            response = input("Do you want to view 5 more rows of data: ")
        else:
            print('please responed with yes or no')
            response = input("Do you want to view 5 rows of data: ")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_5rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

