import pandas
import random
import datetime as dt
import smtplib

email_1 = "tiboma08@gmail.com"
password_1 = "nfvg wtar froi kmte"
email_2 = "tiboma08@yahoo.com"

now = dt.datetime.now()
birth_data = pandas.read_csv("birthdays.csv")

for (index, row) in birth_data.iterrows():
    if row.month == now.month and row.day == now.day:
        letters = ["./letter_templates/letter_3.txt", "./letter_templates/letter_2.txt",
                   "./letter_templates/letter_1.txt"]
        random_letter = random.choice(letters)
        with (open(random_letter, "r") as file):
            message = file.read()
            receiver = row["name"]  # Alternatively --> birth_data.iloc[index]["name"]
            personal_message = message.replace("[NAME]", receiver)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_1, password=password_1)
            connection.sendmail(
                from_addr=email_1,
                to_addrs=email_2,
                msg=f"Subject: Happy Birthday {receiver}!\n\n{personal_message}"
            )




