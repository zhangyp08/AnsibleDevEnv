
import configparser
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os
from testdata.getpath import GetTestConfig

class MyMail:
    def __init__(self, mail_config_file):
        config = configparser.ConfigParser()
        config.read(mail_config_file)

        self.smtp = smtplib.SMTP_SSL()

        self.login_user = config.get('SMTP', 'login_user')
        self.log_pwd = config.get('SMTP', 'login_pwd')
        self.from_addr = config.get('SMTP', 'from_addr')
        self.to_addrs = config.get('SMTP', 'to_addrs')
        self.host = config.get('SMTP', 'host')
        self.port = config.get('SMTP', 'port')

        print(self.login_user)

    def connect(self):
        self.smtp.connect(self.host, self.port)

    def login(self):
        try:
            self.smtp.login(self.login_user, self.log_pwd)
        except Exception as e:
            print('%s' % e)

    def send_mail(self, mail_subject, mail_content, attachment_path_set):
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(eval(self.to_addrs))
        msg['Subject'] = mail_subject

        content = MIMEText(mail_content, 'html', _charset='gbk')
        msg.attach(content)

        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path):
                type, coding = mimetypes.guess_type(attachment_path)
                if type == None:
                    type = 'application/octet-stream'

                major_type, minor_type = type.split('/', 1)
                with open(attachment_path, 'rb') as file:
                    if major_type == 'text':
                        attachment = MIMEText(
                            file.read(), _subtype=minor_type, _charset='GB2312'
                        )
                    elif major_type == 'image':
                        attachment = MIMEImage(
                            file.read(), _subtype=minor_type
                        )
                    elif major_type == 'application':
                        attachment = MIMEApplication(
                            file.read(), _subtype=minor_type
                        )
                    elif major_type == 'audio':
                        attachment = MIMEAudio(
                            file.read(), _subtype=minor_type
                        )

                attachment_name = os.path.basename(attachment_path)
                attachment.add_header(
                    'Content-Disposition', 'attachment', filename=('gbk', '', attachment_name)
                )

                msg.attach(attachment)

        full_text = msg.as_string()
        self.smtp.sendmail(self.from_addr, eval(self.to_addrs), full_text)

    def quit(self):
        self.smtp.quit()

mymail = MyMail(GetTestConfig('mail.conf'))
mymail.connect()
mymail.login()
mail_content = 'Hi the attached ment is test report, please review'
mail_title = '[test_report] test report'

attachments = set(['C:\\Users\\zhangy40\\Documents\\AnsibleDevEnv\\untitled1\\interfacecourse\\4th\\testreport\\2018-11-18-01-39-47-TestReport.xls'])

mymail.send_mail(mail_title, mail_content, attachments)
mymail.quit()

