import smtplib
import emailSpammerConfig



def send_mail(subject, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(emailSpammerConfig.SENDER_ACCOUNT, emailSpammerConfig.SENDER_PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, msg)
        server.sendmail(emailSpammerConfig.SENDER_ACCOUNT, emailSpammerConfig.TO_ADDRESS, message)
        server.close()
        print("email succeeded")
    except:
        print("email failed")


counter = 0
while counter < emailSpammerConfig.SPAM_AMOUNT:
    send_mail(emailSpammerConfig.subject, emailSpammerConfig.message)
    emailSpammerConfig.subject += "n"
    counter += 1


