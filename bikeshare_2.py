import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["all", "january", "february", "march","april","may","june","july"]
days = ("all","monday","tuesday","Wednesday","thuresday","friday","saturday","sunday")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA.keys():
        city = input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
        if  city not in CITY_DATA.keys():
            print("Please enter a valid input\n")
            print("Restaring...")
    
    print(f"\nYou have chosen {city.title()} as your city.")        
        


        
    # get user input for month (all, january, february, ... , june)
    months = {"january":1, "february":2, "march":3,"april":4,"may":5,"june":6,"july":7,"all":8}
    month = ""
    while month not in months.keys():
        print("\n Please enter a valid month from january to june")
        month = input("\n Would you like to filter the data by month, day, both, or not at all? Type (None) for no time filter.\n").lower()
        if month not in months :
             print("Please enter a valid input\n")
             print("Restaring...")
             
    print(f"\nYou have chosen {month.title()} as your month.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = {"monday":1,"tuesday":2,"Wednesday":3,"thuresday":4,"friday":5,"saturday":6,"sunday":7,"all":8}
    day = ""
    while day not in days:
        day = input("which day? \n")
        if day not in days:
             print("Please enter a valid input\n")
             print("Restaring...")
             
    print(f"\nYou have chosen {day.title()} as your day.")         

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
    print("\n Loading Data\n")
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
 
    # display the most common month
    pop_month = df['month'].value_counts().mode()[0]
    print(f"\n Most popular month : {pop_month}")
    # display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print(f"\n Most Popular day : {pop_day}")
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    pop_hour = df['hour'].mode()[0] 
    print(f"\n Most Popular hour : {pop_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
######### here we go git #########

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used start station {commonly_start_station}")

    # display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station {commonly_end_station }")
    # display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep = ("to")).mode()[0]
    print(f"\nThe most frequent combination of start station and end station trip : {df['Start to End']}.")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########## git is so powerful tool ###########
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum() 
    print(f"\n Total travel duration time: {total_travel}")
    # display mean travel time
    mean_travel = round(df['Trip Duration'].mean())
    print(f"\n Mean travel duration time: {mean_travel}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"\n Type of users by number{user_type}")
    
    # Display counts of gender
    try: 
        gender_type = df['Gender'].value_counts()
        print(f"\n The type of users by gender are {gender_type}")
        
    except:
        print("\n This file has no gender type in it")    

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth year'].min())
        print(f"\nThe earliest year of birth: {earliest}")
        
        recent = int(df['Birth year'].max())
        print(f"\n The recent year of birth:{recent}")
        
        common = int(df['Birth year'].mode()[0])
        print(f"\n The common year of birth:{common}")
    
    except:
        print("There is no birth year on this file.")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
####### Adding New Feature in diplay_raw_data #########
def display_raw_data(df):
         
    view_data = input("\n Would you like to view 5 rows of individual trip data? Enter yes or no\n ").lower()
    start_loc = 0
    while view_data != "no":
        print(df.iloc[start_loc: 5])
        start_loc += 5
        view_display = input("Do you wish to continue?\n").lower()
        
        if view_display == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
        elif view_display != 'yes':
            break
######## New feature added ###########
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
