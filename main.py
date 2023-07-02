import datetime as dt
import random
import smtplib

my_email = "Your email"
my_password = "Your pass"

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
            to_addrs="abc@example.com",
            msg=random_quote
        )


print("Sent successfully")



# import smtplib

# my_email = "Your email"
# my_password = "Your pass"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="receiving_@mail.com",
#         msg="Hello!"
#     )

#

#
#
#
# import datetime as dt
#
# date_of_birth = dt.datetime(year=2000, month=6, day=5, hour=4, minute=45, second=35)
# print(f"My Date of birth is: {date_of_birth}")


