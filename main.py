#
#
# import smtplib
#
# my_email = "hisherhim2022@gmail.com"
# my_password = "fqhbljpavieykgoz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="lakho75@yahoo.com",
#         msg="Hello!"
#     )
#
#

#
#
#
# import datetime as dt
#
# date_of_birth = dt.datetime(year=2000, month=6, day=5, hour=4, minute=45, second=35)
# print(f"My Date of birth is: {date_of_birth}")


import datetime as dt
import random
import smtplib

my_email = "hisherhim2022@gmail.com"
my_password = "fqhbljpavieykgoz"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    print("It's monday")
    with open("quotes.txt") as file:
        random_quote = random.choice(file.readlines())

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="lakho75@yahoo.com",
            msg=random_quote
        )


print("Sent successfully")