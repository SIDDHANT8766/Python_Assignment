#-------------------------------------------------------------
# Required imports
#-------------------------------------------------------------

import smtplib
from email.message import EmailMessage
import schedule
import time
import os


#--------------------------------------------------------------
# Function : send_mail 
# Description : Send email with log file attachment
#--------------------------------------------------------------

def send_mail(sender, app_password, receiver, subject, body):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Attach Log File (if exists)
    filename = "MemoryLog.log"

    if os.path.exists(filename):

        with open(filename, "rb") as myfile:
            file_data = myfile.read()

        msg.add_attachment(
            file_data,
            maintype = "application",
            subtype = "octet-stream",
            filename = filename
        )
    else:
        print("Log file not found")

    # Step 5 : Create SMTP SSL connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 6 : Login
    smtp.login(sender, app_password)

    # Step 7 : Send email
    smtp.send_message(msg)

    print("Mail Sent Successfully")

    # Step 8 : Close connection
    smtp.quit()


#-------------------------------------------------------
# Function : main
# Description : Driver code
#------------------------------------------------------

def main():
    
    sender_email = "siddhuBhai9135@gmail.com"
    app_password = "ugai hifp ttbs vajg"
    receiver_email = "siddhantnew8766@gmail.com"

    subject = "Email Report"

    body = """Jay Ganesh,

This is the automated monitoring report.

Please find the attached log file.

Regards,
Siddhant Gadkari
"""

    # First time send immediately
    send_mail(sender_email, app_password, receiver_email, subject, body)

    # Schedule every 10 minutes
    schedule.every(10).minutes.do(
        send_mail,
        sender_email,
        app_password,
        receiver_email,
        subject,
        body
    )

    # Infinite loop
    while True:
        schedule.run_pending()
        time.sleep(1)


#--------------------------------------------------------------------
# Program Entry Point
#--------------------------------------------------------------------

if __name__ == "__main__":
    main()