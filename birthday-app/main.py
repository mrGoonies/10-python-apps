from datetime import date


def get_birthday_user() -> date:
    year_birthday: int = int(input("What year were you born [YYYY]?\n>> "))
    month_birthday: int = int(input("What month were you born [MM]?\n>> "))
    day_birthday: int = int(input("What day were you born [DD]?\n>> "))
    
    # Convert requested data into a date
    date_birthday: date = date(year_birthday, month_birthday, day_birthday)

    return date_birthday


def compute_days_between_date(birthday_user: date):
    pass


if __name__ == "__main__":
    todays_date: date = date.today()
    print("-" * 30)
    print("\tBirthday App")
    print("-" * 30)
    print()
    
    birthday = get_birthday_user()
    print(birthday)
