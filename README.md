EmailSender
===========

Open source email sender written in python3, which contains
"content.txt", "test.csv" you can modify.


content.txt
-----------
In "content.txt", you must add your own information for the program to run. The format of the content.txt is shown as follow.

>type:           # html recommanded
>subject:        # your subject here
>from:           # sender's email address
>to:             # receiver's email address, as cdv file
>attachments:    # attachments, separated by comma
>server:         # server address with ports, such like smtp.gmail.com:587
>username:       # username to login your email account
>password:       # your password to login your email account
>texts:
                # texts you want to send, with {} if you want to specify the receiver's name

Here is a copy of a sample of "content.txt"

>type:html
>subject:Mails header here
>from:sample@email.com
>to:client.csv
>attachments:photo1.jpg, photo2.jpg, aud.mp3, doctm4.docx
>server:smtp.gmail.com:587
>username:username
>password:password
>texts:
>Hello {}, this is just a test mail specially for you.

test.csv
--------
In test.csv, you juse need make sure you are using the conbination of
**Name, Email, Photo, ... **to organize your client's profile