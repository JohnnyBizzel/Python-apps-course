import datetime

def print_header():
    print('--------------------------------')
    print('           BIRTHDAY APP')
    print('--------------------------------')
    pass


def get_birthday_from_usr():
    print('Tell me when you were born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(date_birth, date_now):
    date1 = date_now
    date2 = datetime.datetime(date_now.year, date_birth.month, date_birth.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_info(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print('You had your birthday {} days ago'.format(days))
    else:
        print('Happy birthday')


def main():
    print_header()
    bday = get_birthday_from_usr()
    now = datetime.datetime.now()
    num_of_days = compute_days_between_dates(bday, now)
    print_birthday_info(num_of_days)


main()
