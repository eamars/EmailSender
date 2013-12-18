import smtplib
import os
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from lib.bug_reporter import BugReport

CONTENT_TEMPLATE = """
type: {}
subject: {}
from: {}
to: {}
attachments: {}
server: {}
un: {}
pw: {}
Text:\n\n{}
"""


class Message(object):
    def __init__(self, subject, sender, destination, dest_name, context, attachments = [], text_type='plain'):
        self.msg = MIMEMultipart()
        self.msg['Subject'] = subject
        self.msg['From'] = sender
        self.msg['To'] = destination


        self.msg.attach(MIMEText(context.format(dest_name), text_type, 'utf-8'))
        for attachment in attachments:
            if not os.path.isfile(attachment):
                continue

            ctype, encoding = mimetypes.guess_type(attachment)

            # If cannot guess the type of file, use the generic type
            if ctype is None or encoding is not None:
                ctype = ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)

            # use different method to add file
            if maintype  == 'text':
                fp = open(attachment)
                attachment_bag = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(attachment, 'rb')
                attachment_bag = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'audio':
                fp = open(attachment, 'rb')
                attachment_bag = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(attachment, 'rb')
                attachment_bag = MIMEBase(maintype, subtype)
                attachment_bag.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment_bag)

            # add attachment header and attach to message
            attachment_bag.add_header('Content-Disposition', 'attachment', filename=attachment)
            self.msg.attach(attachment_bag)

    def send(self, server):
        try:
            server.send_message(self.msg)
        except Exception as e:
            raise(e)

    def __str__(self):
        return str(self.msg)


class EmailHandler(object):
    def __init__(self, SMTPserver, username, password):
        self.string_server = SMTPserver
        self.server = smtplib.SMTP(SMTPserver)
        self.username = username
        self.password = password
        self.log = BugReport('EmailSender_email_lib_module', '0')
        print('Waiting to login')

    def send(self, receivers):
        self.server.ehlo()
        self.server.starttls()
        self.server.set_debuglevel(False)
        login = False
        print('Logging in: [{}]\n===================='.format(self.string_server))
        try:
            self.server.login(self.username, self.password)
            login = True
        except Exception as e:
            self.log.submit('Error', str(e))
            print('ERROR[{}]: Bad password or username'.format(str(e)[1:4]))
        
        if login:
            for receiver in receivers:
                print('Sending mail to [{}]'.format(receiver.msg['To']))
                try:
                    receiver.send(self.server)
                    print('Send complete\n====================')
                except Exception as e:
                    self.log.submit('Error', str(e))
                    print('Send error: {}\n===================='.format(e))
                    
            self.server.close()

class Content(object):
    def __init__(self, commands, text):
        self.type = commands[0]
        self.subject = commands[1]
        self.sender = commands[2]
        self.destination = commands[3]
        self.attachments = commands[4]
        self.server = commands[5]
        self.username = commands[6]
        self.password = commands[7]
        self.text = text
    def __str__(self):
        return CONTENT_TEMPLATE.format(self.type, self.subject, self.sender, 
                                    self.destination, self.attachments, self.server, 
                                    self.username, self.password, self.text.encode('utf-8'))



if __name__ == "__main__":
    pass
    
