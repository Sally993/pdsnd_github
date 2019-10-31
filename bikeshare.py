import time
import pandas as pd
import numpy as np

# Creating city data dictonary
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Creating month data list
MONTH_DATA = [  'january' ,
                'february' ,
                'march'  ,
                'april' ,
                'may' ,
                'june'       ]

# Creating week days data list
WEEK_DATA = [   'monday',
                'tuesday',
                'wednesday',
                'thursday',
                'friday',
                'saturday',
                'sunday'     ]              



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
    city = input("Would you like to see data for chicago, new york city, or washington? ").lower()

    # checking if the user entered vailed city name and asking him to try again if its invailed input
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Sorry city name is invalid! Please try again:").lower()

    print("It looks like you want to hear about {}".format(city))

   
    # get user input for month (all, january, february, ... , june)
    month = input("Which month? January, February, March , April ,May, or June?").lower()
    # checking if the user entered vailed month and asking him to try again if its invailed input
    while month not in MONTH_DATA:
        month = input("Sorry, Invalid input! Please try again.").lower()
        continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(" Which day? Please type a day.").lower()
    # checking if the user entered vailed day and asking him to try again if its invailed input
    while day not in WEEK_DATA:
        day = input("Sorry, Invalid input! Please try again.").lower()
        continue
    

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
    # reading the city data file
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start column to datetime
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

    
     # asking the user if he wants to get the most common month of travel           
    while True:
        month_mode= input("Do you want to get the most common month of travel? yes/no \n ").lower()
        if month_mode=="yes":
             # display the most common month
               print("The most common month is: {}".format(
               str(df['month'].mode()[0])) ) 
               break
        elif month_mode=="no":
                break


    
     # asking the user if he wants to get the most common day of the week           
    while True:
        day_of_week_mode= input("Do you want to get the most common day of the week? yes/no \n").lower()
        if day_of_week_mode=="yes":
             # display the most common day of week
               print("The most common day of the week is: {}".format(
               str(df['day_of_week'].mode()[0])) ) 
               break
        elif day_of_week_mode=="no":
                break

              
    
     # asking the user if he wants to get the most common start hour of travel           
    while True:
        hour_mode= input("Do you want to get the most common start hour of travel? yes/no \n ").lower()
        if hour_mode=="yes":
             # display the most common start hour
            df['start_hour'] = df['Start Time'].dt.hour
            print("The most common start hour is: {}".format(
            str(df['start_hour'].mode()[0])) ) 
            break
        elif hour_mode=="no":
                break
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # asking the user if he wants to get the most commonly used start station 
    while True:
        start_station_mode= input("Do you want to get the most commonly used start station ? yes/no \n ").lower()
        if start_station_mode=="yes":
             # display most commonly used start station
            print("The most commonly used start station is: {} ".format(
        df['Start Station'].mode()[0]))
            break
        elif start_station_mode=="no":
            break

    # asking the user if he wants to get the most frequent combination of start station and end station trip
    while True:
        combination_mode= input(
        "Do you want to get the most frequent combination of start station and end station trip ? yes/no \n ").lower()
        if combination_mode=="yes":
             # display most frequent combination of start station and end station trip
            df['combination'] = df['Start Station']+ " " + df['End Station']
            print("The most frequent combination of start station and end station trip is: {}".format(
        df['combination'].mode()[0]) )        
            break
        elif combination_mode=="no":
                break
   

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # calculationg the duration 
    df['duration'] = df['End Time'] - df['Start Time']

    # asking the user if he wants to get the total travel time
    while True:
        total_travel_time= input("Do you want to get the total travel time ? yes/no \n ").lower()
        if total_travel_time=="yes":
            # display total travel time
            print("The total travel time is: {}".format(
            str(df['duration'].sum())) )
            break

        elif total_travel_time=="no":
                break
     
    # asking the user if he wants to get the mean travel time
    while True:
        mean_travel_time= input("Do you want to get the mean travel time ? yes/no \n ").lower()
        if mean_travel_time=="yes":
            # display mean travel time
            print("The mean travel time is: {}".format(
            str(df['duration'].mean())) )
            break

        elif mean_travel_time=="no":
                break        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # asking the user if he wants the counts of user types
    while True:
        user_count= input("Do you want to get the counts of user types ? yes/no \n ").lower()
        if user_count=="yes":
             # Display counts of user types
            print("The counts of user types:")
            print(df['User Type'].value_counts())
            break
        elif user_count=="no":
            break
    
    # asking the user if he wants to get the counts of gender
    while True:
        if city != 'washington':
            gender_count= input("Do you want to get the counts of gender  ? yes/no \n ").lower()
            if gender_count=="yes":
              # Display counts of gender
              print("The counts of gender:")
              print(df['Gender'].value_counts())
              break
            elif gender_count=="no":
                break

    
        
    # asking the user if he wants to get the earliest birth year
    while True:
          earliest_year= input("Do you want to get the earliest birth year ? yes/no \n ").lower()
          if earliest_year=="yes":
            # Display earliest year of birth
            print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min()))))
            break
          elif earliest_year=="no":
            break

    # asking the user if he wants to get the most recent birth year
    while True:
          lastest_year= input("Do you want to get the most recent birth year ? yes/no \n ").lower()
          if lastest_year=="yes":
            # Display most recent year of birth
            print("The most recent birth year is: {}".format(
            str(int(df['Birth Year'].max()))))
            break
          elif lastest_year=="no":
            break

    # asking the user if he wants to get the most common birth year
    while True:
          year_mode= input("Do you want to get the most common birth year ? yes/no \n ").lower()
          if year_mode=="yes":
             # Display most common year of birth
             print("The most common birth year is: {}".format(
             str(int(df['Birth Year'].mode().values[0]))) )
             break
          elif year_mode=="no":
             break
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """
    # asking the user if he wants to see 5 rows of the raw data
    n=0
    end=5
    display = input("Do you want to see the raw data?: ").lower()

    if display == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[n:n+5])
            n += 5
            
            # asking the user if he wants to see more 5 rows of the raw data
            finish = input("Do you want to see more raw data?: ").lower()
            if finish == 'no':
                break  

def main():
    # calling the data frame after applying functions on the data frame
    while True:
        city, month, day = get_filters()
        df =load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        # asking the user if he wants to restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()