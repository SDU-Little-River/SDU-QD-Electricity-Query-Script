import argparse
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from QueryScript import query

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart()
    from_name = "宿舍电量警告"
    msg['From'] = formataddr((from_name, from_email))
    if isinstance(to_email, list):
        msg['To'] = ",".join(to_email)
    else:
        msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText('<html><body><p>'+body +'</p>' +
    '</body></html>', 'html', 'utf-8'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login, password)

    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()

if __name__ == "__main__":
    import yaml
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--email', required=True, help='Email address')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--Synjones_Auth', required=True, help='Synjones_Auth')
    parser.add_argument('--email_list',  help='Additional email addresses')
    args = parser.parse_args()
    
    email = args.email
    password = args.password
    Synjones_Auth = args.Synjones_Auth
    print(f"Email: {email}")
    print(f"Password: {password}")

    from_email = email
    smtp_server = "smtp.qq.com" # 此处使用山大云邮（网易企业邮箱）的SMTP服务器
    smtp_port = 587
    login = email
    password = password
    subject = "宿舍电量提醒"
    last = query("S2", a629, Synjones_Auth=Synjones_Auth)
    print(f"Query result: {last}")  # 添加调试信息

    try:
        last_value = float(last)
        body = f"byd同学：<br><br>您好！<br><br>您的宿舍电量不足，仅剩{last_value}度，请及时充值。"
        if last_value < 10: #last_value 为宿舍剩余电量，低于10度时发送邮件提醒，可根据实际情况修改
            email_list = args.email_list.split(",") if args.email_list else []
            send_email(subject, body, email_list, from_email, smtp_server, smtp_port, login, password)
    except ValueError as e:
        print(f"Error converting query result to float: {e}")
