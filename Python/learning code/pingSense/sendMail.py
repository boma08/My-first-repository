import smtplib
import ping
import devices

email_1 = "tiboma08@gmail.com"
password_1 = "nfvg wtar froi kmte"
email_2 = "tiboma08@yahoo.com"

def send_offline_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_1, password=password_1)
        connection.sendmail(
            from_addr=email_1,
            to_addrs=email_2,
            msg=f"Subject: Attention!!! Device offline\n\nThe {devices.device_list[0]["description"]} at "
                f"{devices.device_list[0]["location"]} with IP: {devices.device_list[0]["ip address"]} is offline"
        )

def check_online_status():
    if ping.unreachable_count > 1:
        devices.device_list[0]["status"] = "offline"
        send_offline_email()

    elif ping.unreachable_count == 0:
        devices.device_list[0]["status"] = "online"

    ping.unreachable_count = 0
    ping.start_tracking()
