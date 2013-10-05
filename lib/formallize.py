import sys
subject = input('Subject: ')
sender = input('From: ')
destination = input('To: ')

content = b''
while True:
    line = input().decode(sys.stdin.encoding)
    if not line:
        break
    content += line


print(subject)
print(sender)
print(destination)
print(content)