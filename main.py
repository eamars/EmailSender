#!/usr/bin/env python
from lib.version import _author, _version, _license, _help
from lib.load import get_members, get_content
from lib.email_lib import Message, EmailHandler
from lib.bug_reporter import BugReport
import sys

MIN_VER = (3, 0)
CUR_VER = sys.version_info

def main():
    if len(sys.argv) != 2:
        print(_help)
    else:
        # Get mail content
        content = get_content(sys.argv[1])
        members = get_members(content.destination)
        EmailSender = EmailHandler(content.server, content.username, content.password)
        messageList = [Message(content.subject, content.sender, member.email, member.name, content.text, content.attachments, content.type) for member in members]
        EmailSender.send(messageList)

if __name__ == "__main__":
    if CUR_VER >= MIN_VER:
        print('EmailSender [{}], {}\n'.format(_version, _author))
        main()
    else:
        bug = BugReport('EmailSender', _version)
        bug.submit('Error', 'Python {}.{}.{} is not supported, Use Python3 instead'.format(CUR_VER[0], CUR_VER[1], CUR_VER[2]))
        print('Python {}.{}.{} is not supported, Use Python3 instead'.format(CUR_VER[0], CUR_VER[1], CUR_VER[2]))
