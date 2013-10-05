#!/usr/bin/env python3

from lib.load import get_members, get_content
from lib.email_lib import Message, EmailHandler
import sys
MIN_VER = (3, 0)
CUR_VER = sys.version_info

def main():
    # Get mail content
    content = get_content('content.txt')
    members = get_members(content.destination)
    ucdragonMail = EmailHandler(content.server, content.username, content.password)
    messageList = [Message(content.subject, content.sender, member.email, member.name, content.text, content.attachments, content.type) for member in members]
    ucdragonMail.send(messageList)

if __name__ == "__main__":
    if CUR_VER >= MIN_VER:
        main()
    else:
        print('Python {}.{}.{} is not supported, Use Python3 instead'.format(CUR_VER[0], CUR_VER[1], CUR_VER[2]))
