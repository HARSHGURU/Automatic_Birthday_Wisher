import random
import pandas
import datetime as dt
import smtplib
PLACEHOLDER = "[NAME]"
YOUR_NAME = ""  #replace with sender name


#Setting sender data
my_email = "SENDER EMAIL ADDRESS"  #Replace with sender email address
password = "APP PASWORD"  #Sender APP Password

#Reading csv file
person_info = pandas.read_csv("birthdays.csv")
person_info_dict = person_info.to_dict(orient="records")

#Reading date time
now = dt.datetime.now()
month = now.month
day = now.day
hr = now.hour
mn = now.minute
sec = now.second


#Sending emails
print(person_info_dict)
print(month, day)
for item in person_info_dict:
    if item['day'] == day and item['month'] == month:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_to_send = letter.read()
        name = letter_to_send.replace(PLACEHOLDER, item['name'])
        message = name.replace("[SENDER NAME]", YOUR_NAME)
        print(message)
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item["email"],
                msg=f"Subject:Birthday wishes\n\n{message}")
        print(f"Message send to {item['name']}")


#
#




