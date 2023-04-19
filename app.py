# IMPORT
from utils.log import *
from utils.req import *
from utils.printJSON import *

import csv
import base64
import os
from dotenv import load_dotenv

# Variables
load_dotenv()
csvFile = os.environ.get('CSVFILE')
fromAccount = os.environ.get('FROMACCOUNT')
toAccount = os.environ.get('TOACCOUNT')

# Setup Logging
create_log()


def migrate_user(email):
    url = '/accounts/%s/users/%s/account' % (fromAccount, email)
    data = {"account_id": toAccount}
    action = 'put'
    response = send_request(action, url, data)


def switch_users():
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            email = row[0]
            migrate_user(email)
