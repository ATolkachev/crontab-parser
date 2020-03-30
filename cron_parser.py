import argparse
from functools import partial


def print_result(*args):
    template = 'minute\t\t\t{}\nhour\t\t\t{}\nday_of_month\t{}\nmonth\t\t\t{}\nday_of_week\t\t{}\ncommand\t\t\t{}'

    print(template.format(*args))


def parse(string, max_val, month=False):
    try:
        r: str = ''
        if ',' in string:
            for part in string.split(','):
                r = r + parse(part, max, month) + ' '
        elif '/' in string:
            for part in range(0, max_val, int(string.split('/')[1])):
                r = r + str(part) + ' '
        elif '-' in string:
            for part in range(int(string.split('-')[0]), int(string.split('-')[1]) + 1):
                r = r + str(part) + ' '
        elif string == '*':
            for part in range(int(month), max_val + int(month)):
                r = r + str(part) + ' '
        else:
            r = string
    except Exception as e:
        print('Something wrong with string: {}'.format(e))
        exit(1)
    else:
        return r


parse_minute = partial(parse, max_val=60)
parse_hour = partial(parse, max_val=24)
parse_day_of_month = partial(parse, max_val=31)
parse_month = partial(parse, max_val=12, month=True)
parse_day_of_week = partial(parse, max_val=7)


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-c', '--cron', required=True, type=str, help='crontab string')

    args = parser.parse_args()

    cron_string = args.cron.split()

    minute = cron_string[0]
    hour = cron_string[1]
    day_of_month = cron_string[2]
    month = cron_string[3]
    day_of_week = cron_string[4]
    command = ' '.join(cron_string[5:])

    print_result(parse_minute(minute),
                 parse_hour(hour),
                 parse_day_of_month(day_of_month),
                 parse_month(month),
                 parse_day_of_week(day_of_week),
                 command)


if __name__ == "__main__":
    main()
