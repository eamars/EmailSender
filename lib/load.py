if __name__ == "__main__":
    from members_lib import Person
    from email_lib import Content
else:
    from .members_lib import Person
    from .email_lib import Content
import codecs
import os

def get_members(filename):
    fp = open(filename, 'r')
    member_list = []
    for line in fp.readlines():
        raw_member = line[:-1].split(',')
        member_list.append(Person(raw_member[0], raw_member[1]))
    fp.close()
    return member_list

def get_content(filename):
    fp = codecs.open(filename, encoding='utf-8')
    commands = []

    # get type
    commands.append(fp.readline().split(':')[1][:-1])

    # get subject
    commands.append(fp.readline().split(':')[1][:-1])

    # get from
    commands.append(fp.readline().split(':')[1][:-1])

    # get to
    commands.append(fp.readline().split(':')[1][:-1])

    # get attachment
    commands.append(fp.readline().split(':')[1].strip().split(','))

    # get server
    commands.append(':'.join(fp.readline().split(':')[1:3])[:-1])

    # get username
    commands.append(fp.readline().split(':')[1][:-1])

    # get password
    commands.append(fp.readline().split(':')[1][:-1])


    # get text
    fp.readline()
    text = fp.read(os.path.getsize(filename))
    fp.close()
    return Content(commands,text)

if __name__ == "__main__":
    print(get_content('../test.txt'))
    