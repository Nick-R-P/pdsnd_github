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
    city_input = False
    city = input ("Please input one of the follow cities Chicago, New York City or Washington           ")
    while city_input == False:
        if city.lower() in CITY_DATA:
            city_input = True
        else:
            city = input("The city you entered was not valid please try again: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = False
    while month_input == False:
        month = input("Please enter the month you wish to filter by:            ")
        if month.lower() == 'january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june' or month.lower() == 'all':
            month_input = True
        else:
            print("Please enter a valid month between january and june or 'all'")         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = False
    while day_input == False:
        day = input("Please enter the day you wish to filter by:            ")
        if day.lower() == 'sunday' or day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or day.lower() == 'thursday' or day.lower() == 'friday' or day.lower() == 'saturday' or day.lower() == 'all':
            day_input = True
        else:
            print("Please enter a valid day or 'all'") 
    
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
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')
        
    month_num = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6}
    day_num = {'monday' : 0, 'tuesday' : 1, 'wednesday' : 2, 'thursday' : 3, 'friday' : 4, 'saturday' : 5, 'sunday' : 6}
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    if month.lower() != "all":
                df = df[df['Start Time'].dt.month == month_num[month.lower()]]
                
    if day.lower() != "all":
                df = df[df['Start Time'].dt.dayofweek == day_num[day.lower()]]
            
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  
    month_num = {'1' : 'January', '2' : 'February', '3' : 'March', '4' : 'April', '5' : 'May', '6' : 'June'}
   
    day_num = {'0' : 'Monday', '1' : 'Tuesday', '2' : 'Wednesday', '3' : 'Thursday', '4' : 'Friday', '5' : 'Saturday', '6' : 'Sunday'}
    # TO DO: display the most common month
    #print (df['Start Time'].dt.month.mode()[0])
    print (month_num[str(df['Start Time'].dt.month.mode()[0])])
    #print (month_num.get(str(df['Start Time'].dt.month.mode()[0])))
    

    # TO DO: display the most common day of week
    print (day_num[str(df['Start Time'].dt.dayofweek.mode()[0])])

    # TO DO: display the most common start hour
    print (str(df['Start Time'].dt.hour.mode()[0]) + ":00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print (df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print (df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df ['Trip'] = df['Start Station'] + " to " + df['End Station']
    print (str(df['Trip'].mode()[0])+ " route was taken " + str(df['Trip'].value_counts().max()) + " times")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print (str(df['Trip Duration'].sum()) + " seconds")

    # TO DO: display mean travel time
    print (str(df['Trip Duration'].mean()) + " seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    for i in range(len(df['User Type'].unique())):
        print (str(df['User Type'].unique()[i]) + " : " + str(df['User Type'].value_counts()[i]) )
            
   
       
    # TO DO: Display counts of gender
    try:    
        for i in range(len(df['Gender'].dropna().unique())):
            print (str(df['Gender'].dropna().unique()[i]) + " : " + str(df['Gender'].value_counts()[i]) )
    except KeyError:
        print ("No Gender data available")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print ("\nThe oldest birth year of riders is: " + str(df['Birth Year'].min()))
        print ('The youngest birth year of riders is: ' + str(df['Birth Year'].max()))
        print ('The most common brith year of riders is: ' + str(df['Birth Year'].mode()))
    except KeyError:
        print("No birth year data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df):
    """This function displays the raw data of the csv file 5 rows at a time"""
    raw_input = True
    raw_data = input('Would you like to see the first 5 lines of raw data?(Y/N) ')
    while raw_input == True:
        if raw_data.lower() == 'y':
            print(df.head(5))
            raw_input = False
        elif raw_data.lower() == 'n':
            break
        else:
            raw_data = input('Please enter Y or N')
        
    raw = True
    count = 5
    if raw_data.lower() == 'y':
        while raw == True:
            next_lines = input('Would you like to see the next 5 lines of raw data?(Y/N) ')
            if next_lines.lower() == 'y':
                print(df.iloc[(count):(count+5),:])
                count +=5
            elif next_lines.lower() == 'n':
                break
            else:
                next_lines = input('Please enter Y or N')
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            

if __name__ == "__main__":
	main()



