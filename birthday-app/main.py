from datetime import date


def custom_message(difference_date: int) -> None:
    """
    We deliver a personalized message depending o the missing days of the user's birthday.

    :param difference_date: Result betweeen the user's birthday date and the current day.
    :return:
        No value is returned, we only print a message upon fulfillment of a condition.
    """
    if difference_date == 0:
        print("Happy Birthday!!")
    elif difference_date < 0:
        print(f"You had your birthday {difference_date} days ago this year.")
    else:
        print(f"These are the days left until your birthday!\n{difference_date}")

def get_birthday_user() -> date:
    """ Request the user's date of birth.

    :return: The date if birth parsed from integer to date type.
    """
    year_birthday: int = int(input("What year were you born [YYYY]?\n>> "))
    month_birthday: int = int(input("What month were you born [MM]?\n>> "))
    day_birthday: int = int(input("What day were you born [DD]?\n>> "))
    
    # Convert requested data into a date
    date_birthday: date = date(year_birthday, month_birthday, day_birthday)

    return date_birthday

def compute_days_between_date(birthday_user: date) -> date.day:
    """
    We obtain the difference in days between the current year and the year of birth.

    :param birthday_user:
    :return:
    """
    today_date: date = date.today()
    date_difference = today_date - birthday_user

    return date_difference.days
if __name__ == "__main__":

    print("-" * 30)
    print("\tBirthday App")
    print("-" * 30)
    print()

    birthday = get_birthday_user()
    result = compute_days_between_date(birthday)

    custom_message(result)

