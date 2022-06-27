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
    city = input("Enter a city name (chicago, new york city, washington): \n").lower()
    while city not in CITY_DATA.keys():
        print("You entered an invalid city, please enter a valid one\n")
        city = input(
            "Enter a city name (chicago, new york city, washington): \n"
        ).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        month = input(
            "Enter a month: (all, january, february, march, april, may, june)"
        ).lower()
        if month in months:
            break
        else:
            print("You entered an invalid month, please enter a valid one\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = [
        "all",
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]
    while True:
        day = input(
            "Enter a day: (all, sunday, monday, tuesday, wednesday, thursday, friday, saturday)"
        ).lower()
        if day in days:
            break
        else:
            print("You entered an invalid day, please enter a valid one\n")

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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["start hour"] = df["Start Time"].dt.hour
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]
    if day != "all":

        df = df[df["day_of_week"] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month : {}".format(df["month"].mode()[0]))


    # TO DO: display the most common day of week
    print("Most common day : {}".format(df["day_of_week"].mode()[0]))


    # TO DO: display the most common start hour
    print("Most common start hour : {}".format(df["start hour"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station : {}".format(df["Start Station"].mode()[0]))


    # TO DO: display most commonly used end station
    print("Most common end station : {}".format(df["End Station"].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df["route"] = df["Start Station"] + "," + df["End Station"]
    print("Most common route : {}".format(df["route"].mode()[0]))
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time : ", (df["Trip Duration"].sum()).round())


    # TO DO: display mean travel time
    print("Average travel time : ", (df["Trip Duration"].mean()).round())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts().to_frame())


    # TO DO: Display counts of gender
    if city != "washington":
        print(df["Gender"].value_counts().to_frame())
        # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest year of birth : ", int(df["Birth Year"].min()))
        print("Most recent year of birth : ", int(df["Birth Year"].max()))
        print("Most common year of birth : ", int(df["Birth Year"].mode()[0]))
    else:
        print("There is no data for washington")

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # Asking the user wether he like to display the raw data of that city as chunks of 5 rows based on his input.
    print("\nRaw data is available to check....\n")

    user_input = input(
        "Would you like to view 5 rows of individual trip data? Enter yes or no?"
    ).lower()
    index = 0
    if user_input not in ["yes", "no"]:
        print("Invalid choice.\n")
        user_input = input(
            "Would you like to view 5 rows of individual trip data? Enter yes or no?"
        ).lower()
    elif user_input == "no":
        print("Thanks\n")
    else:
        while index + 5 < df.shape[0]:
            print(df.iloc[index : index + 5])
            index += 5
            user_input = input(
                "Would you like to view 5 more rows of individual trip data? Enter yes or no?"
            ).lower()
            if user_input != "yes":
                print("Thanks\n")
                break
            
    
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
