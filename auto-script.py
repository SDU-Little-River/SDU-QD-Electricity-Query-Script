import argparse
from email.mime.base import MIMEBase
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from QueryScript import query
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    # Create the email
    msg = MIMEMultipart()
    from_name = "宿舍电量警告"
    msg['From'] = formataddr((from_name, from_email))
    res=''
    for To in to_email:
        res+=To+','
    msg['To'] = res
    msg['Subject'] = subject
    msg.attach(MIMEText('<html><body><p>'+body +'</p>' +
    '</body></html>', 'html', 'utf-8'))
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login, password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--email', required=True, help='Email address')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--Synjones_Auth', required=True, help='Synjones_Auth')
    args = parser.parse_args()
    
    email = args.email
    password = args.password
    Synjones_Auth = args.Synjones_Auth
    print(f"Email: {email}")
    print(f"Password: {password}")

    from_email = email
    smtp_server = "smtphm.qiye.163.com"
    smtp_port = 587
    login = email
    password = password
    subject = "宿舍电量提醒"
    last=query("S11",221,Synjones_Auth=Synjones_Auth)
    body = f"byd同学：<br><br>您好！<br><br>您的宿舍电量不足，仅剩{float(last)}度，请及时充值。"
    if float(last)<10:
        # Read email list from Excel file
        email_list = ["335539025@qq.com","1420334086@qq.com","2292871187@qq.com","2857029527@qq.com"]

        send_email(subject, body, email_list, from_email, smtp_server, smtp_port, login, password)
    
