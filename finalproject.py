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
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            city=input('Sorry, {} is not a valid city. Please enter either Chicago, New York City OR Washington again'.format(city))
        else:
            break

    #TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to see data for January, February, March, April, May, June or all?\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            month=input('Sorry, {} is not a valid month. Please enter either January, February, March, April, May, June, or All'.format(month))
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n").lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            day=input('Sorry, {} is not a valid day of the week. Please enter either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all'.format(day))
        else: day
        break

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
    #using dataframes and pandas to set up the environment
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    return df

#code below used to display statistics

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    frequent_month = df['month'].value_counts().idxmax()

    print('Most Common Start Month:', frequent_month)

    # TO DO: display the most common day of week

    frequent_day = df['day_of_week'].value_counts().idxmax()

    print('Most Common Day of Week:', frequent_day)

    # TO DO: display the most common start hour

    frequent_hour = df['hour'].value_counts().idxmax()

    print('Most Common Start Hour:', frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()

    print('Most Commonly Used Start Station', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()

    print('Most Commonly Used End Station', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_and_end_station = df[['Start Station', 'End Station']].mode().loc[0]

    print("The most frequently used start station and end station : {}, {}"\
            .format(most_frequent_start_and_end_station[0], most_frequent_start_and_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    travel_time = sum(df['Trip Duration'])/(24*60*60)

    print('Total Travel Time in Days', travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    mean_travel_time = mean_travel_time/(24*60*60)

    print('Average Travel Time in Days', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Types of users:", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Counts of gender:", gender)
    except KeyError:
        print("Data Not Available")


    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest birth year
    try:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest birth year:', earliest_year)
    except KeyError:
        print("Data Not Available")

    # Most recent birth year
    try:
        most_recent_birth_year = int(df['Birth Year'].max())
        print('Most recent birth year:', most_recent_birth_year)
    except KeyError:
        print("Data Not Available")

    # Most common birth year
    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year:',int(most_common_birth_year))
    except KeyError:
        print("Data Not Available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays the raw data
    Input:
        all the bikeshare data
    Returns:
       none
    """

    rowIndex = 0

    fiverows = input("\nWould you like to see five rows of the raw data? Please write 'yes' or 'no' \n").lower()

    while True:
        if fiverows == 'no':
           break

        if fiverows == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5
            fiverows = input("\nWould you like to see five more rows of data? Please write 'yes' or 'no' \n").lower()

    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
