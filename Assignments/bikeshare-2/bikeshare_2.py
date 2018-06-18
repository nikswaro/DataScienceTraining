import time
import pandas as pd
import numpy as np
import sys

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
    city_list = ['chicago', 'new york city', 'washington']
    month_list = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nPlease enter the city you want to see the details: Options(chicago-0,new york city-1, washington-2)\n')
            try:
                city = int(city)
                if int(city) in range(len(city_list)):
                    city = city_list[int(city)]
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again'.format(city))
            except ValueError:
                if city.lower() in city_list:
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again'.format(city))
        except KeyboardInterrupt:
            print('\nThank you')
            sys.exit()

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\nPlease enter the month you want to see the details: Options(all-0, january-1, february-2, ...., december-12)\n')
            try:
                month = int(month)
                if int(month) in range(len(month_list)):
                    month = month_list[int(month)]
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again:\n'.format(month))
            except ValueError:
                if month.lower() in month_list:
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again:\n'.format(month))
        except KeyboardInterrupt:
            print('\nThank you')
            sys.exit()  

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nPlease enter the day of week you want to see the details: Options(all-0, monday-1, tuesday-2, ...., sunday-7)\n')
            try:
                day = int(day)
                if int(day) in range(len(day_list)):
                    day = day_list[int(day)]
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again:\n'.format(day))
            except ValueError:
                if day.lower() in day_list:
                    break
                else:
                    print('\nI am afraid "{}" is not a valid input. Please try again:\n'.format(day))
        except KeyboardInterrupt:
            print('\nThank you')
            sys.exit()  

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =  df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    print('\nThe most common month for usage is: {}'.format(months[df['month'].mode()[0]-1]).title())

    # display the most common day of week
    print('The most common day of week for usage is: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('The most common start hour of the day for usage is: {}:00 hrs'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    print('The most common used start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most common used end station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    trip = (df['Start Station'].str.cat(df['End Station'], sep=',')).mode()[0]

    print('The most common trip is from {} to {} station'.format(trip.split(',')[0], trip.split(',')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    print('\nThe total travel time is {} hours, {} minutes and {} seconds'.format((df['Trip Duration'].sum())//3600,
            ((df['Trip Duration'].sum())%3600)//60,
            ((df['Trip Duration'].sum())%3600)%60)) 

    # display mean travel time
    print('The mean travel time is {} hours, {} minutes and {} seconds'.format((df['Trip Duration'].mean())//3600,
            ((df['Trip Duration'].mean())%3600)//60,
            round(((df['Trip Duration'].mean())%3600)%60,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    print("\nUser Types and their counts.")
    print(df.groupby(['User Type']).size())

    # Display counts of gender
    if 'Gender' in df.columns:
        print("\nGender and their counts.")
        print(df.groupby(['Gender']).size())
    else:
        print('\nGender information is unavailable in the data filter selected')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is: {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is: {}'.format(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth year information is unavailable in the data filter selected')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displayData(df, count):
    start_index = (count - 1)*5
    end_index = start_index + 4
    print('\nPlease see below the raw data from {} index to {} index of the data filtered:'.format(start_index,end_index))    
    print(df.loc[start_index:end_index])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        count = 0
        while True:
            raw_data = input('\nWould you like to see next 5 rows of the raw data for the filters selected? Enter yes or no.\n')
            count += 1            
            if raw_data.lower() == 'yes':
                displayData(df,count)
            else:
                break
        restart = input('\nWould you like to restart by selecting new filters? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
