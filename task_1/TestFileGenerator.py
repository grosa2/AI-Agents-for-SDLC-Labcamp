from datetime import date
import random
from random import randint, choice
import sys
import time
import faker
from datetime import datetime
import os
from argparse import ArgumentParser

os.environ['TZ'] = 'Europe/Rome'

fak = faker.Faker()

LOGS_FILE = "server_logs.txt"
TIMESTAMP_FILE = "timestamps.txt"


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end):
    prop = random.random()
    date_str = str_time_prop(start, end, '%d/%b/%Y:%H:%M:%S', prop)
    date_obj = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')

    # Get the current local timezone offset
    offset_seconds = time.localtime().tm_gmtoff
    offset_hours = offset_seconds // 3600
    offset_minutes = (offset_seconds % 3600) // 60
    offset_sign = '+' if offset_seconds >= 0 else '-'
    
    # Format the timezone offset as +HHMM or -HHMM
    tz_offset = f"{offset_sign}{abs(offset_hours):02}{abs(offset_minutes):02}"
    
    # Format the final output with the timezone offset
    return date_obj.strftime('%d/%b/%Y:%H:%M:%S') + f" {tz_offset}"


def main(entries: int):
    dictionary = {
        'request': ['GET', 'POST', 'PUT', 'DELETE'], 
        'endpoint':  [
        '/usr', '/usr/admin', '/usr/admin/developer', '/usr/login', '/usr/register',
        '/api/v1/resource', '/api/v1/resource/item', '/api/v1/resource/item/details', '/api/v1/auth/login', '/api/v1/auth/logout',
        '/products', '/products/electronics', '/products/clothing', '/products/books', '/cart', '/checkout', '/orders', '/orders/history',
        '/home', '/about', '/contact', '/contact/form', '/help', '/help/faq', '/terms', '/privacy', '/settings', '/settings/profile',
        '/dashboard', '/dashboard/analytics', '/dashboard/users', '/reports', '/reports/daily', '/reports/monthly'
        ],
        'statuscode': ['303', '404', '500', '403', '502', '304','200'], 
        'username': ['james', 'adam', 'eve', 'alex', 'smith', 'isabella', 'david', 'angela', 'donald', 'hilary'],
        'ua': [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
            'Mozilla/5.0 (Android 10; Mobile; rv:84.0) Gecko/84.0 Firefox/84.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4380.0 Safari/537.36 Edg/89.0.759.0',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.12.4.5121',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.329',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
            'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1127_15266) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36 Edge/18.19041',
            'Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.7 (KHTML, like Gecko) NF/4.0.0.10.20 NintendoBrowser/5.1.0.13343',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; en-gb; SHIELD Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ],
        'referrer' : ['-',fak.uri()]
    }

    with open(LOGS_FILE, "w") as f, open(TIMESTAMP_FILE, "w") as f2:
        for _ in range(1,entries):
            ts = random_date("01/Jan/2048:12:00:00","01/Jan/2050:12:00:00")
            f.write('%s - - [%s] "%s %s HTTP/1.0" %s %s "%s" "%s" %s\n' % 
                (fak.ipv4(),
                ts, 
                choice(dictionary['request']),
                choice(dictionary['endpoint']),
                choice(dictionary['statuscode']),    
                str(int(random.gauss(5000,50))),
                choice(dictionary['referrer']),
                choice(dictionary['ua']),
                random.randint(1,5000)))

            f2.write(ts + "\n")

    print("Saved:", LOGS_FILE, TIMESTAMP_FILE)

if __name__ == "__main__":
     # add arg parse for number of lines
    args = ArgumentParser()

    args.add_argument("--entries", "-e", type=int, help="Number of lines to generate", default=100000)
    args = args.parse_args()

    main(args.entries)