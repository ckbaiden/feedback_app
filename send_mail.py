import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '0ea3030a46c94c'
    password = 'c670bc272bb219'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = "Private Person <from@smtp.mailtrap.io>"
    receiver_email = "A Test User <to@smtp.mailtrap.io>"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Jaguar Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
