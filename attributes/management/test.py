import sys
import bs4 as bs
import urllib.request
from time import strptime
from datetime import datetime
import mysql.connector
import arrow
import os
import os as inner_os
import requests
import json
start = datetime(2020,2,15)
end = datetime(2020,2,15)
numberOfMonths = 0
for d in arrow.Arrow.range('month', start, end):
    numberOfMonths += 1
print(numberOfMonths)