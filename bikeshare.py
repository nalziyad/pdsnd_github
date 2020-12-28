import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Write a city name to start analyzing: Chicago, New York City or Washington. ").lower()
        if city not in CITY_DATA:
            print("Wrong answer. Please choose a city from 'Chicago' , 'New York City' or 'Washington' Only. ")
            continue
        else:
            break

# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Write the month name you want to filter by from 'January' till 'June' or 'All' to see all months. ").lower()
        if month not in MONTH_LIST:
            print("You wrote a wrong answer. Please choose a month from 'January' till 'June' only or 'All' from all months.")
            continue
        else:
            break
        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day of the week to start filtering from or 'All' for the whole week. ").lower()
        if day not in DAY_LIST:
            print("You choosed a wrong answer. Please try again.")
            continue
        else:
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
    try:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]

        if day != 'all':
                df = df[df['day_of_week'] == day.title()]
        return df
    except Exception as e:
        print('An Error has occurred: {}'.format(e))


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month for travelling is: ', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week for travelling is: ', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour for travelling is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        common_start = df['Start Station'].mode()[0]
        print('The start station most commonly used is: ', common_start)
    except:
        print("An error has occurred.")

    # display most commonly used end station
    try:
        common_end = df['End Station'].mode()[0]
        print('End station that is most commonly used is: ', common_end)
    except:
        print("An error has occurred.")
    # display most frequent combination of start station and end station trip
    try:
        df['combination'] = df['Start Station'] + " " + df['End Station']
        common_combination = df['combination'].mode()[0]
        print('The most frequent combination of start and end stations is: ', common_combination)
    except:
        print("An error has occurred.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = sum(df['Trip Duration'])
    print('The total travel time is: ', total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average travel duration is: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Number of user types: ', user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Users gender: ', gender)
    except:
        print('Sorry there is no gender data in this city.')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_year)
        recent_year = df['Birth Year'].max()
        print('Recent year of birth: ', recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', common_year)
    except:
        print('There is no birth year data in this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    display_data = input("Would you like to see 5 rows of individual trips data? Type 'Yes' or 'No'. ").lower()
    x = 0
    if display_data == 'yes':
        print(df[x:x + 5])

        while True:
            x = x + 5
            display_data = input("Would you like to see more data? Type 'Yes' or 'No'. ").lower()
            if display_data == 'yes':
                print(df[x:x + 5])
            else:
                 break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
