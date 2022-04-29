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
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWhich city data would you like to explore")
        city = input("Chicago, New York City or Washington? \nInput:").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("\nInvalid Selection\n")
            print("Try again!")


    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ["january", "february", "march", "april", "may", "june", "all"]
    month = ''
    while month not in month_list:
        print("\nFor which month?")
        month = input("January, February, March, April, May, June or All? \nInput:").lower()
        if month in month_list:
            break
        else:
            print("\nInvalid Selection.\n")
            print("Try again!")             



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    day = ''
    while day not in day_list:
        print("\nWhich day of the week are you interested in?")
        day = input("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? \nInput:").lower()
        if day in day_list:
            break
        else:
            print("\nInvalid Selection\n")
            print("Try again!")



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
    # load data file into a dataframe
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

def raw_data(df):
    """View five rows of data per time as long as reponse is yes."""
    
    responses = ["yes", "no"]
    response = ''
    start_loc = 0
    print("\nWould you like to view some of the raw data?")
    response = input("Yes or No? \nInput:").lower()
    while response in responses:
        #break while loop if response is no
        if response == "no":
            print("\nWe would skip that!\n")
            print('-'*40)
            break
        #Continue showing five rows of data if response is yes
        if response == "yes":
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        response = input("Do you wish to continue? Yes or No? \nInput:")
        

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    popular_month_index = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = months[popular_month_index - 1]
    print(f"\nThe most popular month is {popular_month}")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"\nThe most popular day is {popular_day}")

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Start Hour'].mode()[0]
    print(f"\nThe most popular Start Hour is {popular_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most popular Start Station is {popular_start_station}")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"\nThe most popular End Station is {popular_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + 'to' + df['End Station']
    popular_combination = df['Start to End'].mode()[0]
    print(f"\nThe most frequent combination of Start and End Station is {popular_combination}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"\nThe total travel time is {total_travel_time}")


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"\nThe mean travel time is {mean_travel_time}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print(f"\nThe count of user type is {count_user_type}")


    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()
    print(f"\nThe count of gender is {count_gender}")


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
