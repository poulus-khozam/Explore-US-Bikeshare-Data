import time
import pandas as pd
import numpy as np

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
    city=''
    while city not in CITY_DATA:
        city = input("Would you like to see data for Chicago, New York city, Washington ?\n")
        city=city.lower()
    
    ans=''
    while ans not in ['month','day','both','none']:
        ans = input('Would you like to filter the data by month ,day ,both , or not at all? Type "none" for no time filter.\n')
        ans=ans.lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month='all'
    if ans in ['month','both']:
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            month = input("Which month? January, February, March, April, May, or June?\n")
            month=month.lower()    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day='all'
    if ans in ['day','both']:
        days = {'1':'Sunday', '2':'Monday', '3':'Tuesday', '4':'Wednesday', '5':'Thursday', '6':'Friday','7':'Saturday'}
        while day not in days:
            day = input("Which day? please type your response as an integer (e.g., 1=Sunday).\n")
        day=days[day].lower()    
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]   
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)

    
    # TO DO: display the most common day of week
    # find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular Start day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    
    # extract hour from the Start Time column to create an hour column    
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    # find the most popular end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # extract hour from the Start Time column to create an hour column    
    df['combination'] = df['Start Station']+'-'+df['End Station']
    
    # find the most popular combination
    popular_combination = df['combination'].mode()[0]

    print('Most Popular combination:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # find the total travel time
    total_travel = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel)


    # TO DO: display mean travel time
    # find the mean travel time
    mean_travel = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:\n', df['User Type'].value_counts()) 
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('counts of user types:\n', df['Gender'].value_counts()) 

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest year of birth:\n', df['Birth Year'].min()) 
        print('most recent year of birth:\n', df['Birth Year'].max()) 
        print('most common year of birth:\n', df['Birth Year'].mode()[0])        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        row_data=''        
        while row_data.lower() !='no' and line<df.shape[0]:            
            row_data=input('\nwould like want to see 5 lines of the raw data ? Enter yes or no.\n')
            print(df[line:line+5])
            line+=5
            
        print('-'*40)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
