# Job: Converting text strings into dates
from datetime import date
import pandas as pd
import dateparser
b["fecha2"] = b.datetime.apply(lambda x: dateparser.parse(x))


text_strings = ["02-02-22", "02/09/2022", "02.07.2022"]


date_time_string = pd.to_datetime(text_strings, format = "%d-%m-%y")


date_time_string = pd.to_datetime(text_strings, format = "%d*%m*%y")


date_string.year

date_string.month

date_string.day



