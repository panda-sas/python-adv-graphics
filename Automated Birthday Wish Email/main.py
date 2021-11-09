##################### Normal Starting Project ######################

import pandas
from datetime import datetime
import random
import smtplib

MYEMAIL = "panda@tamu.edu"
PASSWORD = "12234567"

today = datetime.now()
today_tuple = (today.month, today.date)
# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL, PASSWORD)
        connection.sendmail(from_addr=MYEMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")