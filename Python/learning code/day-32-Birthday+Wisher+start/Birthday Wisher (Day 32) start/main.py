import smtplib
import datetime as dt
import random


# email_1 = "tiboma08@gmail.com"
# password_1 = "nfvg wtar froi kmte"
# email_2 = "tiboma08@yahoo.com"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=email_1, password=password_1)
# connection.sendmail(from_addr=email_1, to_addrs=email_2, msg="Subject: Hello again\n\nsecond testing email")
# connection.close()

email_1 = "tiboma08@gmail.com"
password_1 = "nfvg wtar froi kmte"
email_2 = "tiboma08@yahoo.com"

now = dt.datetime.now()
print(now.month)
week_day = now.weekday()
if week_day == 4:
    with open("quotes.txt", "r") as quotes:
        message = quotes.readlines()
        email_message = random.choice(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_1, password=password_1)
        connection.sendmail(
            from_addr=email_1,
            to_addrs=email_2,
            msg=f"Subject: Hello Friday\n\n{email_message}"
        )

